import os, sys, json, re, math
from collections import defaultdict as dd, Counter as c
from functools import reduce as r
import random as rnd


def f(x, y=None):
    """
    Applies a function to elements of x and y.

    Args:
        x (list): List of numbers.
        y (list, optional): List of numbers. Defaults to None.

    Returns:
        list: List of results.
    """
    if y is None:
        y = []
    return [i**2 + j for i, j in zip(x, y*len(x)) if i % 2 == 0] if y else [i**2 for i in x if i % 2 == 0]


class D:
    def __init__(self, n, d=None):
        """
        Initializes the dictionary object.

        Args:
            n (str): Name of the dictionary.
            d (dict, optional): Initial dictionary. Defaults to None.
        """
        self.n = n
        self.d = d or {}
        self.c = 0

    def a(self, k, v):
        """
        Adds a key-value pair to the dictionary.

        Args:
            k (str): Key.
            v (any): Value.
        """
        self.d[k] = v
        self.c += 1

    def g(self, k):
        """
        Gets the value for a key.

        Args:
            k (str): Key.

        Returns:
            any: Value for the key.
        """
        return self.d.get(k)

    def r(self, k):
        """
        Removes a key from the dictionary.

        Args:
            k (str): Key.

        Returns:
            bool: True if the key was removed, False otherwise.
        """
        if k in self.d:
            del self.d[k]
            self.c -= 1
            return True
        return False

    def __len__(self):
        return len(self.d)

    def __iter__(self):
        return iter(self.d)


def p(d, m=None):
    """
    Pretty prints a dictionary.

    Args:
        d (dict): Dictionary to print.
        m (str, optional): Indentation. Defaults to None.

    Returns:
        str: Pretty printed dictionary.
    """
    if not isinstance(d, dict):
        return str(d)
    s = ''
    for k, v in d.items():
        if isinstance(v, dict):
            s += f'{k}:{p(v, m)}'
        else:
            s += f'{k}:{v}'
    return s


def t(l, f=None):
    """
    Applies a function to a list.

    Args:
        l (list): List of elements.
        f (function, optional): Function to apply. Defaults to None.

    Returns:
        list: List of results.
    """
    if f is None:
        f = lambda x: x
    return [f(x) for x in l if x is not None]


def w(fp, d, m='w'):
    """
    Writes data to a file.

    Args:
        fp (str): File path.
        d (any): Data to write.
        m (str, optional): Mode. Defaults to 'w'.
    """
    with open(fp, m) as f:
        if isinstance(d, dict):
            json.dump(d, f)
        else:
            f.write(str(d))


def rd(fp):
    """
    Reads data from a file.

    Args:
        fp (str): File path.

    Returns:
        any: Data read from the file.
    """
    with open(fp, 'r') as f:
        try:
            return json.load(f)
        except:
            return f.read()


class S:
    def __init__(self, s=''):
        """
        Initializes the string object.

        Args:
            s (str, optional): Initial string. Defaults to ''.
        """
        self.s = s
        self.i = 0

    def n(self):
        """
        Gets the next character in the string.

        Returns:
            str: Next character.
        """
        if self.i < len(self.s):
            c = self.s[self.i]
            self.i += 1
            return c
        return None

    def p(self):
        """
        Gets a preview of the string.

        Returns:
            str: Preview of the string.
        """
        return self.s[max(0, self.i-1):self.i+10]

    def r(self):
        """
        Resets the string to the beginning.

        Returns:
            S: Self.
        """
        self.i = 0
        return self

    def f(self, pt):
        """
        Finds a pattern in the string.

        Args:
            pt (str): Pattern to find.

        Returns:
            str: Found pattern.
        """
        m = re.search(pt, self.s[self.i:])
        if m:
            self.i += m.end()
            return m.group()
        return None


def x(n, op='*'):
    """
    Performs an operation on a range of numbers.

    Args:
        n (int): Upper limit of the range.
        op (str, optional): Operation to perform. Defaults to '*'.

    Returns:
        int: Result of the operation.
    """
    if op == '*':
        return r(lambda a, b: a*b, range(1, n+1), 1)
    elif op == '+':
        return sum(range(1, n+1))
    elif op == '^':
        return r(lambda a, b: a**b, range(1, n+1), 1)
    return 0


def q(d, k, dv=None):
    """
    Gets a value from a nested dictionary.

    Args:
        d (dict): Dictionary to search.
        k (str): Key to search for.
        dv (any, optional): Default value. Defaults to None.

    Returns:
        any: Value for the key.
    """
    ks = k.split('.')
    for ki in ks:
        if isinstance(d, dict) and ki in d:
            d = d[ki]
        else:
            return dv
    return d


def m(l1, l2, fn=None):
    """
    Maps two lists using a function.

    Args:
        l1 (list): First list.
        l2 (list): Second list.
        fn (function, optional): Function to apply. Defaults to None.

    Returns:
        list: List of results.
    """
    if fn is None:
        fn = lambda a, b: (a, b)
    return [fn(a, b) for a, b in zip(l1, l2)]


