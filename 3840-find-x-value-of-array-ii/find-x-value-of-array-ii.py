class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)
        tree = [None] * (4 * n)

        def merge(a, b):
            p1, c1 = a
            p2, c2 = b

            c = c1[:]

            for x in range(k):
                c[(p1 * x) % k] += c2[x]

            return (p1 * p2 % k, c)

        def build(i, l, r):
            if l == r:
                c = [0] * k
                c[nums[l] % k] = 1
                tree[i] = (nums[l] % k, c)
                return

            m = (l + r) // 2
            build(i * 2, l, m)
            build(i * 2 + 1, m + 1, r)
            tree[i] = merge(tree[i * 2], tree[i * 2 + 1])

        def update(i, l, r, pos, val):
            if l == r:
                c = [0] * k
                c[val % k] = 1
                tree[i] = (val % k, c)
                return

            m = (l + r) // 2

            if pos <= m:
                update(i * 2, l, m, pos, val)
            else:
                update(i * 2 + 1, m + 1, r, pos, val)

            tree[i] = merge(tree[i * 2], tree[i * 2 + 1])

        def query(i, l, r, ql, qr):
            if ql <= l and r <= qr:
                return tree[i]

            m = (l + r) // 2

            if qr <= m:
                return query(i * 2, l, m, ql, qr)

            if ql > m:
                return query(i * 2 + 1, m + 1, r, ql, qr)

            return merge(
                query(i * 2, l, m, ql, qr),
                query(i * 2 + 1, m + 1, r, ql, qr)
            )

        build(1, 0, n - 1)

        ans = []

        for idx, val, start, x in queries:
            update(1, 0, n - 1, idx, val)
            ans.append(query(1, 0, n - 1, start, n - 1)[1][x])

        return ans
        