"""LeetCode 131. 分割回文串 (Palindrome Partitioning) — 字节真题
难度：中等
题目：把字符串分割成若干回文子串，返回所有分割方案。
示例："aab" → [["a","a","b"],["aa","b"]]
思路：中心扩展预处理回文区间，再回溯枚举分割方案。"""


def fun(s):
    """中心扩展 + 回溯。时间 O(n·2ⁿ)，空间 O(n²)。"""
    n = len(s)
    is_palindrome = [[False] * n for _ in range(n)]
    for i in range(n):
        left = right = i
        while left >= 0 and right < n and s[left] == s[right]:
            is_palindrome[left][right] = True
            left -= 1
            right += 1
        left, right = i, i + 1
        while left >= 0 and right < n and s[left] == s[right]:
            is_palindrome[left][right] = True
            left -= 1
            right += 1

    result = []
    path = []

    def backtrack(start):
        if start == n:
            result.append(path.copy())
            return
        for i in range(start, n):
            if is_palindrome[start][i]:
                path.append(s[start:i + 1])
                backtrack(i + 1)
                path.pop()

    backtrack(0)
    return result


if __name__ == "__main__":
    assert fun("aab") == [["a", "a", "b"], ["aa", "b"]], "示例1失败"
    assert fun("a") == [["a"]], "单字符测试失败"
    print("✅ P06 分割回文串 全部测试通过")
