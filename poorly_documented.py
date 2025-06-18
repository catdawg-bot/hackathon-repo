import os, sys, json, re, math
from collections import defaultdict as dd, Counter as c
from functools import reduce as r
import random as rnd


def f(x, y=None):
    """
    Performs a specific operation on the elements of list x and optionally y.

    Args:
        x (list): List of numbers to operate on.
        y (list, optional): Optional list of numbers to operate on.
            Defaults to None.

    Returns:
        list: A list of results based on the operation performed.
    """
    if y is None:
        y = []
    return [i**2 + j for i, j in zip(x, y*len(x)) if i % 2 == 0] if y else [i**2 for i in x if i % 2 == 0]


class D:
    def __init__(self, n, d=None):
        """
        Initializes a new instance of the D class.

        Args:
            n (str): Name of the instance.
            d (dict, optional): Initial dictionary to use.
                Defaults to None.
        """
        self.n = n
        self.d = d or {}
        self.c = 0

    def a(self, k, v):
        """
        Adds a key-value pair to the dictionary.

        Args:
            k (str): Key to add.
            v (any): Value to add.
        """
        self.d[k] = v
        self.c += 1

    def g(self, k):
        """
        Gets the value associated with a key.

        Args:
            k (str): Key to get the value for.

        Returns:
            any: The value associated with the key, or None if the key is not found.
        """
        return self.d.get(k)

    def r(self, k):
        """
        Removes a key-value pair from the dictionary.

        Args:
            k (str): Key to remove.

        Returns:
            bool: True if the key was found and removed, False otherwise.
        """
        if k in self.d:
            del self.d[k]
            self.c -= 1
            return True
        return False

    def __len__(self):
        """
        Gets the number of key-value pairs in the dictionary.

        Returns:
            int: The number of key-value pairs in the dictionary.
        """
        return len(self.d)

    def __iter__(self):
        """
        Returns an iterator over the keys in the dictionary.

        Returns:
            iterator: An iterator over the keys in the dictionary.
        """
        return iter(self.d)


def p(d, m=None):
    """
    Recursively prints a dictionary or other object.

    Args:
        d (dict or any): The object to print.
        m (str, optional): The mode to use when printing.
            Defaults to None.

    Returns:
        str: A string representation of the object.
    """
    if not isinstance(d, dict):
        return str(d)
    s = ''
    for k, v in d.items():
        if isinstance(v, dict):
            s += f'{k}:{p(v, m)}\n'
        else:
            s += f'{k}:{v}\n'
    return s


def t(l, f=None):
    """
    Applies a function to each element in a list and filters out None values.

    Args:
        l (list): The list to operate on.
        f (function, optional): The function to apply to each element.
            Defaults to None.

    Returns:
        list: A list of the results of applying the function to each element.
    """
    if f is None:
        f = lambda x: x
    return [f(x) for x in l if x is not None]


def w(fp, d, m='w'):
    """
    Writes data to a file.

    Args:
        fp (str): The file path to write to.
        d (dict or any): The data to write.
        m (str, optional): The mode to use when writing.
            Defaults to 'w'.
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
        fp (str): The file path to read from.

    Returns:
        dict or str: The data read from the file.
    """
    with open(fp, 'r') as f:
        try:
            return json.load(f)
        except:
            return f.read()


class S:
    def __init__(self, s=''):
        """
        Initializes a new instance of the S class.

        Args:
            s (str, optional): The initial string to use.
                Defaults to ''.
        """
        self.s = s
        self.i = 0

    def n(self):
        """
        Gets the next character in the string.

        Returns:
            str: The next character in the string, or None if there are no more characters.
        """
        if self.i < len(self.s):
            c = self.s[self.i]
            self.i += 1
            return c
        return None

    def p(self):
        """
        Gets a substring of the string.

        Returns:
            str: A substring of the string.
        """
        return self.s[max(0, self.i-1):self.i+10]

    def r(self):
        """
        Resets the string.

        Returns:
            S: The current instance.
        """
        self.i = 0
        return self

    def f(self, pt):
        """
        Finds a pattern in the string.

        Args:
            pt (str): The pattern to find.

        Returns:
            str: The matched pattern, or None if no match is found.
        """
        m = re.search(pt, self.s[self.i:])
        if m:
            self.i += m.end()
            return m.group()
        return None


