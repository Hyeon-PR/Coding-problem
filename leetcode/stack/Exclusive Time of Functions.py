class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        ext = [0] * n
        stack = []
        prev = 0
        for fid, se, tms in map(lambda log: log.split(":"), logs):
            fid, tms = int(fid), int(tms)
            if se == "start":
                if stack:
                    ext[stack[-1]] += tms - prev
                stack.append(fid)
                prev = tms
            else:
                ext[stack[-1]] += tms - prev + 1
                stack.pop()
                prev = tms + 1
        return ext
