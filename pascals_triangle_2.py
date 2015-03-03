'''
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

class Solution:
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
    s = Solution2()
    p = s.generate(5)
    print(p)
    q = Solution()
    p = q.generate(5)
    print(p)

if __name__ == "__main__":
    main()

