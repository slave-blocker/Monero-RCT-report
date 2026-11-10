"""Check F5's coefficient counts, dense interpolation, and mask identities."""
from random import Random

rng=Random(52026)
mod=65537

def evaluate(coeffs,x):
    value=0
    for a in reversed(coeffs):value=(value*x+a)%mod
    return value

def lagrange_basis(t):
    # P(X) = product (X-j), coefficients in increasing order.
    P=[1]
    for j in range(t):
        nxt=[0]*(len(P)+1)
        for k,a in enumerate(P):
            nxt[k]=(nxt[k]-j*a)%mod
            nxt[k+1]=(nxt[k+1]+a)%mod
        P=nxt
    basis=[]
    for j in range(t):
        Q=[0]*t;Q[-1]=P[-1]
        for k in range(t-1,0,-1):Q[k-1]=(P[k]+j*Q[k])%mod
        assert (P[0]+j*Q[0])%mod==0
        denominator=evaluate(Q,j)
        inv=pow(denominator,-1,mod)
        basis.append([a*inv%mod for a in Q])
    return basis

def interpolate(values,basis):
    result=[0]*len(values);products=0
    for value,poly in zip(values,basis):
        for i,a in enumerate(poly):
            result[i]=(result[i]+a*value)%mod;products+=1
    return result,products

for length,t,expected in [(253,129,33282),(255,131,34322)]:
    d=length+1
    degree0=d//2;degree1=(d-3)//2
    total=(degree0+1)+(degree1+1)
    assert total==d and total-1==length
    assert 2*length+2=={253:508,255:512}[length]
    assert degree0<t and degree1<t
    basis=lagrange_basis(t)
    for j,poly in enumerate(basis):
        for k in range(t):assert evaluate(poly,k)==int(j==k)
    for _ in range(8):
        count=0
        for degree in [degree0,degree1]:
            coeffs=[rng.randrange(mod) for _ in range(degree+1)]
            values=[evaluate(coeffs,j) for j in range(t)]
            result,products=interpolate(values,basis);count+=products
            assert result==coeffs+[0]*(t-len(coeffs))
        assert count==expected==2*t*t

assert 4*253+5*253+10==2287
assert 2287+6==2293
assert 4*252+2*254==1516
assert 5*7==35 and (5+3-1)*7==49

# A small actual elliptic-curve group checks every sign in the presentations.
def add(P,Q):
    if P is None:return Q
    if Q is None:return P
    x,y=P;u,v=Q
    if x==u and (y+v)%17==0:return None
    slope=((3*x*x+2)*pow(2*y,-1,17) if P==Q
           else (v-y)*pow(u-x,-1,17))%17
    rx=(slope*slope-x-u)%17
    return rx,(slope*(x-rx)-y)%17

def mul(n,P):
    result=None;n%=19
    while n:
        if n&1:result=add(result,P)
        P=add(P,P);n>>=1
    return result

G=(5,1);T=mul(2,G);U=mul(3,G);V=mul(5,G)
for _ in range(200):
    O,J,C=[mul(rng.randrange(1,19),G) for _ in range(3)]
    ro,rj,rr,rc=[rng.randrange(1,19) for _ in range(4)]
    ot,jt,ct=add(O,mul(ro,T)),add(J,mul(rj,U)),add(C,mul(rc,G))
    R=add(mul(rj,V),mul(rr,T))
    do,du,dv,dr,dc=mul(-ro,T),mul(-rj,U),mul(-rj,V),mul(rr,T),mul(-rc,G)
    assert add(ot,do)==O and add(jt,du)==J
    assert add(R,dv)==dr and add(ct,dc)==C

print('253/255 coefficient counts, 508/512 data counts, and aggregate costs checked.')
print('Dense Lagrange bases 129/131 checked at all grid nodes; 16 pairs of polynomials recovered.')
print('Each pair used exactly 33282/34322 field products; 200 mask presentations checked.')
