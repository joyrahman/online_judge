'''
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37
'''
class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def string_to_int(self,list):
        result = []
        #print(list)
        for item in list:
            result.append(int(item))
        return result
    def compareVersion(self, version1, version2):
        slist1 = version1.split(".")
        slist2 = version2.split(".")

        list1 = self.string_to_int(slist1)
        list2 = self.string_to_int(slist2)
        len1 = len(list1)
        len2 = len(list2)
        if len1 > len2:
            list2 += [0] * (len1 - len2)
        elif len2 > len1:
            list1 += [0] * (len2 - len1)
        len1 = len(list1)
        len2 = len(list2)
        #print list1
        #print list2
        flag_v1 = False
        flag_v2 = False
        for i in range(len1):
            if list1[i] > list2[i]:
                    # print "a) l1:{} l2:{}".format(list1[i],list2[i])
                flag_v1 = True
                break
            if list1[i] < list2[i]:
                    # print "b) l1:{} l2:{}".format(list1[i],list2[i])
                flag_v2 = True
                break



        if flag_v1: return 1
        elif flag_v2: return -1
        elif not flag_v1 and not flag_v2: return 0






def main():
    s = Solution()
    test_v1 = "13.1"
    test_v2 = "1.1.1"
    result = s.compareVersion(test_v1,test_v2)
    print(result)


if __name__ == "__main__":
    main()