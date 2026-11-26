"""Finite sanity checks; these are not a substitute for written proofs."""
from itertools import combinations, product
from math import comb
import unittest


def moment_counts(p, A):
    A = tuple(A)
    r = {}
    for m in range(p):
        for K in range(p):
            r[m, K] = sum(((a - m)*(b - m) - K) % p == 0
                          for a, b in product(A, repeat=2))
    return r


def additive_energy(p, A):
    return sum((a+b-c-d) % p == 0 for a,b,c,d in product(A, repeat=4))


def line_occupancies(p, A):
    S = {( (a+b) % p, (a*b) % p) for a,b in product(A, repeat=2)}
    lines = [sum((v - m*u - b) % p == 0 for u,v in S)
             for m,b in product(range(p), repeat=2)]
    lines += [sum(u == c for u,v in S) for c in range(p)]
    return S, lines


def corrected_occupancies(p, A):
    r = moment_counts(p,A)
    result = []
    for m,K in product(range(p), repeat=2):
        d = sum(((a-m)*(a-m) - K) % p == 0 for a in A)
        assert (r[m,K] + d) % 2 == 0
        result.append((r[m,K]+d)//2)
    for c in range(p):
        s = sum((a+b-c)%p == 0 for a,b in product(A,repeat=2))
        h = sum((2*a-c)%p == 0 for a in A)
        assert (s+h)%2 == 0
        result.append((s+h)//2)
    return result


class TestProjectedSegre(unittest.TestCase):
    def test_exhaustive_small_fields(self):
        for p in (2, 3, 5, 7):
            for mask in range(1 << p):
                A = [i for i in range(p) if mask & (1 << i)]
                n = len(A)
                S, actual = line_occupancies(p, A)
                self.assertEqual(len(S), n * (n + 1) // 2)
                r = moment_counts(p,A)
                self.assertEqual(sum(v*v for v in r.values()),
                                 n**4 - additive_energy(p,A) + p*(2*n*n-n))
                self.assertEqual(sum(r.values()), p*n*n)
                self.assertEqual(sorted(actual), sorted(corrected_occupancies(p,A)))
                t1 = sum(comb(k,3) for k in actual if k >= 3)
                t2 = sum(comb(k,3) for k in corrected_occupancies(p,A) if k >= 3)
                self.assertEqual(t1,t2)
                pts = list(S)
                t3 = sum(( (b[0]-a[0])*(c[1]-a[1]) -
                           (b[1]-a[1])*(c[0]-a[0]) ) % p == 0
                          for a,b,c in combinations(pts,3))
                self.assertEqual(t1,t3)

    def test_singleton_disproves_unqualified_third_moment(self):
        for p in (3, 5, 7, 11, 101):
            r = moment_counts(p, {2 % p})
            self.assertEqual(sum(x**3 for x in r.values()), p)

    def test_reducible_hyperbola(self):
        for p in (3,5,7):
            for m in range(p):
                for x,y in product(range(p), repeat=2):
                    self.assertEqual((x-m)*(y-m) % p == 0,
                                     x == m or y == m)


if __name__ == '__main__':
    unittest.main()
