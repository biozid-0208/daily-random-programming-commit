class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        d = {}
        for i, n in enumerate(mat):
            d[i] = sum(n)
        sortedDict = sorted(d, key = d.get)
        return sortedDict[:k]
        