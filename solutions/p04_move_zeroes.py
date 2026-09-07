"""
============================================================
LeetCode 283. 移动零 (Move Zeroes) — Hot 100
============================================================
难度：简单

题目：给定一个数组 nums，编写函数将所有 0 移动到数组的末尾，
      同时保持非零元素的相对顺序。必须原地操作，不能拷贝数组。

示例：
  输入: nums = [0,1,0,3,12]
  输出: [1,3,12,0,0]

============================================================
Python 语法要点（C++ 对比）
============================================================

1. 列表长度
   C++:  nums.size()
   Python: len(nums)
   → len() 是内置函数，不是列表方法

2. 列表元素交换
   C++:  swap(nums[slow], nums[fast]);
   Python: nums[slow], nums[fast] = nums[fast], nums[slow]
   → Python 使用元组解包完成交换，不需要临时变量
   → 右侧先计算并打包，再依次赋值给左侧

3. range() 生成下标序列
   C++:  for (int fast = 0; fast < nums.size(); ++fast)
   Python: for fast in range(len(nums)):
   → range(n) 依次生成 0, 1, 2, ..., n - 1
   → fast 在这里是扫描指针，不是普通循环计数变量

4. 原地修改与返回值
   C++:  void moveZeroes(vector<int>& nums)
   Python: def moveZeroes(nums: list[int]) -> None:
   → Python 列表是可变对象，函数内修改会影响外部
   → 返回类型标注为 None，表示函数不返回结果

5. 切片
   C++:  需要使用迭代器指定范围
   Python: nums[0:3] / nums[:] / nums[::-1]
   → 切片采用左闭右开区间；省略边界可复制或反转整个列表
"""


def moveZeroes(nums: list[int]) -> None:
    """
    双指针交换：slow 指向下一个非零元素应该放置的位置。
    时间复杂度 O(n)，空间复杂度 O(1)
    """
    slow = 0

    for fast in range(len(nums)):
        if nums[fast] != 0:
            # 将非零元素交换到 slow 指向的位置
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1


# =============================================================================
# 测试代码
# =============================================================================
if __name__ == "__main__":
    nums1 = [0, 1, 0, 3, 12]
    moveZeroes(nums1)
    assert nums1 == [1, 3, 12, 0, 0], f"示例1失败: {nums1}"
    nums2 = [0]
    moveZeroes(nums2)
    assert nums2 == [0], f"单0测试失败: {nums2}"
    nums3 = [1, 2, 3]
    moveZeroes(nums3)
    assert nums3 == [1, 2, 3], f"无0测试失败: {nums3}"
    print("✅ P04 移动零 全部测试通过")
