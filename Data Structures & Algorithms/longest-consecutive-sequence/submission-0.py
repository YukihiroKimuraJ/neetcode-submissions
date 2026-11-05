class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        longest_streak = 0

        for num in num_set:
            # 連続列の「先頭」のときだけ数え始める
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                # 次の数が存在する間はカウントアップ
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                longest_streak = max(longest_streak, current_streak)

        return longest_streak