class Solution:
    def processStr(self, s: str, k: int) -> str:
        # Step 1: Forward pass to record the length evolution
        lengths = []
        curr_len = 0

        for c in s:
            if c == "#":
                curr_len *= 2
            elif c == "%":
                pass
            elif c == "*":
                if curr_len > 0:
                    curr_len -= 1
            else:
                curr_len += 1
            lengths.append(curr_len)
        if k < 0 or k >= curr_len:
            return "."

        # Step 2: Backward pass to trace index k
        for i in range(len(s) - 1, -1, -1):
            c = s[i]
            prev_len = lengths[i - 1] if i > 0 else 0

            if c == "#":
                # If k is in the duplicated second half, map it to the first half
                if k >= prev_len:
                    k -= prev_len
            elif c == "%":
                # Mirror the index for the reverse operation
                if prev_len > 0:
                    k = prev_len - 1 - k
            elif c == "*":
                pass
            else:
                # Literal character. If k points to the end of the current prefix:
                if k == prev_len:
                    return c

        return "."
