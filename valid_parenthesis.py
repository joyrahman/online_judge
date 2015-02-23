class Solution:
    # @return a boolean
    def isValid(self, s):
        input_length = len(s)
        stack = []
        response = True

        for i in range(0, input_length):
            try:
                if (s[i] == '(') or (s[i] == '[') or (s[i] == '{'):
                    stack.append(s[i])
                elif (s[i] == ')') and (stack.pop() != '('):
                    response = False
                elif (s[i] == ']') and (stack.pop() != '['):
                    response = False
                elif (s[i] == '}') and (stack.pop() != '{'):
                    response = False

            except Exception as e:
                return False
        if stack:
            response = False

        return response


def main():
    s = Solution()
    print s.isValid("()")


if __name__ == "__main__":
    main()