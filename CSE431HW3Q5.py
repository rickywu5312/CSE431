import timeit
import random
import matplotlib.pyplot as plt
list1 = []
list2 = []


def merge(left, right):
    result = []
    i ,j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

#source: https://stackoverflow.com/questions/10502533/explanation-of-merge-sort-for-dummies
def mergesort(list):
    if len(list) < 2:
        return list
    middle = len(list) // 2
    left = mergesort(list[:middle])
    right = mergesort(list[middle:])
    return merge(left, right)

#source: https://stackoverflow.com/questions/12755568/how-does-python-insertion-sort-work
def insertionsort(s):
    for i in range(1, len(s)):
        val = s[i]
        j = i - 1
        while (j >= 0) and (s[j] > val):
            s[j+1] = s[j]
            j = j - 1
        s[j+1] = val

line1 = []
line2 = []
y = []
count = 1
for i in range(0,300,5):
    y.append(i)
    for j in range(i):
        list1.append(random.randint(0,100000))
    start = timeit.default_timer()
    insertionsort(list1.copy())
    line1.append(timeit.default_timer() - start)
    start = timeit.default_timer()
    mergesort(list1.copy())
    line2.append(timeit.default_timer() - start)
    list1 = []
    if line1[int(i/5)] < line2[int(i/5)]:
        count = i
plt.plot(line1,y, label = "Insertion")
plt.plot(line2,y, label = "Merge")
plt.axhline(y = count)
plt.xlabel("time in milliseconds")
plt.ylabel("amount of entries")
plt.title("Merge vs Insertion sort time difference")
plt.legend()
plt.show()