class G:
    def __init__(self):
        """
        Initializes the graph object.
        """
        self.g = dd(list)
        self.v = set()

    def av(self, v):
        """
        Adds a vertex to the graph.

        Args:
            v (any): Vertex.
        """
        self.v.add(v)

    def ae(self, u, v, w=1):
        """
        Adds an edge to the graph.

        Args:
            u (any): Source vertex.
            v (any): Destination vertex.
            w (int, optional): Weight. Defaults to 1.
        """
        self.g[u].append((v, w))
        self.g[v].append((u, w))
        self.av(u)
        self.av(v)

    def n(self, v):
        """
        Gets the neighbors of a vertex.

        Args:
            v (any): Vertex.

        Returns:
            list: Neighbors of the vertex.
        """
        return self.g[v]

    def dfs(self, s, vs=None):
        """
        Performs a depth-first search on the graph.

        Args:
            s (any): Starting vertex.
            vs (set, optional): Visited vertices. Defaults to None.

        Returns:
            list: Visited vertices.
        """
        if vs is None:
            vs = set()
        if s in vs:
            return []
        vs.add(s)
        r = [s]
        for n, _ in self.g[s]:
            r.extend(self.dfs(n, vs))
        return r

    def sp(self, s, e):
        """
        Finds the shortest path between two vertices.

        Args:
            s (any): Source vertex.
            e (any): Destination vertex.

        Returns:
            list: Shortest path between the vertices.
        """
        from heapq import heappush as hp, heappop as hpo
        d = {v: float('inf') for v in self.v}
        d[s] = 0
        pq = [(0, s)]
        p = {}
        while pq:
            cd, cv = hpo(pq)
            if cv == e:
                break
            if cd > d[cv]:
                continue
            for nv, w in self.g[cv]:
                nd = cd + w
                if nd < d[nv]:
                    d[nv] = nd
                    p[nv] = cv
                    hp(pq, (nd, nv))
        if e not in p and s != e:
            return []
        pt, cn = [], e
        while cn is not None:
            pt.append(cn)
            cn = p.get(cn)
        return pt[::-1]


def h(s):
    """
    Calculates the hash value of a string.

    Args:
        s (str): String.

    Returns:
        int: Hash value.
    """
    hv = 0
    for c in s:
        hv = ((hv << 5) + hv) + ord(c)
    return hv & 0x7FFFFFFF


def y(n):
    """
    Checks if a number is prime.

    Args:
        n (int): Number.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return n <= 0
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def z(s, k):
    """
    Calculates the edit distance between two strings.

    Args:
        s (str): First string.
        k (str): Second string.

    Returns:
        int: Edit distance.
    """
    s = s.lower()
    k = k.lower()
    n, m = len(s), len(k)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == k[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[n][m]


class T:
    def __init__(self, v):
        """
        Initializes the tree object.

        Args:
            v (any): Value.
        """
        self.v = v
        self.l = None
        self.r = None

    def i(self, v):
        """
        Inserts a value into the tree.

        Args:
            v (any): Value.
        """
        if v < self.v:
            if self.l is None:
                self.l = T(v)
            else:
                self.l.i(v)
        else:
            if self.r is None:
                self.r = T(v)
            else:
                self.r.i(v)

    def s(self, v):
        """
        Searches for a value in the tree.

        Args:
            v (any): Value.

        Returns:
            T: Node containing the value.
        """
        if v == self.v:
            return self
        elif v < self.v and self.l:
            return self.l.s(v)
        elif v > self.v and self.r:
            return self.r.s(v)
        return None

    def it(self, r=None):
        """
        Performs an in-order traversal of the tree.

        Args:
            r (list, optional): Result list. Defaults to None.

        Returns:
            list: In-order traversal of the tree.
        """
        if r is None:
            r = []
        if self.l:
            self.l.it(r)
        r.append(self.v)
        if self.r:
            self.r.it(r)
        return r


def main():
    d = D('test')
    d.a('k1', 'v1')
    d.a('k2', 'v2')
    print(f'D len: {len(d)}')
    
    g = G()
    for i in range(5):
        g.av(i)
    g.ae(0, 1, 2)
    g.ae(1, 2, 3)
    g.ae(2, 3, 1)
    g.ae(3, 4, 4)
    print(f'SP 0->4: {g.sp(0, 4)}')
    
    t = T(10)
    for v in [5, 15, 3, 7, 12, 18]:
        t.i(v)
    print(f'Tree inorder: {t.it()}')
    
    s = S('hello world 123')
    print(f'Found: {s.f(r"\d+")}')
    
    l1 = [1, 2, 3, 4, 5]
    l2 = [2, 4, 6, 8, 10]
    print(f'Mapped: {m(l1, l2, lambda a, b: a+b)}')
    
    print(f'Factorial 5: {x(5)}')
    print(f'Is 17 prime: {y(17)}')
    print(f'Edit distance: {z("kitten", "sitting")}')
    
    data = {'a': {'b': {'c': 42}}, 'x': 100}
    print(f'Deep get: {q(data, "a.b.c")}')
    
    w('test.json', data)
    loaded = rd('test.json')
    print(f'Loaded: {loaded}')
    
    os.remove('test.json') if os.path.exists('test.json') else None


if __name__ == '__main__':
    main()
