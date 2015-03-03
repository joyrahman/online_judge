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
        prev_row = [0]*rowIndex
        next_row = [0]*rowIndex
        prev_row[0] = 1
        next_row [0] = 1

        for i in range(1,rowIndex):
            for j in range(1,i):
                next_row[j] = prev_row[j-1] + prev_row[j]
                prev_row = next_row

        return next_row

class Solution3:
    # @return a list of lists of integers
    def generate(self, numRows):
        pyramid = [[1 for i in xrange(rows)] for rows in xrange(1, numRows+1)]
        #print pyramid
        for i in range(1, numRows):
            for j in range(1,i):
                 # if j==1 or j==i:
                 #     pyramid[i][j] = 1
                 # else:
                    pyramid[i][j] = pyramid[i-1][j-1] + pyramid[i-1][j]




        return pyramid


class Solution2:
    # @return a list of lists of integers
    def generate(self, numRows):
        if not numRows: return []
        out = [[1 for i in xrange(row)] for row in xrange(1, numRows+1)]
        print out
        for row in xrange(1, numRows):
            for i in xrange(1, row): out[row][i] = out[row-1][i-1] + out[row-1][i]
        return out


def main():
    # s = Solution2()
    # p = s.generate(5)
    # print(p)
    # q = Solution3()
    # p = q.generate(5)
    # print(p)
    #
    s = Solution()
    print (s.getRow(1))

if __name__ == "__main__":
    main()

