"""
============================================================
LeetCode 49. 字母异位词分组 (Group Anagrams) — Hot 100
============================================================
难度：中等

题目：给你一个字符串数组，请你将字母异位词组合在一起。
      字母异位词是字母相同但排列不同的字符串。
      可以按任意顺序返回结果列表。

示例：
  输入: strs = ["eat","tea","tan","ate","nat","bat"]
  输出: [["bat"],["nat","tan"],["ate","eat","tea"]]

============================================================
Python 语法要点（C++ 对比）
============================================================

1. 字符串排序
   C++:  sort(s.begin(), s.end());
   Python: sorted(s) → 返回排序后的字符列表
           "".join(sorted(s)) → 转回字符串
   → sorted() 返回新列表，不修改原对象
   → "".join(list) 把字符列表直接拼接成字符串

2. defaultdict 对应带默认值的哈希表
   C++:  unordered_map<string, vector<string>> mp;
   Python: mp = defaultdict(list)
   → 访问不存在的 key 时会自动创建空 list，省去手动判断

3. 列表追加
   C++:  result.push_back(s);
   Python: result.append(s)
   → Python 使用 append() 向列表末尾追加一个元素

4. 字典的 values()
   C++:  需要遍历哈希表并手动收集每个 value
   Python: list(mp.values())
   → values() 返回所有值的视图，用 list() 转换为列表

5. 类型注解中的嵌套泛型
   C++:  vector<vector<string>>
   Python: list[list[str]]
   → Python 3.9+ 支持直接嵌套内置容器类型
"""

from collections import defaultdict


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    """
    排序法：将每个字符串排序后的结果作为 key，把异位词分到同一组。
    时间复杂度 O(n * k log k)，空间复杂度 O(nk)
    """
    mp: defaultdict[str, list[str]] = defaultdict(list)

    for s in strs:
        # 异位词排序后会得到相同的字符串
        key = "".join(sorted(s))
        mp[key].append(s)

    return list(mp.values())


# =============================================================================
# 测试代码
# =============================================================================
if __name__ == "__main__":
    result = groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    sorted_result = sorted([sorted(g) for g in result])
    expected = [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
    assert sorted_result == expected, f"示例1失败: {sorted_result}"
    assert groupAnagrams([""]) == [[""]], "空字符串测试失败"
    assert groupAnagrams(["a"]) == [["a"]], "单字符测试失败"
    print("✅ P02 字母异位词分组 全部测试通过")
