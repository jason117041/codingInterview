#题目描述
#输入一个链表，反转链表后，输出新链表的表头。

#需要三个指针，一个保存当前，一个保存下一个，一个保存上一个

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead  or not pHead.next:
            return pHead
        pnext = None
        pre = None
        p = pHead
        while p:
            pnext = p.next
            p.next = pre
            pre = p
            p = pnext
        return pre
