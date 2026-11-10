"""Exact arithmetic checks for F4; security assumptions are not tested here."""
from math import isqrt
from random import Random

p = 2**255 - 19
q = 2**255 - 11686397589588510723982429389243424941
ell = 2**252 + 27742317777372353535851937790883648493
bH = 17523451383230374900436292617863907649717438939964238673872692863501483215968
bS = 25675911719867737339625140396204798989996478324626569376465022644547366285284
kappa = 51042569399160536130206135233146329284152202253034631822681833788666877215207
A = 486662
aW = (1 - A*A*pow(3, -1, p)) % p
bW = (2*A**3*pow(27, -1, p) - A*pow(3, -1, p)) % p
assert aW == int('2aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa984914a144', 16)
assert bW == int('7b425ed097b425ed097b425ed097b425ed097b425ed097b4260b5e9c7710c864', 16)
assert kappa*kappa % p == (-486664) % p
assert bW != 0
d = -121665*pow(121666, -1, p) % p
sqrt_minus_one = pow(2, (p-1)//4, p)

def sqrt(n):
    n %= p
    r = pow(n, (p+3)//8, p)
    if r*r % p != n:
        r = r*sqrt_minus_one % p
    return r if r*r % p == n else None

def eadd(P, Q):
    x,y = P; u,v = Q
    t = d*x*u*y*v % p
    return ((x*v+y*u)*pow(1+t, -1, p) % p,
            (y*v+x*u)*pow(1-t, -1, p) % p)

def mul(n, P, add, identity):
    R = identity
    while n:
        if n & 1: R = add(R, P)
        P = add(P, P)
        n >>= 1
    return R

def wadd(P,Q,mod,a):
    if P is None: return Q
    if Q is None: return P
    x,y = P; u,v = Q
    if x == u and (y+v) % mod == 0: return None
    m = ((3*x*x+a)*pow(2*y, -1, mod) if P==Q
         else (v-y)*pow(u-x, -1, mod)) % mod
    rx = (m*m-x-u) % mod
    return (rx, (m*(x-rx)-y) % mod)

def wei(P):
    if P == (0,1): return None
    x,y = P
    assert x != 0 and y != 1
    assert (-x*x+y*y-1-d*x*x*y*y) % p == 0
    u = (1+y)*pow(1-y, -1, p) % p
    v = kappa*u*pow(x, -1, p) % p
    assert v*v % p == (u**3+A*u*u+u) % p
    X,Y = (u+A*pow(3,-1,p))%p,v
    assert Y*Y % p == (X**3+aW*X+bW) % p
    return X,Y

y = 4*pow(5,-1,p) % p
x = sqrt((y*y-1)*pow(d*y*y+1,-1,p))
if x%2: x=p-x
G = x,y
assert mul(ell,G,eadd,(0,1)) == (0,1)
assert (wei(G)[0]-A*pow(3,-1,p))%p == 9

# Obtain an order-eight torsion point by halving a point of order four.
T = None
for z in [sqrt(1+d), -sqrt(1+d)]:
    t = (-1+z)*pow(d,-1,p)%p
    xx,yy = sqrt(-t),sqrt(t)
    if xx is not None and yy is not None:
        candidate = xx,yy
        if mul(8,candidate,eadd,(0,1)) == (0,1) and mul(4,candidate,eadd,(0,1)) != (0,1):
            T = candidate
            break
assert T is not None

rng=Random(4102026)
projection_count=0
for n in list(range(1,9))+[rng.randrange(1,ell) for _ in range(16)]:
    P=mul(n,G,eadd,(0,1))
    W=wei(P)
    assert W == mul(n,wei(G),lambda R,S:wadd(R,S,p,aW),None)
    other=mul(rng.randrange(1,ell),G,eadd,(0,1))
    assert wei(eadd(P,other)) == wadd(W,wei(other),p,aW)
    for j in range(8):
        with_torsion=eadd(P,mul(j,T,eadd,(0,1)))
        projected=mul(8*pow(8,-1,ell),with_torsion,eadd,(0,1))
        assert projected==P
        projection_count+=1

curves=[(p,q,bH,43927350165885181914572701368652294970994947138804342515295004363921039321018),
        (q,p,bS,25798700515841442074436724357845010259191889815205036617843407906692357567936)]
for mod,order,b,gy in curves:
    assert gy*gy%mod == (1-3+b)%mod
    assert (4*(-3)**3+27*b*b)%mod != 0
    assert pow(b,(mod-1)//2,mod)==mod-1
    add=lambda R,S:wadd(R,S,mod,-3)
    assert mul(order,(1,gy),add,None) is None
    bound=isqrt(4*mod)
    low,high=mod+1-bound,mod+1+bound
    assert (low+order-1)//order == high//order == 1

layers=[]; size=700; depth=0
while size>1:
    width=38 if depth%2==0 else 18
    size=(size+width-1)//width
    layers.append(size);depth+=1
assert layers==[19,2,1]
index=699; path=[]
for width in [38,18,38]:
    index,pos=divmod(index,width);path.append((index,pos))
assert path==[(18,15),(1,0),(0,1)]

# Root proof equation checked in a genuine elliptic-curve group.
add=lambda P,Q:wadd(P,Q,17,2)
g=(5,1); order=19
for _ in range(200):
    base,root,beta,nonce,challenge=[rng.randrange(order) for _ in range(5)]
    B=mul(base,g,add,None); R=mul(root,g,add,None)
    K=mul((root-base+beta)%order,g,add,None)
    delta=add(add(B,K),mul((-root)%order,g,add,None))
    msg=mul(nonce,g,add,None)
    assert add(msg,mul(challenge,delta,add,None)) == mul((nonce+challenge*beta)%order,g,add,None)

print('Constants and two cycle groups checked (prime moduli assumed from primary source).')
print('24 Wei maps/scalar multiplications and 24 sums checked; 192 torsion projections checked.')
print('700-output tree/path and 200 root Schnorr identities checked.')
