'''
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
'''


class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        prev_row = []
        for i in range(0,rowIndex):
            next_row = [0]*rowIndex

            for j in range(0,i+1):
                #print "before",next_row,

                if(j == 0) or (j == i):
                    next_row[j]=1
                else:
                    next_row[j] = prev_row[j-1] + prev_row[j]
                #print "after{}=>{}".format(i,j),next_row,'\n'
            prev_row = next_row


        return prev_row


def main():
    # s = Solution2()
    # p = s.generate(5)
    # print(p)
    # q = Solution3()
    # p = q.generate(5)
    # print(p)
    #
    s = Solution()
    print (s.getRow(5))

if __name__ == "__main__":
    main()

