'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

'''
import unittest


class Solution:
    # @return a string
    def convert(self, s, nRows):
        zigzag_list = []
        for i in range(nRows):
            zigzag_list.append([])

        string_length = len(s)
        i = 0
        while (i < string_length):
            for k in range(0, nRows):
                if i == string_length:
                    break
                # print("{}=>{}".format(s[i],k))
                zigzag_list[k].append(s[i])
                i += 1

            for j in range(nRows - 2, 0, -1):
                if i == string_length:
                    break
                # print("{}=>{}".format(s[i],j))
                zigzag_list[j].append(s[i])
                i += 1

        converted_string = ""
        for i in range(nRows):
            for item in zigzag_list[i]:
                converted_string += str(item)

        return (converted_string)


class zigzag_test(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.convert("PAYPALISHIRING"), "PAHNAPLSIIGYIR")


def main():
    # s = Solution()
    #print(s.convert("PAYPALISHIRING",3))
    z = zigzag_test()
    z.test()


if __name__ == "__main__":
    main()