def x(n, op='*'):
    """
    Performs a specific operation on a range of numbers.

    Args:
        n (int): The upper bound of the range.
        op (str, optional): The operation to perform.
            Defaults to '*'.

    Returns:
        int: The result of the operation.
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
    Recursively gets a value from a dictionary using a dot-separated key.

    Args:
        d (dict): The dictionary to get the value from.
        k (str): The dot-separated key to use.
        dv (any, optional): The default value to return if the key is not found.
            Defaults to None.

    Returns:
        any: The value associated with the key, or the default value if the key is not found.
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
        l1 (list): The first list to map.
        l2 (list): The second list to map.
        fn (function, optional): The function to use when mapping.
            Defaults to None.

    Returns:
        list: A list of the results of mapping the two lists.
    """
    if fn is None:
        fn = lambda a, b: (a, b)
    return [fn(a, b) for a, b in zip(l1, l2)]


class G:
    def __init__(self):
        """
        Initializes a new instance of the G class.
        """
        self.g = dd(list)
        self.v = set()

    def av(self, v):
        """
        Adds a vertex to the graph.

        Args:
            v (any): The vertex to add.
        """
        self.v.add(v)

    def ae(self, u, v, w=1):
        """
        Adds an edge to the graph.

        Args:
            u (any): The first vertex of the edge.
            v (any): The second vertex of the edge.
            w (int, optional): The weight of the edge.
                Defaults to 1.
        """
        self.g[u].append((v, w))
        self.g[v].append((u, w))
        self.av(u)
        self.av(v)

    def n(self, v):
        """
        Gets the neighbors of a vertex.

        Args:
            v (any): The vertex to get the neighbors of.

        Returns:
            list: A list of the neighbors of the vertex.
        """
        return self.g[v]

    def dfs(self, s, vs=None):
        """
        Performs a depth-first search on the graph.

        Args:
            s (any): The starting vertex.
            vs (set, optional): The set of visited vertices.
                Defaults to None.

        Returns:
            list: A list of the vertices in the order they were visited.
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
        Finds the shortest path between two vertices in the graph.

        Args:
            s (any): The starting vertex.
            e (any): The ending vertex.

        Returns:
            list: A list of the vertices in the shortest path, or an empty list if no path is found.
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
        s (str): The string to calculate the hash value for.

    Returns:
        int: The hash value of the string.
    """
    hv = 0
    for c in s:
        hv = ((hv << 5) + hv) + ord(c)
    return hv & 0x7FFFFFFF


def y(n):
    """
    Checks if a number is prime.

    Args:
        n (int): The number to check.

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
        s (str): The first string.
        k (str): The second string.

    Returns:
        int: The edit distance between the two strings.
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
        Initializes a new instance of the T class.

        Args:
            v (any): The value to use.
        """
        self.v = v
        self.l = None
        self.r = None

    def i(self, v):
        """
        Inserts a value into the tree.

        Args:
            v (any): The value to insert.
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
            v (any): The value to search for.

        Returns:
            T: The node containing the value, or None if the value is not found.
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
            r (list, optional): The list to store the results in.
                Defaults to None.

        Returns:
            list: A list of the values in the tree in in-order.
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
    print(f'Found: {s.f(r'\\d+')}')

    l1 = [1, 2, 3, 4, 5]
    l2 = [2, 4, 6, 8, 10]
    print(f'Mapped: {m(l1, l2, lambda a, b: a+b)}')

    print(f'Factorial 5: {x(5)}')
    print(f'Is 17 prime: {y(17)}')
    print(f'Edit distance: {z('kitten', 'sitting')}')

    data = {'a': {'b': {'c': 42}}, 'x': 100}
    print(f'Deep get: {q(data, 'a.b.c')}')

    w('test.json', data)
    loaded = rd('test.json')
    print(f'Loaded: {loaded}')

    os.remove('test.json') if os.path.exists('test.json') else None


if __name__ == '__main__':
    main()
