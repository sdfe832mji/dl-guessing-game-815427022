def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
## I got this from w3schools.com
## (Link: https://www.w3schools.com/python/python_dsa_bubblesort.asp)

print('Welcome to my bubble sorter.')
print('Please enter your numbers seperated by comma.')
mylist = list(map(int,input('Enter your numbers separated by comma:').strip().split(',')))
print('I will now magically bubble sort this list.')
bubbleSort(mylist)
print(mylist)

