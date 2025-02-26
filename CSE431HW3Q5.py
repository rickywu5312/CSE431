import timeit
import random
import matplotlib.pyplot as plt
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []


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

for i in range(10):
    list1.append(random.randint(1, 10))
for i in range(50):
    list2.append(random.randint(1, 50))
for i in range(100):
    list3.append(random.randint(1, 100))
for i in range(200):
    list4.append(random.randint(1, 200))
for i in range(300):
    list5.append(random.randint(1, 300))

l1 = list1.copy()
l2 = list2.copy()
l3 = list3.copy()
l4 = list4.copy()
l5 = list5.copy()


line1 = []
line2 = []
y = [10,50,100,200,300]
for i in (l1, l2, l3, l4, l5):
    start = timeit.default_timer()
    insertionsort(i.copy())
    line1.append(timeit.default_timer() - start)
    start = timeit.default_timer()
    mergesort(i.copy())
    line2.append(timeit.default_timer() - start)
plt.scatter(line1,y, label = "Insertion")
plt.scatter(line2,y, label = "Merge")
plt.xlabel("time in milliseconds")
plt.ylabel("amount of entries")
plt.title("Merge vs Insertion sort time difference")
plt.legend()
plt.show()
for i in range(5):
    print(y[i])
    print("Insertion:",line1[0])
    print("Merge:",line2[0])
