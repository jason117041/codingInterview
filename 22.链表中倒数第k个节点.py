题目描述
输入一个链表，输出该链表中倒数第k个结点。

#l两种解法，第一种，先遍历所有，得到长度n，然后从头遍历n-k+1就可以得到
#解法2：一次遍历：两个指针，第一个先遍历k-1，然后第二个指针跟着第一个指针一起走，第一个走到尾，第二个即为要求。
#注意，指针为空，或k=0，或k大于总长度的边界条件。

class Solution:
    def FindKthToTail(self, head, k):
        # write code here   
        if head is None or k == 0:
            return None

        phead = ListNode(0)
        phead = head
        pbehind = ListNode(0)
        for i in range(k-1):
            if phead.next is not None:
                phead = phead.next
            else:
                return None
        pbehind = head
        while phead.next is not None:
            phead = phead.next
            pbehind = pbehind.next
        return pbehind
