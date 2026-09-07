"""LeetCode 88. 合并两个有序数组 (Merge Sorted Array) — 字节真题
难度：简单
题目：把 nums2 合并到 nums1 中，使 nums1 仍然有序。
示例：nums1=[1,2,3,0,0,0], nums2=[2,5,6] → [1,2,2,3,5,6]
思路：从后向前放较大的数，避免覆盖 nums1 的有效元素。"""


def fun(nums1, m, nums2, n):
    """逆向双指针。时间 O(m+n)，空间 O(1)。"""
    i, j, right = m - 1, n - 1, m + n - 1
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[right] = nums1[i]
            i -= 1
        else:
            nums1[right] = nums2[j]
            j -= 1
        right -= 1


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    fun(nums1, 3, [2, 5, 6], 3)
    assert nums1 == [1, 2, 2, 3, 5, 6], "示例1失败"
    print("✅ P03 合并两个有序数组 全部测试通过")
