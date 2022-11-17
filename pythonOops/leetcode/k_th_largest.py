class Solution:
    def find_kth_largest(self, nums, kth_index: int) -> int:
        nums.sort()
        max_num = max(nums)
        if kth_index == 0:
            return 0
        elif kth_index == 1:
            return max_num
        # for i in range(kth_index-1):
        #     nums.pop()
        #     max_num = max(nums)
        while kth_index-1:
            nums.pop()
            max_num = max(nums)
            kth_index -= 1

        return max_num


sol = Solution()
nums_lst = list()
result = 0
try:
    nums_lst = list(map(int, input().split()))
except ValueError as val_error:
    print(val_error)

k = int(input())
lst_filter = filter(lambda n: -10000 <= n <= 10000, nums_lst)
new_lst = list(lst_filter)
is_size_pass = lambda x: 1 <= x <= len(new_lst) <= 100000
if is_size_pass(k):
    result = sol.find_kth_largest(nums_lst, k)
if result != 0:
    print(result)
