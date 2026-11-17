from random import Random
rng=Random(20261111)
counts=dict(coefficient=0,public_point=0,polynomial_check=0,ipa_statement=0,
            ipa_folds=0,scalar_commitments=0,example=0,squares=0)
for p in (101,65537):
    def add(*vs): return [sum(xs)%p for xs in zip(*vs)]
    def scale(a,v): return [(a*x)%p for x in v]
    def dot(a,b): return sum(x*y for x,y in zip(a,b))%p
    def had(a,b): return [x*y%p for x,y in zip(a,b)]
    def mat(W,v): return [dot(row,v) for row in W]
    def weights(W,z): return [sum(z[j]*W[j][i] for j in range(len(W)))%p for i in range(len(W[0]))]
    def rand(n): return [rng.randrange(p) for _ in range(n)]

    def check_folds(left, right, gs, hs, U, point):
        """Dobra o ponto público e a testemunha por caminhos independentes."""
        while len(left) > 1:
            half = len(left) // 2
            a, b = left[:half], left[half:]
            c, d = right[:half], right[half:]
            g1, g2 = gs[:half], gs[half:]
            h1, h2 = hs[:half], hs[half:]
            L = add(msm(a, g2), msm(d, h1), scale(dot(a, d), U))
            R = add(msm(b, g1), msm(c, h2), scale(dot(b, c), U))
            u = rng.randrange(1, p)
            inv = pow(u, -1, p)
            point = add(point, scale(u*u, L), scale(inv*inv, R))
            left = add(scale(u, a), scale(inv, b))
            right = add(scale(inv, c), scale(u, d))
            gs = [add(scale(inv, x), scale(u, y)) for x, y in zip(g1, g2)]
            hs = [add(scale(u, x), scale(inv, y)) for x, y in zip(h1, h2)]
            counts['ipa_folds'] += 1
        assert point == add(scale(left[0], gs[0]), scale(right[0], hs[0]),
                            scale(left[0]*right[0], U))

    def check_squares():
        """Forma [X⁴] directamente a partir das três parcelas das duas portas."""
        inputs = [3, 4]
        for lam in range(1, 101):
            y = [1, lam]
            for zeta in (1, 2, 7):
                z1, z2, z3, z4, z5 = [pow(zeta, j, p) for j in range(1, 6)]
                w_left = [z1, z3]
                shift = [z2, z4 * pow(lam, -1, p) % p]
                delta = dot(shift, w_left)
                operand_term = dot(add(inputs, shift), add(had(y, inputs), w_left))
                branch_term = dot(inputs, [-z1-z2, -z3-z4])
                for outputs, value, expected_error in (
                    ([9, 16], 25, 0),
                    ([10, 15], 25, lam - 1),
                    ([9, 16], 24, z5),
                ):
                    result_term = dot(outputs, [z5-1, z5-lam])
                    td = (operand_term + branch_term + result_term) % p
                    public_value = (delta + z5*value) % p
                    assert (td - public_value) % p == expected_error % p
                    if p == 101 and lam == zeta == 2:
                        assert delta == 72
                        assert td == (65 if outputs == [10, 15] else 64)
                    counts['squares'] += 1
        if p == 101:
            # Mesmo circuito com xi = 3 e desafio da dobra e = 2.
            xi, e = 3, 2
            a = add(scale(xi**2, [7, 12]), scale(xi**3, inputs),
                    scale(xi**4, [9, 16]), scale(xi**5, [1, 2]))
            b = add([31, 30], scale(xi, [-6, -24]), scale(xi**2, [5, 16]),
                    scale(xi**5, [3, 2]))
            assert (a, b, dot(a, b)) == ([5, 79], [80, 83], 89)
            inv = pow(e, -1, p)
            final_a = (e*a[0] + inv*a[1]) % p
            final_b = (inv*b[0] + e*b[1]) % p
            folded_product = (dot(a, b) + e**2*a[0]*b[1] + inv**2*a[1]*b[0]) % p
            assert (final_a, final_b, folded_product) == (100, 4, 97)
            assert final_a*final_b % p == folded_product

    for m in (2,4,8):
      for s in range(5):
       for rep in range(8):
        q=4;d=2*s+2;half=s+1
        aL=rand(m);aR=rand(m);aO=had(aL,aR)
        c=[rand(m) for _ in range(s)];dc=[rand(m) for _ in range(s)]
        WL,WR,WO=[[rand(m) for _ in range(q)] for _ in range(3)]
        Wc=[[rand(m) for _ in range(q)] for _ in range(s)]
        # b + Wv v = Wl aL + Wr aR + Wo aO + sum Wk ck.
        # A identidade nas primeiras linhas dá posto de coluna completo a Wv.
        scalar_count = rep % 4
        values, masks = rand(scalar_count), rand(scalar_count)
        Wv = [[int(i == j) for j in range(scalar_count)] for i in range(scalar_count)]
        Wv += [rand(scalar_count) for _ in range(q - scalar_count)]
        b=add(mat(WL,aL),mat(WR,aR),mat(WO,aO),*[mat(W,c_) for W,c_ in zip(Wc,c)],
              scale(-1, mat(Wv, values)))
        lam,zeta=[rng.randrange(1,p) for _ in range(2)]
        y=[pow(lam,i,p) for i in range(m)]; yi=[pow(t,-1,p) for t in y]
        z=[pow(zeta,i+1,p) for i in range(q)]
        wL,wR,wO=[weights(W,z) for W in (WL,WR,WO)];wc=[weights(W,z) for W in Wc]
        delta=dot(had(yi,wR),wL);bz=dot(z,b)
        sL=rand(m);sR=rand(m)
        lp=[[0]*m for _ in range(d+2)];rp=[[0]*m for _ in range(d+2)]
        lp[half]=add(aL,had(yi,wR));lp[d]=aO;lp[d+1]=sL
        rp[0]=add(wO,scale(-1,y));rp[half]=add(had(y,aR),wL);rp[d+1]=had(y,sR)
        for k in range(1,s+1):
            lp[d-k]=c[k-1];rp[k]=wc[k-1];rp[d-k]=had(y,dc[k-1])
        t=[0]*(2*d+3)
        for i,L in enumerate(lp):
            for j,R in enumerate(rp): t[i+j]=(t[i+j]+dot(L,R))%p
        assert all(ti==0 for ti in t[:half])
        wv = weights(Wv, z)
        assert t[d]==(bz + delta + dot(wv, values)) % p
        counts['coefficient']+=1
        size=2*m+2
        basis=lambda i: [int(j==i) for j in range(size)]
        g=basis(0);h=basis(1);gs=[basis(2+i) for i in range(m)];hs=[basis(2+m+i) for i in range(m)]
        def msm(vals,points):
            return [sum(v*point[j] for v,point in zip(vals,points))%p for j in range(size)]
        # Em coordenadas formais, uma máscara omitida não pode
        # cancelar um erro em g ou nos geradores vectoriais.
        V = [add(scale(v, g), scale(mask, h)) for v, mask in zip(values, masks)]
        Bd = add(scale(bz + delta, g), msm(wv, V))
        mask_d = dot(wv, masks)
        assert Bd == add(scale(t[d], g), scale(mask_d, h))
        if V:
            counts['scalar_commitments'] += 1
        alpha,beta,rho=rand(3);gamma=rand(s)
        AI=add(msm(aL,gs),msm(aR,hs),scale(alpha,h));AO=add(msm(aO,gs),scale(beta,h))
        S=add(msm(sL,gs),msm(sR,hs),scale(rho,h))
        K=[add(msm(c_,gs),msm(d_,hs),scale(mask,h)) for c_,d_,mask in zip(c,dc,gamma)]
        Tindices=[i for i in range(half,2*d+3) if i!=d]
        taus={i:rng.randrange(p) for i in Tindices}
        Ts={i:add(scale(t[i],g),scale(taus[i],h)) for i in Tindices}
        for xi in (1,2,rng.randrange(1,p)):
            powers=[pow(xi,i,p) for i in range(2*d+3)]
            ell=[sum(L[j]*powers[i] for i,L in enumerate(lp))%p for j in range(m)]
            rr=[sum(R[j]*powers[i] for i,R in enumerate(rp))%p for j in range(m)]
            that=dot(ell,rr)
            tau=(sum(taus[i]*powers[i] for i in Tindices) + powers[d]*mask_d) % p
            mu=(alpha*powers[half]+beta*powers[d]+rho*powers[d+1]+sum(gamma[k-1]*powers[d-k] for k in range(1,s+1)))%p
            hp=[scale(yi_,h_) for yi_,h_ in zip(yi,hs)]
            correction=add(wO,scale(-1,y),scale(powers[half],wL),*[scale(powers[k],wc[k-1]) for k in range(1,s+1)])
            P=add(scale(powers[half],AI),scale(powers[d],AO),scale(powers[d+1],S),*[scale(powers[d-k],K[k-1]) for k in range(1,s+1)],scale(powers[half],msm(had(yi,wR),gs)),msm(correction,hp))
            assert P==add(msm(ell,gs),msm(rr,hp),scale(mu,h));counts['public_point']+=1
            public_evaluation = add(scale(powers[d], Bd), *[scale(powers[i],Ts[i]) for i in Tindices])
            assert add(scale(that, g), scale(tau, h)) == public_evaluation
            counts['polynomial_check'] += 1
            omega=rng.randrange(1,p);upi=scale(omega,g)
            assert add(P,scale(-mu,h),scale(that,upi))==add(msm(ell,gs),msm(rr,hp),scale(dot(ell,rr),upi));counts['ipa_statement']+=1
            check_folds(ell, rr, gs, hp, upi, add(P, scale(-mu, h), scale(that, upi)))
    check_squares()
    for zeta in range(1,101):
      for u,v in ((2,10),(3,18),(2,11)):
        td=((u+zeta*zeta)*(u+zeta)+u*u*(zeta**3-1)+u*(-zeta-zeta*zeta+3*zeta**3)-v*zeta**3)%p
        assert td==(zeta**3*(1+u*u+3*u-v))%p
        counts['example']+=1
print(f"{counts['coefficient']} coeficientes reservados, dos quais "
      f"{counts['scalar_commitments']} com compromissos escalares.")
print(f"{counts['public_point']} pontos públicos, {counts['polynomial_check']} avaliações, "
      f"{counts['ipa_statement']} relações de produto interno e {counts['ipa_folds']} dobras.")
print(f"{counts['example']} casos da relação quadrática auxiliar e "
      f"{counts['squares']} do circuito dos dois quadrados em F101 e F65537.")
