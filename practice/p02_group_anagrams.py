"""
============================================================
LeetCode 49. 字母异位词分组 (Group Anagrams) — Hot 100
============================================================
难度：中等

将字符串数组中的字母异位词分到同一组，可以按任意顺序返回。

示例：
  输入: strs = ["eat","tea","tan","ate","nat","bat"]
  输出: [["bat"],["nat","tan"],["ate","eat","tea"]]

要求：
  - 函数名: groupAnagrams
  - 参数: strs，字符串数组，list[str]
  - 返回值: 分组结果，list[list[str]]
============================================================
"""

# TODO: 在这里写出完整的 def groupAnagrams(...): 函数


# =============================================================================
# 测试（不要修改）
# =============================================================================
if __name__ == "__main__":
    result = groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    sorted_result = sorted([sorted(g) for g in result])
    expected = [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
    assert sorted_result == expected, f"示例1失败: {sorted_result}"
    assert groupAnagrams([""]) == [[""]], "空字符串测试失败"
    print("✅ P02 字母异位词分组 通过！")
