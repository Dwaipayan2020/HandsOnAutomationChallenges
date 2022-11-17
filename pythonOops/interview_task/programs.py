"""Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
"""

"""Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted."""

# nums1 = [1, 2, 2, 1]
# nums2 = [2, 2]
# lst = list()
# for i in nums2:
#
#     for j in nums1:
#         if i == j:
#             lst.append(i)
# print(list(set(lst)))


nums2 = [9, 4, 9, 8, 4]
nums1 = [4, 9, 5]
lst = list()
for i in nums1:

    for j in nums2:
        if i == j:
            lst.append(i)
# print(list(set(lst)))
# print(lst)
fltr = lambda x: x == x + 1
rdc  = lambda x : set(x)
nwlst = list()
for item in lst:
    if filter(fltr(item), lst):
        nwlst.append(item)
print(nwlst)
