# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# https://leetcode.com/problems/linked-list-cycle/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        nodes_seen = set()
        while head is not None:
            if head in nodes_seen:
                return True
            nodes_seen.add(head)
            head = head.next
        return False


def Example1():
    print('Example1')

    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2

    solution = Solution()

    print(solution.hasCycle(node1))


def Example2():
    print('Example2')

    node1 = ListNode(1)
    node2 = ListNode(2)

    node1.next = node2
    node2.next = node1

    solution = Solution()

    print(solution.hasCycle(node1))


def Example3():
    print('Example3')

    node1 = ListNode(1)

    solution = Solution()

    print(solution.hasCycle(node1))


Example1()
Example2()
Example3()
