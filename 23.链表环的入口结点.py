给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。

#使用快慢指针，快的走一步，慢的一次走两步，如果快的指针到尾也没追上，则无环，追上就有。


 -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead or not pHead.next or not pHead.next.next:
            return None
        slow = pHead.next
        fast = slow.next
        has = 0
        while fast.next != None:
            if fast == slow:
                has = 1
                break
            else:
                slow = slow.next
                fast = fast.next.next
        if has:
            slow = pHead
                
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
        else:
            return None
            
            
        
