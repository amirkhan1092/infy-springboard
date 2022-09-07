'''This problem was asked by Microsoft.

Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

2
1.5
2
3.5
2
2
2'''

def median(nums: list):
    nnums = sorted(nums)
    ln = len(nnums)
    if ln % 2:
        return nnums[ln // 2]
    else:
        return (nnums[ln // 2] + nnums[ln // 2 - 1] ) / 2


    #  n_num = [1, 2, 3, 4, 5]
# n = len(n_num)
# n_num.sort()
  
# if n % 2 == 0:
#     median1 = n_num[n//2]
#     median2 = n_num[n//2 - 1]
#     median = (median1 + median2)/2
# else:
#     median = n_num[n//2]
# print("Median is: " + str(median))       


lst = [1, 2, 5]

out = median(lst)
print(out)