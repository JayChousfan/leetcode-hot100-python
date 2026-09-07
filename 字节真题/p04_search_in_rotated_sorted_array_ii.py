"""LeetCode 81. 搜索旋转排序数组 II (Search in Rotated Sorted Array II) — 字节真题
难度：中等
题目：判断可能含重复元素的旋转排序数组中是否存在 target。
示例：[2,5,6,0,0,1,2], target=0 → True
思路：二分判断有序区间，三端相等时同时收缩边界。"""


def fun(nums, target):
    """二分查找。平均时间 O(log n)，最坏 O(n)，空间 O(1)。"""
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return True
        if nums[left] == nums[mid] == nums[right]:
            left += 1
            right -= 1
        elif nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return False


if __name__ == "__main__":
    assert fun([2, 5, 6, 0, 0, 1, 2], 0), "示例1失败"
    assert not fun([2, 5, 6, 0, 0, 1, 2], 3), "不存在测试失败"
    print("✅ P04 搜索旋转排序数组 II 全部测试通过")
