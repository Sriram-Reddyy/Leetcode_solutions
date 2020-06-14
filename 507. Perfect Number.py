"""
507. Perfect Number
Easy

246

589

Add to List

Share
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
"""
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        sum_of_factor = 1
        for i in range(2, floor( num**0.5 ) + 1 ):
            if num % i == 0:
                if i == num // i :
                    sum_of_factor +=  i
                else:
                    sum_of_factor += ( i + num // i )
        return sum_of_factor == num
