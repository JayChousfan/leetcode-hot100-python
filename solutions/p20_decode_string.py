"""
============================================================
LeetCode 394. 字符串解码 (Decode String) — Hot 100
============================================================
难度：中等

题目：给定一个经过编码的字符串，编码规则为 k[encoded_string]，表示方括号
      内部的字符串重复 k 次。返回解码后的字符串，输入保证格式有效。

示例：
  输入: s = "3[a2[c]]"
  输出: "accaccacc"

============================================================
Python 语法要点（C++ 对比）
============================================================

1. str.isdigit() 与 str.isalpha()
   C++:  isdigit(ch) / isalpha(ch)
   Python: char.isdigit() / char.isalpha()
   → 字符串方法直接判断字符类别，无需导入 cctype

2. nonlocal 闭包变量
   C++:  lambda 用 [&i] 捕获并修改外层下标
   Python: nonlocal i
   → 内层函数要给外层变量重新赋值时，必须先声明 nonlocal

3. str.join() 高效拼接
   C++:  循环向 string 追加各片段
   Python: "".join(parts)
   → join() 一次合并字符串列表，避免反复创建中间字符串

4. 字符串乘法
   C++:  循环 k 次追加 sub_str
   Python: sub_str * current_num
   → 字符串乘整数会得到重复指定次数的新字符串

5. ord() 与 chr()
   C++:  int code = ch; char ch = code;
   Python: ord(ch) / chr(code)
   → ord() 把字符转为 Unicode 码点，chr() 执行反向转换；本题用 int(char) 更直接
"""


def decodeString(s: str) -> str:
    """
    递归解析每层方括号；共享 i 保证每个字符只处理一次。
    时间复杂度 O(n + output)，空间复杂度 O(depth + output)
    """
    i = 0

    def parse() -> str:
        nonlocal i
        result: list[str] = []

        while i < len(s) and s[i] != "]":
            if s[i].isalpha():
                result.append(s[i])
                i += 1
                continue

            current_num = 0
            while i < len(s) and s[i].isdigit():
                current_num = current_num * 10 + int(s[i])
                i += 1

            # 跳过左方括号，递归解析内部字符串
            i += 1
            sub_str = parse()
            # 跳过右方括号
            i += 1
            result.append(sub_str * current_num)

        return "".join(result)

    return parse()


# =============================================================================
# 测试代码
# =============================================================================
if __name__ == "__main__":
    result1 = decodeString("3[a2[c]]")
    assert result1 == "accaccacc", f"示例1失败: {result1}"
    assert decodeString("3[a]2[bc]") == "aaabcbc", "并列编码测试失败"
    assert decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef", "混合字符串测试失败"
    print("✅ P20 字符串解码 全部测试通过")
