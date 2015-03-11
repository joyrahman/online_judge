'''
Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.
'''
import math
class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        org_str = str(x)
        print(org_str[0:m])
        length = len(org_str)
        if length%2==0:
            m = (length/2)
            print "m: ",m
            print(org_str[0:m])

            print "a.{},{}".format(org_str[0:m-1], org_str[length-1:m:-1])
            if org_str[0:m-1] == org_str[length-1:m:-1]:
                return True
        if length%2==1:
            length -= 1
            m = (length/2)
            print "m: ",m
            print "b.{},{}".format(org_str[0:m-1], org_str[length:m+1:-1])
            if org_str[0:m-1] == org_str[length:m+1:-1]:
                return True

        return False



def main():
    test = 11001
    s = Solution()
    print(s.isPalindrome(test))



if __name__ == "__main__":
    main()