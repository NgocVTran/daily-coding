# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]


nums = [8, 1, 2, 2, 3]

# sorted list - increasing
sorted_nums = sorted(nums)

# save position of number in sorted to a dict,
# so the number of smaller number in original list
# is just the position's number in sorted list
position_nr = {}
for i in range(len(sorted_nums)):
    # save position number in sorted list
    if sorted_nums[i] not in position_nr:
        position_nr.update({
            # number i-te in sorted list is in position nr i
            sorted_nums[i]: i,
        })

# now, number of smaller numbers than current position is
for i in range(len(nums)):
    nums[i] = position_nr[nums[i]]

print(nums)

