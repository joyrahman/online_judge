'''
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Have you thought about this?
Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Update (2014-11-10):
Test cases had been added to test the overflow behavior.
'''
import math
import sys
class Solution:
    # @return an integer
    def int_overflow(self,val):
        if not -sys.maxint-1 <= val <= sys.maxint:
            return True
        return False
    def detect_additive_overflow(self,a,b):
        if a<b:
            return True
        return False

    def detect_multiplicative_overflow(self,a,b,c):
        if b==0 or c !=a/b:
            return True
        return False


    def reverse(self, x):
        #print "x:{}".format(x)
        #check negetive
        negetive_flag = 1
        if x < 0:
            negetive_flag = -1
            x *= -1
        power = len(str(x))-1

        result = 0


        while(x):
            y = int(x%10)
            #print y
            temp_mul = int(y) * pow(10,power)
            if self.detect_multiplicative_overflow(temp_mul,pow(10,power),int(y)):
                return 0
            else:
                temp_add = result +  temp_mul

            if self.detect_additive_overflow(temp_add,result):
                return 0
            else:
                result = temp_add
            x = x / 10
            power -= 1



        if self.int_overflow(result):
            return 0
        return result * negetive_flag





def main():
    test = 1534236469
    s = Solution()
    result = s.reverse(test)
    print (result)

if __name__ == "__main__":
    main()