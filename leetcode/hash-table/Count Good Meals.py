class Solution:
    def countPairs(self, deliciousness: list[int]) -> int:
        nums = {}
        answer = 0
        MOD = 10 ** 9 + 7
        for delicious in deliciousness:
            for power in range(22):
                paired = (1 << power) - delicious
                if paired in nums:
                    answer = (answer + nums[paired]) % MOD
            if delicious not in nums:
                nums[delicious] = 1
            else:
                nums[delicious] += 1
        return answer
