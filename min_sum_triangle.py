'''
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
'''


class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        sum_triangle = 0
        index = 0
        for row in triangle:
           #print "running on row:{} with index={} value".format(row, index)
            if (index ==0 and len(row)==1):
                min_val = row[index]
                sum_triangle += min_val
                #print(">(First If) picked {} in row: {} with sum:{}".format(min_val, row,sum_triangle))


            elif (index==0 and len(row)==2):
                min_val = row[index]
                if row[index+1] < min_val:
                    min_val = row[index+1]
                    index = index+1

                sum_triangle += min_val
                #print(">(Second If) picked {} in row: {} with sum:{}".format(min_val, row, sum_triangle))



            elif (index==0 and len(row)>2):
                for i in range(index,index+2):
                    min_val = row[index]
                    if row[i] < min_val:
                        min_val = row[i]
                        index = i
                sum_triangle += min_val
                #print(">(Third for) picked {} in row: {} with sum:{}".format(min_val, row,sum_triangle))


            else:
                min_val = row[index]
                for i in range(index-1,index+2,1):
                    if row[i] < min_val:
                        min_val = row[i]
                        index = i
                        #print(">(Forth for) picked {} in row: {}".format(min_val, row))
                sum_triangle += min_val
                #print(">(Fourth Loop for) picked {} in row: {} with sum:{}".format(min_val, row,sum_triangle))


        return sum_triangle



def main():
    test_triangle = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    test_triangle2 = [
        [-1],
        [2,3,4],
        [-2,1,-3]


    ]
    s = Solution()
    print (s.minimumTotal(test_triangle))
    print (s.minimumTotal(test_triangle2))



if __name__ == "__main__":
    main()
