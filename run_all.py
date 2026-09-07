"""一键运行 solutions/ 下的全部题目。"""

from pathlib import Path
import os
import subprocess
import sys


PROBLEMS = [
    ("p01_two_sum.py", "1", "两数之和"),
    ("p02_group_anagrams.py", "49", "字母异位词分组"),
    ("p03_longest_consecutive.py", "128", "最长连续序列"),
    ("p04_move_zeroes.py", "283", "移动零"),
    ("p05_container_with_most_water.py", "11", "盛最多水的容器"),
    ("p06_three_sum.py", "15", "三数之和"),
    ("p07_longest_substring_without_repeating.py", "3", "无重复字符的最长子串"),
    ("p08_subarray_sum_equals_k.py", "560", "和为K的子数组"),
    ("p09_maximum_subarray.py", "53", "最大子数组和"),
    ("p10_merge_intervals.py", "56", "合并区间"),
    ("p11_reverse_linked_list.py", "206", "反转链表"),
    ("p12_linked_list_cycle.py", "141", "环形链表"),
    ("p13_binary_tree_inorder_traversal.py", "94", "二叉树的中序遍历"),
    ("p14_unique_paths.py", "62", "不同路径"),
    ("p15_combination_sum.py", "39", "组合总和"),
    ("p16_daily_temperatures.py", "739", "每日温度"),
    ("p17_kth_largest_element.py", "215", "数组中的第K个最大元素"),
    ("p18_search_in_rotated_sorted_array.py", "33", "搜索旋转排序数组"),
    ("p19_number_of_islands.py", "200", "岛屿数量"),
    ("p20_decode_string.py", "394", "字符串解码"),
]


def main() -> None:
    solutions_dir = Path(__file__).parent / "solutions"
    failed: list[str] = []
    environment = os.environ.copy()
    environment["PYTHONIOENCODING"] = "utf-8"
    sys.stdout.reconfigure(encoding="utf-8")

    for filename, problem_id, title in PROBLEMS:
        print(f"\n▶ LeetCode {problem_id}. {title}", flush=True)
        result = subprocess.run(
            [sys.executable, str(solutions_dir / filename)],
            env=environment,
        )
        if result.returncode != 0:
            failed.append(filename)

    if failed:
        print(f"\n❌ 运行失败: {', '.join(failed)}")
        raise SystemExit(1)

    print(f"\n🎉 全部 {len(PROBLEMS)} 道题测试通过")


if __name__ == "__main__":
    main()
