from math import gcd


class Solution:
    def smallestNumber(self, num: str, t: int) -> str:

        n = len(num)

        # --------------------------------------------------
        # t can only contain prime factors 2, 3, 5, 7
        # --------------------------------------------------

        x = t

        for p in (2, 3, 5, 7):
            while x % p == 0:
                x //= p

        if x != 1:
            return "-1"

        # --------------------------------------------------
        # rem[i] = factor still required after prefix [0:i]
        # --------------------------------------------------

        rem = [0] * (n + 1)
        rem[0] = t

        first_zero = n

        for i, ch in enumerate(num):

            d = ord(ch) - ord('0')

            if d == 0 and first_zero == n:
                first_zero = i

            rem[i + 1] = rem[i] // gcd(rem[i], d)

        # --------------------------------------------------
        # num itself is already valid
        # --------------------------------------------------

        if first_zero == n and rem[n] == 1:
            return num

        # --------------------------------------------------
        # We need to modify num.
        #
        # If there is a zero, start from the first zero.
        # Otherwise start from the last digit.
        # --------------------------------------------------

        start = first_zero if first_zero < n else n - 1

        # --------------------------------------------------
        # Try changing one digit from RIGHT -> LEFT
        # --------------------------------------------------

        for i in range(start, -1, -1):

            old_digit = int(num[i])

            if old_digit == 0:
                low = 1
            else:
                low = old_digit + 1

            # Try smallest possible bigger digit
            for new_digit in range(low, 10):

                # Remaining factor after fixing this digit
                need = rem[i] // gcd(rem[i], new_digit)

                # Store only non-1 digits.
                # They will occupy positions from right to left.
                picked = []

                j = n - 1

                # --------------------------------------------------
                # Fill suffix from RIGHT -> LEFT.
                #
                # We choose the LARGEST digit possible because
                # this gives smaller digits toward the left.
                # --------------------------------------------------

                while j > i and need != 1:

                    chosen = 0

                    for d in range(9, 1, -1):

                        if need % d == 0:
                            chosen = d
                            break

                    if chosen == 0:
                        break

                    picked.append((j, chosen))

                    need //= chosen
                    j -= 1

                # --------------------------------------------------
                # Successfully constructed required factor
                # --------------------------------------------------

                if need == 1:

                    # Everything not explicitly selected is '1'.
                    ans = list(
                        num[:i]
                        + str(new_digit)
                        + '1' * (n - i - 1)
                    )

                    # Put selected digits into their positions
                    for pos, digit in picked:
                        ans[pos] = str(digit)

                    return ''.join(ans)

        # --------------------------------------------------
        # No answer with same length.
        #
        # Therefore answer must have MORE digits.
        # --------------------------------------------------

        digits = []

        need = t

        # Extract largest possible digit factors first
        while need > 1:

            chosen = 0

            for d in range(9, 1, -1):

                if need % d == 0:
                    chosen = d
                    break

            if chosen == 0:
                return "-1"

            digits.append(str(chosen))
            need //= chosen

        # We extracted digits from RIGHT -> LEFT,
        # so reverse them.
        digits.reverse()

        # Must be strictly longer than num
        target_length = max(n + 1, len(digits))

        # Remaining positions are filled with 1
        ones = target_length - len(digits)

        return '1' * ones + ''.join(digits)