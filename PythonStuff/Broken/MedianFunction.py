def median(l):
    half = len(l) // 2
    if not len(l) % 2:
        return (l[half - 1] + l[half]) / 2.0
    return l[half]
a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(median(a))
def median2(l):
  if not len(l) % 2:
    print("if route")
    ll = len(l)
    lq = ll/2
    lq = int(lq)
    hq = lq + 1
    hq = int(hq)
    lq = l[lq]
    hq = l[hq]
    q = lq + hq
    q = q / 2
    return q
  else:
    print("else route")
    ll = len(l)
    ll = int(ll)
    ll = ll - 1
    q = ll / 2
    q = q + 1
    q = l[q]
    return q
b = median2(a)
print(b)
print(a)