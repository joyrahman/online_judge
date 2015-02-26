'''
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
'''

class Solution:
    # @param s, a string
    # @return an integer
    alphabet_mapping = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12,
                        'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23,
                        'X': 24, 'Y': 25, 'Z': 26, ' ': 0
    }

    def titleToNumber(self, s):
        if (len(s)==0):
            return 0
        value = 0
        total_len = len(s)
        for i in range(0,total_len):
            x = self.alphabet_mapping[s[i]]
            power = 1
            for z in range(0,total_len-1-i):
                power*=26
            value += x*power

        return value


def main():
    s = Solution()
    print(s.titleToNumber('AA'))



if __name__ == "__main__":
    main()
