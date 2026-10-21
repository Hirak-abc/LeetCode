class Solution(object):
    def decrypt(self, code, k):
        n = len(code)

        if k == 0:
            return [0] * n

        arr = code + code
        p = [0] * (len(arr) + 1)

        for i in range(len(arr)):
            p[i + 1] = p[i] + arr[i]

        ans = []

        for i in range(n):
            if k > 0:
                total = p[i + k + 1] - p[i + 1]
            else:
                m = abs(k)
                total = p[n + i] - p[n + i - m]

            ans.append(total)

        return ans