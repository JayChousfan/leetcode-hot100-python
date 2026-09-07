"""
============================================================
LeetCode 215. 数组中的第K个最大元素 (Kth Largest Element in an Array) — Hot 100
============================================================
难度：中等

题目：给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
      注意是排序后的第 k 个最大元素，而不是第 k 个不同的元素。

示例：
  输入: nums = [3,2,1,5,6,4], k = 2
  输出: 5

============================================================
Python 语法要点（C++ 对比）
============================================================

1. heapq 默认是最小堆
   C++:  priority_queue<int, vector<int>, greater<int>> heap;
   Python: import heapq
   → heapq 操作普通列表，并把最小元素维护在 heap[0]

2. heapify 原地建堆
   C++:  priority_queue<int, vector<int>, greater<int>> heap(data.begin(), data.end());
   Python: heapq.heapify(heap)
   → heapify() 在线性时间内把现有列表调整为堆

3. heappush 与 heappop
   C++:  heap.push(num); heap.pop();
   Python: heapq.heappush(heap, num); heapq.heappop(heap)
   → 每次插入或删除堆顶的时间复杂度都是 O(log k)

4. heapreplace 与 nlargest
   C++:  heap.pop(); heap.push(num);
   Python: heapq.heapreplace(heap, num); heapq.nlargest(k, nums)
   → heapreplace 一次完成弹出和压入；nlargest 可直接返回最大的 k 个值
"""

import heapq


def findKthLargest(nums: list[int], k: int) -> int:
    """
    维护大小为 k 的最小堆，堆顶始终是当前第 k 个最大元素。
    时间复杂度 O(n log k)，空间复杂度 O(k)
    """
    heap = nums[:k]
    heapq.heapify(heap)

    for num in nums[k:]:
        # 只有比堆顶大的数字才可能进入前 k 大
        if num > heap[0]:
            heapq.heapreplace(heap, num)

    return heap[0]


# =============================================================================
# 测试代码
# =============================================================================
if __name__ == "__main__":
    result1 = findKthLargest([3, 2, 1, 5, 6, 4], 2)
    assert result1 == 5, f"示例1失败: {result1}"
    result2 = findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
    assert result2 == 4, f"重复元素测试失败: {result2}"
    assert findKthLargest([1], 1) == 1, "单元素测试失败"
    print("✅ P17 数组中的第K个最大元素 全部测试通过")
