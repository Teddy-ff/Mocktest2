# Merge k Sorted Lists

**Difficulty:** Hard  
**Tags:** Linked List, Heap, Divide and Conquer  

---

## 🧩 Problem
You are given an array of `k` linked-lists, each linked-list sorted in ascending order.  
Merge all linked-lists into one sorted linked-list and return it.

**Example:**
Input: [[9,9,4],[6,6,8],[2,1,1]] Output: 4 Explanation: The longest increasing path is [1, 2, 6, 9]



---

## 🧠 Approach
We use a **Min Heap (Priority Queue)** to efficiently pick the smallest node among all current heads:
1. Push the first node of each list into a heap.
2. Pop the smallest node and append it to the merged list.
3. Push its `next` node (if any) into the heap.
4. Repeat until the heap is empty.

This ensures the merged list is built in sorted order efficiently.

---

## ⏱️ Complexity
- **Time:** O(N log k) — where N is the total number of nodes
- **Space:** O(k) for heap

---

## 🧑‍💻 Code
See `solution.py` for the full implementation.
