"""
============================================================
LeetCode 33. 搜索旋转排序数组 (Search in Rotated Sorted Array) — Hot 100
============================================================
难度：中等

题目：整数数组 nums 原本升序且元素互不相同，在未知位置旋转后，给定
      target；找到则返回下标，否则返回 -1，要求时间复杂度 O(log n)。

示例：
  输入: nums = [4,5,6,7,0,1,2], target = 0
  输出: 4

============================================================
Python 语法要点（C++ 对比）
============================================================

1. // 整数除法
   C++:  int mid = left + (right - left) / 2;
   Python: mid = (left + right) // 2
   → // 向下取整；Python 整数可自动扩展，不会发生固定宽度整数溢出

2. 链式比较
   C++:  nums[left] <= target && target < nums[mid]
   Python: nums[left] <= target < nums[mid]
   → Python 可把同一变量参与的多个比较连写，并且只求值一次中间项

3. float('inf') 与 float('-inf')
   C++:  numeric_limits<double>::infinity()
   Python: float("inf") / float("-inf")
   → 可作为没有上下界时的哨兵值；本题元素为整数，因此不需要额外哨兵

4. 无符号下标差异
   C++:  size_t 下标减到 -1 可能发生无符号溢出
   Python: right = middle - 1
   → Python 下标变量是普通整数，循环条件 left <= right 负责阻止越界访问
"""


def search(nums: list[int], target: int) -> int:
    """
    变形二分：每轮至少有一半有序，判断 target 是否落在该有序区间。
    时间复杂度 O(log n)，空间复杂度 O(1)
    """
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # 左半部分有序
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # 右半部分有序
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


# =============================================================================
# 测试代码
# =============================================================================
if __name__ == "__main__":
    result1 = search([4, 5, 6, 7, 0, 1, 2], 0)
    assert result1 == 4, f"示例1失败: {result1}"
    assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1, "目标不存在测试失败"
    assert search([1], 1) == 0, "单元素测试失败"
    print("✅ P18 搜索旋转排序数组 全部测试通过")
