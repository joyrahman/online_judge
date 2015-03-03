import math

class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        hash_table = {}
        for item in num:
            if item not in hash_table:
                hash_table[item] = 1
            else:
                hash_table[item] += 1
        #print hash_table
        thresh_hold = math.floor(len(num)/2)
        #print thresh_hold
        val_max_element = 0
        key_max_element = 0
        for k,v in hash_table.iteritems():
            #print k,"->",v
            if (v> thresh_hold):
                if (v> val_max_element):
                    val_max_element = v
                    key_max_element = k


        return key_max_element


def main():
    s = Solution()
    x = s.majorityElement([1,1,1,2,2,4,4,4,4,4,5,4,4,1,4])
    print(x)


if __name__ == "__main__":
    main()