class Solution:
    def addDigits(self, num: int) -> int:
        res=1000
        while res >= 10:
            n = str(num)
            d = [int(s) for s in n]
            summ=sum(d)
            res=summ
            num=summ
        return res
    
    """
class Solution:
    def addDigits(self, num: int) -> int:
        return 0 if num == 0 else 9 if  num%9==0 else num%9
    some optimal solution l found on the internet

"""