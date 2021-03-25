class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        else:
            sign = x//abs(x)
            rev = sign * int(str(abs(x))[::-1])
            if -2 **31 > rev or rev > 2**31 -1:
                return 0
            else:
                return rev

            # rev = 0
            # while x !=0:
            #     temp = x % 10
            #     rev = rev*10 + temp
            #     x //= int(10)
            # return rev