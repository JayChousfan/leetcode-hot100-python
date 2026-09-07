"""
============================================================
LeetCode 560. 和为K的子数组 (Subarray Sum Equals K) — Hot 100
============================================================
难度：中等

题目：给定一个整数数组 nums 和一个整数 k，请统计并返回数组中和为 k
      的连续子数组个数。

示例：
  输入: nums = [1,1,1], k = 2
  输出: 2

============================================================
Python 语法要点（C++ 对比）
============================================================

1. defaultdict(int) 默认值为 0
   C++:  unordered_map<int, int> counts; counts[prefix]++;
   Python: counts = defaultdict(int)
   → int() 的默认结果是 0，首次访问不存在的 key 时可直接累加

2. 前缀和变量累加
   C++:  current_sum += num;
   Python: current_sum += num
   → += 会把计算结果重新绑定给变量

3. 字典按键读取计数
   C++:  count += prefix_count[current_sum - k];
   Python: count += prefix_count[current_sum - k]
   → 若存在前缀和 prefix - k，则两段前缀之差正好为 k

4. 初始化空前缀
   C++:  prefix_count[0] = 1;
   Python: prefix_count[0] = 1
   → 空前缀使从数组下标 0 开始、和恰好为 k 的子数组也能被统计
"""

from collections import defaultdict


def subarraySum(nums: list[int], k: int) -> int:
    """
    前缀和加哈希计数：累加此前出现过的 prefix - k 的次数。
    时间复杂度 O(n)，空间复杂度 O(n)
    """
    prefix_count: defaultdict[int, int] = defaultdict(int)
    prefix_count[0] = 1
    current_sum = 0
    count = 0

    for num in nums:
        current_sum += num
        # current_sum - previous_sum == k
        count += prefix_count[current_sum - k]
        prefix_count[current_sum] += 1

    return count


# =============================================================================
# 测试代码
# =============================================================================
if __name__ == "__main__":
    assert subarraySum([1, 1, 1], 2) == 2, "示例1失败"
    assert subarraySum([1, 2, 3], 3) == 2, "多子数组测试失败"
    assert subarraySum([-1, -1, 1], 0) == 1, "含负数测试失败"
    print("✅ P08 和为K的子数组 全部测试通过")
