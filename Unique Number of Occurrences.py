class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        if len(set(arr))==len(set(Counter(arr).values())):

            return True

        return False

        