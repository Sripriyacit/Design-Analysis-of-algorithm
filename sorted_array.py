
arr = [45, 12, 78, 23, 9, 56, 31]

print("Original Array:", arr)

print("\nPress:")
choice = input("Enter your choice: ")

if choice== "1":
    arr.sort()
    print("Ascending Order:", arr)

elif choice == "2":
    arr.sort(reverse=True)
    print("Descending Order:", arr)

else:
    print("Invalid Choice!")