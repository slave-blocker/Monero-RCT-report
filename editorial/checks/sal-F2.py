from random import Random
rng=Random(20261110)
q=17
ell=19
zero=None

def add(A,B):
    if A is None: return B
    if B is None: return A
    x,y=A; u,v=B
    if x==u and (y+v)%q==0: return None
    m=((v-y)*pow((u-x)%q,-1,q) if x!=u else (3*x*x+2)*pow(2*y,-1,q))%q
    X=(m*m-x-u)%q
    return X,(m*(x-X)-y)%q

def mul(k,A):
    R=None
    k%=ell
    while k:
        if k&1: R=add(R,A)
        A=add(A,A); k>>=1
    return R

def lin(*terms):
    R=None
    for k,A in terms: R=add(R,mul(k,A))
    return R

G=(5,1);T=mul(2,G);V=mul(3,G);U=mul(4,G)
assert len({mul(i,G) for i in range(ell)})==ell
logsT={mul(i,T):i for i in range(ell)}
sample=lambda:rng.randrange(ell)
counts=dict(completeness=0,extraction=0,simulation=0,message_challenge=0)
for case in range(40):
    x=rng.randrange(1,ell); y=sample(); rO=sample(); rJ=sample(); rR=sample(); rP=sample()
    ybar=(y+rO)%ell; w=x*rJ%ell; eta=(rP-ybar-rR)%ell
    O=lin((x,G),(y,T)); J=mul(rng.randrange(1,ell),G)
    Ot=lin((1,O),(rO,T)); Jt=lin((1,J),(rJ,U)); R=lin((rJ,V),(rR,T)); I=mul(x,J)
    P=lin((x,G),(rJ,V),(w,U),(rP,T)); D=lin((1,P),(-1,Ot),(-1,R))
    assert D==lin((w,U),(eta,T))
    alpha,beta,delta,mu,ky,kw,ke=[sample() for _ in range(7)]
    A=lin((alpha,G),(beta,V),(alpha*rJ+beta*x,U),(delta,T))
    B=lin((alpha*beta,U),(mu,T))
    RO=lin((alpha,G),(ky,T));RP=lin((kw,U),(ke,T));RI=lin((alpha,Jt),(-kw,U))
    def responses(e):
        return tuple(v%ell for v in (alpha+e*x,beta+e*rJ,mu+e*delta+e*e*rP,ky+e*ybar,kw+e*w,ke+e*eta))
    def check(e,A,B,RO,RP,RI,S):
        sx,sJ,sP,sy,sw,se=S
        assert lin((e*e,P),(e,A),(1,B))==lin((e*sx,G),(e*sJ,V),(sx*sJ,U),(sP,T))
        assert lin((1,RO),(e,Ot))==lin((sx,G),(sy,T))
        assert lin((1,RP),(e,D))==lin((sw,U),(se,T))
        assert lin((1,RI),(e,I))==lin((sx,Jt),(-sw,U))
    for e in range(ell):
        S=responses(e); check(e,A,B,RO,RP,RI,S); counts['completeness']+=1
        e2=(e+1)%ell; S2=responses(e2)
        inv=pow((e-e2)%ell,-1,ell)
        ext=tuple((S[i]-S2[i])*inv%ell for i in (0,3,4,5))
        assert ext==(x,ybar,w,eta); counts['extraction']+=1
        assert lin((1,RI),(e2,I))!=lin((S[0],Jt),(-S[4],U)); counts['message_challenge']+=1
        simA=mul(sample(),G); simS=tuple(sample() for _ in range(6))
        sx,sJ,sP,sy,sw,se=simS
        simB=lin((e*sx,G),(e*sJ,V),(sx*sJ,U),(sP,T),(-e*e,P),(-e,simA))
        simRO=lin((sx,G),(sy,T),(-e,Ot));simRP=lin((sw,U),(se,T),(-e,D));simRI=lin((sx,Jt),(-sw,U),(-e,I))
        check(e,simA,simB,simRO,simRP,simRI,simS)
        aa=(sx-e*x)%ell;bb=(sJ-e*rJ)%ell
        dd=logsT[lin((1,simA),(-aa,G),(-bb,V),(-(aa*rJ+bb*x),U))]
        mm=(sP-e*dd-e*e*rP)%ell
        kky=(sy-e*ybar)%ell;kkw=(sw-e*w)%ell;kke=(se-e*eta)%ell
        assert simB==lin((aa*bb,U),(mm,T))
        assert simRO==lin((aa,G),(kky,T))
        assert simRP==lin((kkw,U),(kke,T))
        assert simRI==lin((aa,Jt),(-kkw,U))
        counts['simulation']+=1
print(counts)
print('Algebra checks in the order-19 curve subgroup over F17; no cryptographic security claim from these finite checks.')
