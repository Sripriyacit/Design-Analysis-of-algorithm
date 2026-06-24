arr = [62, 55, 8, 30, 80, 88, 50]  # Array with 7 elements
target = 30  # Fixed target element

found = False

for i in range(len(arr)):
    if arr[i] == target:
        print("Element found at index:", i)
        found = True
        break

if not found:
    print("Element not found")