"""
============================================================
LeetCode 1. 两数之和 (Two Sum) — Hot 100
============================================================
难度：简单

题目：给定一个整数数组 nums 和一个整数目标值 target，请在数组中找出
      和为 target 的两个整数，并返回它们的数组下标。
      每种输入只会对应一个答案，同一个元素不能使用两遍。

示例：
  输入: nums = [2,7,11,15], target = 9
  输出: [0,1]
  解释: nums[0] + nums[1] == 9

============================================================
Python 语法要点（C++ 对比）
============================================================

1. 字典 dict 对应哈希表
   C++:  unordered_map<int, int> mp;
   Python: mp: dict[int, int] = {}
   → dict 的键和值都可以通过类型注解标明，平均查询复杂度为 O(1)

2. enumerate() 同时取得下标和值
   C++:  for (int i = 0; i < nums.size(); ++i) { int num = nums[i]; }
   Python: for i, num in enumerate(nums):
   → enumerate() 避免手动维护下标变量

3. in 判断字典中是否存在键
   C++:  mp.find(complement) != mp.end()
   Python: complement in mp
   → 对字典使用 in 时检查的是 key，不是 value

4. 字典的下标访问与赋值
   C++:  mp[num] = i;
   Python: mp[num] = i
   → 已存在的键会更新值，不存在的键会创建新键值对

5. 类型注解 list[int]
   C++:  vector<int>
   Python: list[int]
   → Python 3.9+ 可以直接用内置容器写类型注解
"""


def twoSum(nums: list[int], target: int) -> list[int]:
    """
    一次遍历哈希表：查找当前数字所需的补数，再记录当前数字的下标。
    时间复杂度 O(n)，空间复杂度 O(n)
    """
    mp: dict[int, int] = {}  # key=数字, value=该数字的下标

    for i, num in enumerate(nums):
        complement = target - num
        # 先查补数，避免同一个元素被使用两次
        if complement in mp:
            return [mp[complement], i]
        mp[num] = i

    return []


# =============================================================================
# 测试代码
# =============================================================================
if __name__ == "__main__":
    result1 = twoSum([2, 7, 11, 15], 9)
    assert result1 == [0, 1], f"示例1失败: {result1}"
    assert twoSum([3, 2, 4], 6) == [1, 2], "普通测试失败"
    assert twoSum([3, 3], 6) == [0, 1], "重复元素测试失败"
    print("✅ P01 两数之和 全部测试通过")
