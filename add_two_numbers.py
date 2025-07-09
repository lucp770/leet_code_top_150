"""
2. Add Two Numbers

ou are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



""" 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val} -> {self.next}'

class Solution:

    def create_List_Node(self,number:int):
        lst = list(str(number))
        lst = list(reversed(lst))
        first_node = ListNode(int(lst[0]))#first node sem referencia

        previous_node = first_node

        for value in lst[1:]:
            curr_node = ListNode(int(value))
            previous_node.next = curr_node

            previous_node = curr_node

        return first_node

    def getNumber(self,l: ListNode) -> int:
        # l is the firts node
        number = str(l.val)
        next_node = l.next

        while next_node:
            number += str(next_node.val)
            next_node = next_node.next

        return int(''.join(list(reversed(list(number)))))


    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = self.getNumber(l1)
        n2 = self.getNumber(l2)
        print(n1,n2)

        result = n1+n2
        result = self.create_List_Node(result)
        print(result)
        return result


if __name__=='__main__':

    
    s = Solution()
    
    l1 = s.create_List_Node(465)
    l0 = s.create_List_Node(342)
    s.addTwoNumbers(l0,l1)