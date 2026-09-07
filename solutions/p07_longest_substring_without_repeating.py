"""
============================================================
LeetCode 3. 无重复字符的最长子串 (Longest Substring Without Repeating Characters) — Hot 100
============================================================
难度：中等

题目：给定一个字符串 s，请找出其中不含重复字符的最长子串的长度。
      子串必须是原字符串中连续的一段字符。

示例：
  输入: s = "abcabcbb"
  输出: 3
  解释: 最长无重复字符子串是 "abc"

============================================================
Python 语法要点（C++ 对比）
============================================================

1. 字符串可以直接迭代
   C++:  for (char ch : s)
   Python: for char in s:
   → 每次循环得到长度为 1 的字符串

2. 字典记录字符最后位置
   C++:  unordered_map<char, int> char_map;
   Python: char_map: dict[str, int] = {}
   → 字符串可以直接作为字典的 key

3. enumerate() 指定起始下标
   C++:  for (int right = 0; right < s.size(); ++right)
   Python: for right, char in enumerate(s):
   → enumerate() 默认从 0 开始，也可以传入第二个参数指定起点

4. 字典元素更新
   C++:  char_map[ch] = right;
   Python: char_map[ch] = right
   → 重复赋值会覆盖旧位置，始终保存字符最后一次出现的下标
"""


def lengthOfLongestSubstring(s: str) -> int:
    """
    滑动窗口：left 指向无重复窗口左边界，字典记录字符最后出现位置。
    时间复杂度 O(n)，空间复杂度 O(k)，k 为字符集大小
    """
    char_map: dict[str, int] = {}
    left = 0
    max_len = 0

    for right, ch in enumerate(s):
        # 重复字符位于当前窗口内时，收缩左边界
        if ch in char_map and char_map[ch] >= left:
            left = char_map[ch] + 1

        char_map[ch] = right
        max_len = max(max_len, right - left + 1)

    return max_len


# =============================================================================
# 测试代码
# =============================================================================
if __name__ == "__main__":
    assert lengthOfLongestSubstring("abcabcbb") == 3, "示例1失败"
    assert lengthOfLongestSubstring("bbbbb") == 1, "重复字符测试失败"
    assert lengthOfLongestSubstring("") == 0, "空字符串测试失败"
    print("✅ P07 无重复字符的最长子串 全部测试通过")
