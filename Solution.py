# Merge k Sorted Lists
# Difficulty: Hard
# Tags: Linked List, Heap, Divide and Conquer

import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        """
        Merge k sorted linked lists into one sorted linked list.
        """
        heap = []
        
        # Push the first node of each list into the heap
        for idx, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, idx, node))
        
        dummy = ListNode(0)
        curr = dummy
        
        # Extract the smallest node and push its next into the heap
        while heap:
            val, idx, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))
        
        return dummy.next


# Helper functions for testing
def build_linked_lists(arr):
    """Build multiple linked lists from a 2D array."""
    lists = []
    for sublist in arr:
        dummy = ListNode(0)
        curr = dummy
        for val in sublist:
            curr.next = ListNode(val)
            curr = curr.next
        lists.append(dummy.next)
    return lists

def to_list(node):
    """Convert a linked list back to a Python list."""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


# Example usage
if __name__ == "__main__":
    lists = build_linked_lists([[1,4,5],[1,3,4],[2,6]])
    solution = Solution()
    merged = solution.mergeKLists(lists)
    print(to_list(merged))  # Output: [1,1,2,3,4,4,5,6]
