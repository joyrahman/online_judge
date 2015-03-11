'''
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

'''
# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        a = self.list_to_int(l1)
        b = self.list_to_int(l2)
        #print a
        #print b
        c = a + b
        return self.int_to_list(c)




    def int_to_list(self,c):
        c = str(c)
        length = len(c)
        #head = ListNode(c[length-1])
        #for i in range(length-2,-1,-1):
        head = ListNode(c[0])
        for i in range(1,length):
            temp = ListNode(c[i])
            temp.next = head
            head = temp

        return head


    def list_to_int(self, head):
        temp = head
        val = 0
        #j = self.get_length(head)-1
        j = 0
        while temp is not None:
            val += temp.val * pow(10,j)
            j += 1
            temp = temp.next

        #print val
        return val

    def get_length(self, head):
        temp = head
        count = 0
        while temp is not None:
            temp = temp.next
            count +=1
        return count


def create_linked_list(A):
    length = len(A)
    head = ListNode(A[length-1])
    #print head.val

    for i in range(length-2,-1,-1):
        #print "i:",i
        temp = ListNode(A[i])
        #print temp.val
        temp.next = head
        head = temp
        #print "({},{})".format(head.val, head.next.val)

    return head

def print_linked_list(head):
    temp = head

    while temp is not None:
        print "{}->".format(temp.val),
        temp = temp.next


def main():

    A = [2,4,3]
    B = [5,6,4]
    list_A = create_linked_list(A)
    list_B = create_linked_list(B)
    #print list_A, "ball"
    #print_linked_list(list_A)
    s = Solution()

    list_C = s.addTwoNumbers(list_A,list_B)
    print_linked_list(list_C)
        
if __name__ == "__main__":
    main()