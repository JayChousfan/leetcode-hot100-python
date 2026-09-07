"""
============================================================
LeetCode 128. 最长连续序列 (Longest Consecutive Sequence) — Hot 100
============================================================
难度：中等

题目：给定一个未排序的整数数组 nums，找出数字连续的最长序列长度。
      要求算法的时间复杂度为 O(n)。

示例：
  输入: nums = [100,4,200,1,3,2]
  输出: 4
  解释: 最长连续序列是 [1,2,3,4]

============================================================
Python 语法要点（C++ 对比）
============================================================

1. set 集合去重
   C++:  unordered_set<int> num_set(nums.begin(), nums.end());
   Python: num_set = set(nums)
   → set 自动去重，平均查找复杂度为 O(1)

2. not in 判断元素不存在
   C++:  num_set.find(num - 1) == num_set.end()
   Python: num - 1 not in num_set
   → not in 比 not (num in container) 更自然易读

3. 遍历集合
   C++:  for (int num : num_set)
   Python: for num in num_set:
   → 集合无固定顺序，但本题只统计长度，不依赖遍历顺序

4. max() 更新最优值
   C++:  max_len = max(max_len, current_len);
   Python: max_len = max(max_len, current_len)
   → Python 内置 max() 可比较两个或更多值
"""


def longestConsecutive(nums: list[int]) -> int:
    """
    用集合查找连续数字，只从没有前驱的数字开始扩展序列。
    时间复杂度 O(n)，空间复杂度 O(n)
    """
    num_set: set[int] = set(nums)
    max_len = 0

    for num in num_set:
        # num - 1 不存在时，num 才可能是连续序列的起点
        if num - 1 not in num_set:
            current_num = num
            current_len = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_len += 1

            max_len = max(max_len, current_len)

    return max_len


# =============================================================================
# 测试代码
# =============================================================================
if __name__ == "__main__":
    assert longestConsecutive([100, 4, 200, 1, 3, 2]) == 4, "示例1失败"
    assert longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9, "重复元素测试失败"
    assert longestConsecutive([]) == 0, "空数组测试失败"
    print("✅ P03 最长连续序列 全部测试通过")
