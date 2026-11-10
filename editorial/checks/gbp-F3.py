from random import Random
rng=Random(20261111)
counts=dict(coefficient=0,public_point=0,polynomial_check=0,ipa_statement=0,example=0)
for p in (101,65537):
    def add(*vs): return [sum(xs)%p for xs in zip(*vs)]
    def scale(a,v): return [(a*x)%p for x in v]
    def dot(a,b): return sum(x*y for x,y in zip(a,b))%p
    def had(a,b): return [x*y%p for x,y in zip(a,b)]
    def mat(W,v): return [dot(row,v) for row in W]
    def weights(W,z): return [sum(z[j]*W[j][i] for j in range(len(W)))%p for i in range(len(W[0]))]
    def rand(n): return [rng.randrange(p) for _ in range(n)]
    for m in (2,4,8):
      for s in range(5):
       for rep in range(8):
        q=4;d=2*s+2;half=s+1
        aL=rand(m);aR=rand(m);aO=had(aL,aR)
        c=[rand(m) for _ in range(s)];dc=[rand(m) for _ in range(s)]
        WL,WR,WO=[[rand(m) for _ in range(q)] for _ in range(3)]
        Wc=[[rand(m) for _ in range(q)] for _ in range(s)]
        b=add(mat(WL,aL),mat(WR,aR),mat(WO,aO),*[mat(W,c_) for W,c_ in zip(Wc,c)])
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
        assert t[d]==(bz+delta)%p
        counts['coefficient']+=1
        size=2*m+2
        basis=lambda i: [int(j==i) for j in range(size)]
        g=basis(0);h=basis(1);gs=[basis(2+i) for i in range(m)];hs=[basis(2+m+i) for i in range(m)]
        def msm(vals,points):
            return [sum(v*point[j] for v,point in zip(vals,points))%p for j in range(size)]
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
            that=dot(ell,rr);tau=sum(taus[i]*powers[i] for i in Tindices)%p
            mu=(alpha*powers[half]+beta*powers[d]+rho*powers[d+1]+sum(gamma[k-1]*powers[d-k] for k in range(1,s+1)))%p
            hp=[scale(yi_,h_) for yi_,h_ in zip(yi,hs)]
            correction=add(wO,scale(-1,y),scale(powers[half],wL),*[scale(powers[k],wc[k-1]) for k in range(1,s+1)])
            P=add(scale(powers[half],AI),scale(powers[d],AO),scale(powers[d+1],S),*[scale(powers[d-k],K[k-1]) for k in range(1,s+1)],scale(powers[half],msm(had(yi,wR),gs)),msm(correction,hp))
            assert P==add(msm(ell,gs),msm(rr,hp),scale(mu,h));counts['public_point']+=1
            assert add(scale(that,g),scale(tau,h))==add(scale(powers[d]*(bz+delta),g),*[scale(powers[i],Ts[i]) for i in Tindices]);counts['polynomial_check']+=1
            omega=rng.randrange(1,p);upi=scale(omega,g)
            assert add(P,scale(-mu,h),scale(that,upi))==add(msm(ell,gs),msm(rr,hp),scale(dot(ell,rr),upi));counts['ipa_statement']+=1
    for zeta in range(1,101):
      for u,v in ((2,10),(3,18),(2,11)):
        td=((u+zeta*zeta)*(u+zeta)+u*u*(zeta**3-1)+u*(-zeta-zeta*zeta+3*zeta**3)-v*zeta**3)%p
        assert td==(zeta**3*(1+u*u+3*u-v))%p
        counts['example']+=1
print(counts)
print('Coefficientwise algebra over F101 and F65537; arbitrary right-hand VC coordinates included. These finite checks do not replace security proofs.')
