"""Finite-field checks of the arithmetic relations explained in F6."""
from itertools import product
from random import Random

p=17
points=[(x,y) for x in range(p) for y in range(p) if (y*y-x*x*x-2*x-2)%p==0]
assert len(points)==18
accepted=0;same_result_x=0
for x0,y0 in points:
    for x1,y1 in points:
        dx=(x1-x0)%p
        if not dx:
            assert all(i*dx%p!=1 for i in range(p))
            continue
        inverse=pow(dx,-1,p);slope=(y1-y0)*inverse%p
        result=((slope*slope-x0-x1)%p,0)
        result=(result[0],(slope*(x0-result[0])-y0)%p)
        matches=[]
        for x2,y2 in points:
            valid=(inverse*dx%p==1 and slope*dx%p==(y1-y0)%p
                   and slope*(x2-x0)%p==(-y2-y0)%p
                   and slope*slope%p==(x0+x1+x2)%p)
            if valid:matches.append((x2,y2))
        assert matches==[result]
        accepted+=1;same_result_x+=result[0]==x0
assert accepted==288 and same_result_x==18

rng=Random(62026)
for width in range(1,39):
    for _ in range(20):
        values=[rng.randrange(p) for _ in range(width)]
        for choice in range(p):
            carried=(values[0]-choice)%p
            for value in values[1:]:carried=carried*(value-choice)%p
            assert (carried==0)==(choice in values)

tuples=[(5,1,6,3,10,6),(3,1,9,16,16,13),(0,6,13,7,7,6)]
weights=range(1,7)
compressed=[sum(a*b for a,b in zip(t,weights))%17 for t in tuples]
assert compressed==[4,16,14]
for t in tuples:
    assert all(tuple(t[k:k+2]) in points for k in [0,2,4])
assert [(v-14)%17 for v in compressed]==[7,2,0]

# Exhaust all six nonzero weights in F_7, with data fixed before weights.
q=7;claimed=(1,1,1,1,1,1)
diffs=[[(a-b)%q for a,b in zip(t,claimed)] for t in tuples]
assert all(any(d) for d in diffs)
counts=[0,0,0];union=0;trials=0
for chi in product(range(1,q),repeat=6):
    events=[sum(a*b for a,b in zip(chi,d))%q==0 for d in diffs]
    counts=[a+int(b) for a,b in zip(counts,events)]
    union+=any(events);trials+=1
assert all(c*(q-1)<=trials for c in counts)
assert union*(q-1)<=len(tuples)*trials

def pow2(v):return 1<<(v-1).bit_length()
for depth in range(1,33):
    for n in range(1,65):
        ns=n*sum(97 if level==1 else 52 for level in range(1,depth+1,2))
        nh=n*sum(32 for level in range(2,depth+1,2))
        assert ns==n*(97+52*((depth-1)//2))
        assert nh==32*n*(depth//2)
        ms,mh=pow2(max(256,ns)),pow2(max(128,n,nh))
        assert ms>=ns and mh>=nh
        assert mh==max(128,pow2(n*max(32*(depth//2),1)))
assert (pow2(max(256,149)),pow2(max(128,1,32)))==(256,128)
assert (pow2(max(256,298)),pow2(max(128,2,64)))==(512,128)
assert 5*7+3*3+4*4+37==97
assert 1+7+3+4+37==52 and 1+7+3+4+17==32
print('288 affine sums uniquely verified; 18 valid cases have result abscissa equal to the public point.')
print('12920 scalar-membership cases; sextuple example and 46656 nonzero challenge vectors checked.')
print('Collision counts:',counts,'union:',union,'of',trials)
print('2048 layer/input configurations and IPA dimensions checked.')
