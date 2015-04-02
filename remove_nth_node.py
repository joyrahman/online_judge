class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.
Try to do this in one pass.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None




class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        runner = head
        temp = head
        prev = None
        for i in range(1, n):
            runner = runner.next
        #print runner.val
        while runner is not None:
            #print "T:{}".format(temp.val)
            #print "R:{}".format(runner.val)
            if (runner.next is not None):
                #temp = temp.next
                prev = temp
                temp = temp.next
            runner = runner.next
        # now delete the element at temp
        if(temp == head):
            head = temp.next
        else:
            prev.next = temp.next
        #prev.next = temp.next
        #print "prev:{} next:{}".format(prev.val,temp.val)
        #print_linked_list(head)
        return head




def create_linked_list(A):
    length = len(A)
    index = length -1
    head = ListNode(A[length-1])
    #head = ListNode(A.pop(index))
    #print head.val

    for i in range(length-2,-1,-1):
        #print item
        #print "i:",i
        temp = ListNode(A[i])
        #temp = ListNode(item)
        #print temp.val
        temp.next = head
        head = temp
        #index -= 1
        #print "({},{})".format(head.val, head.next.val)
    return  head


def print_linked_list(head):
    temp = head

    while temp is not None:
        print "{}->".format(temp.val),
        temp = temp.next



def main():
    A = [1,2,3,4,5]
    head = create_linked_list(A)
    n = 5

    s = Solution()
    print_linked_list(s.removeNthFromEnd(head,n))
    #print_linked_list(head)



if __name__ == "__main__":
    main()