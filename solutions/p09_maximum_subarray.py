"""
============================================================
LeetCode 53. 最大子数组和 (Maximum Subarray) — Hot 100
============================================================
难度：中等

题目：给定一个整数数组 nums，找出一个具有最大和的连续子数组，返回其
      最大和。子数组至少包含一个元素。

示例：
  输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
  输出: 6
  解释: 连续子数组 [4,-1,2,1] 的和最大

============================================================
Python 语法要点（C++ 对比）
============================================================

1. 切片取得后续元素
   C++:  从 nums.begin() + 1 开始遍历
   Python: nums[1:]
   → start:stop 切片包含 start，不包含 stop；省略 stop 表示直到末尾

2. 同时初始化多个变量
   C++:  int current_sum = nums[0], max_sum = nums[0];
   Python: current_sum = max_sum = nums[0]
   → 连续赋值会把同一个值绑定给多个变量

3. max() 表达状态转移
   C++:  current_sum = max(num, current_sum + num);
   Python: current_sum = max(num, current_sum + num)
   → 当前元素要么独立开始新子数组，要么接在此前子数组后面

4. float('-inf') 表示负无穷
   C++:  numeric_limits<double>::lowest()
   Python: float("-inf")
   → 可用于初始化“尚未取得任何最大值”的变量；本题直接用 nums[0] 更准确
"""


def maxSubArray(nums: list[int]) -> int:
    """
    Kadane 动态规划：current_sum 表示以当前位置结尾的最大子数组和。
    时间复杂度 O(n)，空间复杂度 O(1)
    """
    current_sum = max_sum = nums[0]

    for num in nums[1:]:
        # 选择从 num 重新开始，或接在前一个子数组后面
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


# =============================================================================
# 测试代码
# =============================================================================
if __name__ == "__main__":
    assert maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6, "示例1失败"
    assert maxSubArray([1]) == 1, "单元素测试失败"
    assert maxSubArray([-3, -2, -5]) == -2, "全负数测试失败"
    print("✅ P09 最大子数组和 全部测试通过")
