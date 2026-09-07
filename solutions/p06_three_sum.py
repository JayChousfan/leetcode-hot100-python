"""
============================================================
LeetCode 15. 三数之和 (3Sum) — Hot 100
============================================================
难度：中等

题目：给你一个整数数组 nums，判断是否存在三元组 [nums[i],nums[j],nums[k]]
      满足 i!=j, i!=k, j!=k 且 nums[i]+nums[j]+nums[k]==0。
      返回所有和为 0 且不重复的三元组。

示例：
  输入: nums = [-1,0,1,2,-1,-4]
  输出: [[-1,-1,2],[-1,0,1]]

============================================================
Python 语法要点（C++ 对比）
============================================================

1. 列表原地排序
   C++:  sort(nums.begin(), nums.end());
   Python: nums.sort()
   → sort() 修改原列表并返回 None；sorted(nums) 则返回新列表

2. range() 控制循环范围
   C++:  for (int i = 0; i < n - 2; ++i)
   Python: for i in range(n - 2):
   → range(stop) 产生从 0 到 stop - 1 的整数

3. continue 跳过本轮循环
   C++:  if (i > 0 && nums[i] == nums[i - 1]) continue;
   Python: if i > 0 and nums[i] == nums[i - 1]: continue
   → Python 使用 and、or、not 代替 &&、||、!

4. 列表追加嵌套列表
   C++:  result.push_back({nums[i], nums[left], nums[right]});
   Python: result.append([nums[i], nums[left], nums[right]])
   → [] 创建列表字面量，append() 把整个三元组作为一个元素加入

5. 嵌套列表类型注解
   C++:  vector<vector<int>>
   Python: list[list[int]]
   → 外层 list 保存多个三元组，内层 list 保存整数
"""


def threeSum(nums: list[int]) -> list[list[int]]:
    """
    排序加双指针：固定一个数，在右侧区间寻找和为其相反数的两个数。
    时间复杂度 O(n²)，空间复杂度 O(1)（不计返回结果）
    """
    nums.sort()
    n = len(nums)
    result: list[list[int]] = []

    for i in range(n - 2):
        # 最小的固定值已经大于 0，后面不可能凑出 0
        if nums[i] > 0:
            break
        # 跳过重复的固定值
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])

                # 跳过重复的 left 和 right
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

    return result


# =============================================================================
# 测试代码
# =============================================================================
if __name__ == "__main__":
    result1 = threeSum([-1, 0, 1, 2, -1, -4])
    expected1 = [[-1, -1, 2], [-1, 0, 1]]
    assert sorted(result1) == sorted(expected1), f"示例1失败: {result1}"
    assert threeSum([0, 1, 1]) == [], "无解测试失败"
    assert threeSum([0, 0, 0]) == [[0, 0, 0]], "全0测试失败"
    print("✅ P06 三数之和 全部测试通过")
