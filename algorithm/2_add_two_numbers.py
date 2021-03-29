from algorithm.model import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head, tail = None, None
        cf = 0
        while l1 is not None or l2 is not None:
            n1 = 0 if l1 is None else l1.val
            n2 = 0 if l2 is None else l2.val
            sum = n1 + n2 + cf
            if head is None:
                head = ListNode(sum % 10)
                tail = head
            else:
                tail.next = ListNode(sum % 10)
                tail = tail.next

            cf = 0 if sum < 10 else 1
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        if cf > 0:
            tail.next = ListNode(val=1, next=None)
        return head


if __name__ == "__main__":
    l1 = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=None)))
    l2 = ListNode(val=3, next=ListNode(val=4, next=ListNode(val=9, next=None)))
    solution = Solution()
    res = solution.addTwoNumbers(l1, l2)
    while res is not None:
        print(res.val)
        res = res.next
