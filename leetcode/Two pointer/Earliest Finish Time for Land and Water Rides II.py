from typing import List

class Solution:
    def getMinTemp(self, startTime: List[int], duration: List[int], size: int) -> int:
        temp = float('inf')
        for i in range(size):
            temp = min(temp, startTime[i] + duration[i])
        return temp

    def getEarliest(self, prevFinished: int, startTime: List[int], duration: List[int], size: int) -> int:
        earliest = float('inf')
        for j in range(size):
            earliest = min(earliest, max(prevFinished, startTime[j]) + duration[j])
        return earliest

    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        n = len(landStartTime)
        m = len(waterStartTime)
        temp_lw = self.getMinTemp(landStartTime, landDuration, n)
        temp_wl = self.getMinTemp(waterStartTime, waterDuration, m)
        earliest_lw = self.getEarliest(temp_lw, waterStartTime, waterDuration, m)
        earliest_wl = self.getEarliest(temp_wl, landStartTime, landDuration, n)
        return min(earliest_lw, earliest_wl)

if __name__ == "__main__":
    sol = Solution()
    landStartTime = [5]
    landDuration = [3]
    waterStartTime = [1]
    waterDuration = [10]
    print(sol.earliestFinishTime(landStartTime, landDuration, waterStartTime, waterDuration))
