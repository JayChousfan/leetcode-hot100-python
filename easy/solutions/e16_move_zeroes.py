"""LeetCode 283. 移动零 (Move Zeroes) — Hot 100
难度：简单
题目：原地把所有 0 移到数组末尾，并保持非零元素顺序。
示例：[0,1,0,3,12] → [1,3,12,0,0]
思路：用快慢指针交换非零元素。"""


def fun(nums):
    """slow/fast 原地交换。时间 O(n)，空间 O(1)。"""
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1


if __name__ == "__main__":
    nums1 = [0, 1, 0, 3, 12]
    fun(nums1)
    assert nums1 == [1, 3, 12, 0, 0], "示例1失败"
    print("✅ E16 移动零 全部测试通过")
