class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


'''
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.
# Definition for singly-linked list.

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):


'''
class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        head_a = l1
        head_b = l2
        counter = 3
        #while head_a is not None and head_b is not None:
        #while counter<=10:
        while True:
            if head_a is None:
                prev_a.next = head_b
                print "A executed"
                break

            elif head_b is None:
                prev_b.next = head_a
                #head_b.next = head_a
                print "B executed"

                break
            if head_a.val < head_b.val:
                #print "1.{}-{}".format(head_a.val, head_b.val)

                prev_a = head_a
                if head_a.next is not None:
                    head_a = head_a.next
                    print "a:"+str(head_a.val)

            elif head_a.val >= head_b.val:
                #print "2.{}-{}".format(head_a.val, head_b.val)
                prev_a.next = head_b
                temp = head_b
                prev_b = head_b
                if head_b.next is not None:
                    head_b = head_b.next
                    print "b:"+str(head_b.val)
                temp.next = head_a
                prev_a = temp

                #print "3.{}-{}".format(head_a.val, prev_a.val)
            #counter += 1
            #print counter
            #if counter == 3:
             #   break




            #if head_a is None or head_b is None:
            #    break

        return l1


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
    A = [1,2,4,6,7,9]
    B = [2,3,5,6,8,10]
    list_a = create_linked_list(A)
    list_b = create_linked_list(B)
    #print_linked_list(list_a)
    #print_linked_list(list_b)
    s = Solution()
    s.mergeTwoLists(list_a,list_b)
    print_linked_list(list_a)



if __name__ == "__main__":
    main()