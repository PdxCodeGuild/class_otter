nums = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

peak_nums = []


def get_the_peaks(numbers):
    for i in range(1, len(numbers)-1):
        if numbers[i] > numbers[i + 1] and numbers[i] > numbers[i - 1]:
            peak_nums.append(i)
    return peak_nums


peaks = get_the_peaks(nums)
# print(get_the_peaks(nums))


valley_nums = []


def get_the_valleys(nums):
    for i in range(1, len(nums)-1):
        if nums[i] < nums[i + 1] and nums[i] < nums[i-1]:
            valley_nums.append(i)
    return valley_nums
# print(get_the_valleys)


valleys = get_the_valleys(nums)

peaks.extend(valleys)
peaks_valleys = peaks
peaks_valleys.sort()
print(peaks_valleys)
