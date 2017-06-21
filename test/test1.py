'''
bigmuls = lambda xs, ys: filter(lambda (x, y): x*y > 25, combine(xs, ys))
combine = lambda xs, ys: map(None, xs * len(ys), dupelms(ys, len(xs)))
dupelms = lambda lst, n: reduce(lambda s, t: s + t, map(lambda l, n=n: [l]*n, lst))
print bigmuls([1, 2, 3, 4], [10, 15, 3, 22])
'''

class A(object):
    x = 1
    gen = (lambda x: (x for _ in xrange(10)))(x)

def fun():
    for x in xrange(10):
        print x,

if __name__ == "__main__":
    print(list(A.gen))
    fun()