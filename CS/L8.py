# BÀI 11

def sum_of_unique_elements(nums1):
    count = {}
    sum = 0
    for num in nums1:
        if num in count:
            count[num] += 1
        else: 
            count[num] = 1
    for x in count:
        if count[x] == 1:
            sum += x
    return sum

nums1 = [1,5,7,4,5]
print('Bài 11: List: ', nums1)
print(sum_of_unique_elements(nums1))

#BAI 21

def number_of_good_pairs(nums2):
    count = {}
    occ = 0
    for num in nums2:
        if num in count:
            count[num] += 1
        else: 
            count[num] = 1
    for x in count:
        if count[x] > 1:
            occ += (count[x] * (count[x]-1))/2
    return int(occ)

nums2 = [1,2,3,1,1,3,2,2,1]
print('Bài 21: List: ', nums2)
print(number_of_good_pairs(nums2))

#BAI 22

def contains_duplicate(nums3):
    count = {}
    dup = True
    for num in nums3:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    for x in count:
        if count[x] != 1:
            dup = False
            break
    return dup

nums3 = [1,2,3]
print('Bài 22: List: ', nums3)
print(contains_duplicate(nums3))




