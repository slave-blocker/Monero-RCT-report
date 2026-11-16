"""Confere as aberturas SAL sob quatro relações conhecidas entre geradores.

Constrói os quatro testes SAL para todos os desafios do grupo pequeno.
Verifica álgebra sob parâmetros deliberadamente relacionados; não executa
uma prova de pertença FCMP++ nem afirma uma exploração da rede real.
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from random import Random
import sys

sys.dont_write_bytecode = True
spec = spec_from_file_location('clsag_math', Path(__file__).with_name('clsag-aggregation.py'))
math = module_from_spec(spec)
spec.loader.exec_module(math)
G, ell, add, mul = math.G, math.ELL, math.add, math.mul
rng = Random(16112026)


def lin(*terms):
    result = None
    for scalar, point in terms:
        result = add(result, mul(scalar, point))
    return result


def proof_checks(G, T, U, V, Ot, Jt, R, P, I, x, y, r, rP, w, eta,
                 shared=None):
    D = lin((1,P),(-1,Ot),(-1,R))
    assert P == lin((x,G),(r,V),(x*r,U),(rP,T))
    assert Ot == lin((x,G),(y,T))
    assert D == lin((w,U),(eta,T))
    assert I == lin((x,Jt),(-w,U))
    alpha,beta,delta,mu,ky,kw,ke = [rng.randrange(ell) for _ in range(7)]
    kappa = rng.randrange(ell)
    if shared == 'x':
        kw = (r*alpha+kappa) % ell
    if shared == 'y':
        ke = (kappa-ky) % ell
    A = lin((alpha,G),(beta,V),(alpha*r+beta*x,U),(delta,T))
    B = lin((alpha*beta,U),(mu,T))
    RO = lin((alpha,G),(ky,T))
    RP = lin((kw,U),(ke,T))
    RI = lin((alpha,Jt),(-kw,U))
    for e in range(ell):
        sx,sJ,sP,sy,sw,se = ((alpha+e*x)%ell, (beta+e*r)%ell,
            (mu+e*delta+e*e*rP)%ell, (ky+e*y)%ell, (kw+e*w)%ell, (ke+e*eta)%ell)
        if shared == 'x':
            assert sw == (r*sx+kappa) % ell
            sw = (r*sx+kappa) % ell
        if shared == 'y':
            assert se == (kappa-sy+e*(eta+y)) % ell
            se = (kappa-sy+e*(eta+y)) % ell
        assert lin((e*e,P),(e,A),(1,B)) == lin((e*sx,G),(e*sJ,V),(sx*sJ,U),(sP,T))
        assert lin((1,RO),(e,Ot)) == lin((sx,G),(sy,T))
        assert lin((1,RP),(e,D)) == lin((sw,U),(se,T))
        assert lin((1,RI),(e,I)) == lin((sx,Jt),(-sw,U))
    return ell


counts = {}
for relation in ('TG','UT','VT','VU'):
    count = attempts = accepted = 0
    while accepted < 80:
        attempts += 1
        q = rng.randrange(1,ell)
        T,U,V,J = [mul(rng.randrange(1,ell),G) for _ in range(4)]
        if relation == 'TG': T = mul(q,G)
        if relation == 'UT': U = mul(q,T)
        if relation == 'VT': V = mul(q,T)
        if relation == 'VU': V = mul(q,U)
        x = rng.randrange(1,ell)
        y,r,rR,rP = [rng.randrange(ell) for _ in range(4)]
        shift = rng.randrange(1,ell)
        Ot = lin((x,G),(y,T))
        Jt = lin((1,J),(r,U))
        R = lin((r,V),(rR,T))
        old_image = mul(x,J)
        xs,ys,rs = x,y,r
        if relation == 'TG':
            xs=(x+shift)%ell
            ys=(y-shift*pow(q,-1,ell))%ell
            w=xs*r%ell
            eta=(rP-ys-rR)%ell
            expected=mul(xs,J)
        elif relation == 'UT':
            w=(x*r+shift)%ell
            eta=(rP-y-rR-q*shift)%ell
            expected=lin((x,J),(-shift,U))
        elif relation == 'VT':
            rs=(r+shift)%ell
            w=x*rs%ell
            eta=(rP-y-rR+q*shift)%ell
            expected=lin((x,J),(-x*shift,U))
        else:
            rs=(r+shift)%ell
            w=(x*rs+q*shift)%ell
            eta=(rP-y-rR)%ell
            expected=lin((x,J),(-(x+q)*shift,U))
        P=lin((xs,G),(rs,V),(xs*rs,U),(rP,T))
        new_image=lin((xs,Jt),(-w,U))
        assert new_image == expected
        if relation == 'VU' and (x+q)%ell == 0:
            assert new_image == old_image
            continue
        assert new_image != old_image
        if new_image is None or xs == 0:
            continue
        count += proof_checks(G,T,U,V,Ot,Jt,R,P,new_image,xs,ys,rs,rP,w,eta)
        accepted += 1
    counts[relation]=count

for _ in range(256):
    secret=rng.randrange(ell)
    shared=[rng.randrange(ell) for _ in range(5)]
    x=(secret+sum(shared))%ell
    J=mul(rng.randrange(1,ell),G)
    image=lin((secret,J),*((part,J) for part in shared))
    assert image == mul(x,J)
    r=rng.randrange(ell)
    assert r*x%ell == (r*secret+sum(r*part for part in shared))%ell
    beta,nu,e = [rng.randrange(ell) for _ in range(3)]
    h=mul(rng.randrange(1,ell),G)
    assert lin((nu,h),(e*beta,h)) == mul(nu+e*beta,h)

print('Testes SAL por relação:', counts)
print('320 imagens alternativas não nulas; 6080 desafios; 256 somas parciais e fechos de raiz.')

# As transformações de respostas têm de conservar todos os testes SAL,
# incluindo o produto quadrático, para qualquer desafio. Os parâmetros do
# grupo pequeno verificam identidades, sem uma hipótese de segurança sobre
# estes geradores nem sobre a coordenação distribuída.
distributed = {}
for shared in ('x', 'y'):
    checked = 0
    for _ in range(80):
        T,U,V,J = [mul(rng.randrange(1,ell),G) for _ in range(4)]
        x,y,r,rR,rP = [rng.randrange(ell) for _ in range(5)]
        w,eta = x*r%ell,(rP-y-rR)%ell
        Ot=lin((x,G),(y,T))
        Jt=lin((1,J),(r,U))
        R=lin((r,V),(rR,T))
        P=lin((x,G),(r,V),(w,U),(rP,T))
        I=mul(x,J)
        checked += proof_checks(G,T,U,V,Ot,Jt,R,P,I,x,y,r,rP,w,eta,shared)
    distributed[shared]=checked
print('Transformações das respostas partilhadas, todos os testes SAL:', distributed)
