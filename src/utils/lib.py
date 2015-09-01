from __future__ import division, print_function
import random

"""
Default class which everything extends.
"""
class O():
  def __init__(i,**d): i.has().update(**d)
  def has(i): return i.__dict__
  def update(i,**d): i.has().update(d); return i
  def __repr__(i)   :
    show=[':%s %s' % (k,i.has()[k])
      for k in sorted(i.has().keys() )
      if k[0] is not "#"]
    txt = ' '.join(show)
    if len(txt) > 60:
      show=map(lambda x: '\t'+x+'\n',show)
    return '{'+' '.join(show)+'}'
  def __getitem__(i, item):
    return i.has().get(item)

"""
An accumulator for reporting on numbers.
"""
class N():
  "Add/delete counts of numbers."
  def __init__(i,inits=[]):
    i.zero()
    map(i.__iadd__,inits)
  def zero(i):
    i.n = i.mu = i.m2 = 0
    i.cache= Cache()
  def sd(i)  :
    if i.n < 2:
      return 0
    else:
      return (max(0,i.m2)/(i.n - 1))**0.5
  def __iadd__(i,x):
    i.cache += x
    i.n     += 1
    delta    = x - i.mu
    i.mu    += delta/(1.0*i.n)
    i.m2    += delta*(x - i.mu)
    return i
  def __isub__(i,x):
    i.cache = Cache()
    if i.n < 2: return i.zero()
    i.n  -= 1
    delta = x - i.mu
    i.mu -= delta/(1.0*i.n)
    i.m2 -= delta*(x - i.mu)
    return i

CACHE_SIZE=128
class Cache:
  "Keep a random sample of stuff seen so far."
  def __init__(i, inits=[]):
    i.all,i.n,i._has = [],0,None
    map(i.__iadd__,inits)
  def __iadd__(i,x):
    i.n += 1
    if len(i.all) < CACHE_SIZE: # if not full
      i._has = None
      i.all += [x]               # then add
    else: # otherwise, maybe replace an old item
      if random.random() <= CACHE_SIZE/i.n:
        i._has=None
        i.all[int(random.random()*CACHE_SIZE)] = x
    return i
  def has(i):
    if i._has == None:
      lst  = sorted(i.all)
      med,iqr = medianIQR(lst,ordered=True)
      i._has = O(
        median = med,      iqr = iqr,
        lo     = i.all[0], hi  = i.all[-1])
    return i._has

def medianIQR(lst, ordered=False):
  if not ordered:
    lst = sorted(lst)
  n = len(lst)
  q = n//4
  iqr = lst[q*3] - lst[q]
  if n % 2:
    return lst[q*2],iqr
  else:
    p = max(0,q-1)
    return (lst[p] + lst[q]) * 0.5,iqr