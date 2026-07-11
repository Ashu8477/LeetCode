class Solution:
    def reverse(self, x: int) -> int:

        sign = -1 if x<0 else 1
        x=abs(x)

        total=0

        while x>0:
            rem=x%10
            total=total*10+rem
            x=x//10
       
        final=total*sign
        if final<-(2**31) or final>(2**31-1):
            return 0
        return final