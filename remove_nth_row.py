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
