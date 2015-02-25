# count_and_say.py
'''
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

'''


class Solution:
    # @return a string

    @staticmethod
    def list_to_string(list):
        result = ''
        for item in list:
            result += item
            result += ", "
        x = len(result)-2
        return  result[0:x]

    @staticmethod
    def generate_next(prev):
        count = 1
        result = ''
        prev += ' '

        for i in range(0, len(prev)-1):
            if prev[i] == prev[i+1]:
                count += 1

            else:
                result += str(count)
                result += prev[i]
                #index = i+1
                count = 1
        # if result == '':
        #     result += '11'

        return (result)


    def countAndSay(self, n):
        list = ['1']
        for i in range(1, n ):

            prev = list.pop()
            next = self.generate_next(prev)


            list.append(prev)
            list.append(next)

        last_item = list.pop()
        result = last_item
        return result


def main():
    s = Solution()
    print (s.countAndSay(2))


if __name__ == '__main__':
    main()

