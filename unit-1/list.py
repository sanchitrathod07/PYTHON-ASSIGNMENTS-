# -------------------------------
# List Operations in Python
# -------------------------------

# Creating a list
numbers = [10, 40, 20, 50, 30]
print("Initial List:", numbers)

# -------------------------------
# 1. Adding Elements
# -------------------------------

# Add element at the end
numbers.append(60)
print("After append:", numbers)

# Add element at a specific index
numbers.insert(2, 25)
print("After insert:", numbers)

# Add multiple elements
numbers.extend([70, 80])
print("After extend:", numbers)

# -------------------------------
# 2. Removing Elements
# -------------------------------

# Remove specific value
numbers.remove(40)
print("After remove:", numbers)

# Remove element by index
numbers.pop(3)
print("After pop:", numbers)

# Remove last element
numbers.pop()
print("After pop last:", numbers)

# Delete element using index
del numbers[0]
print("After del:", numbers)

# Clear entire list
temp_list = [1, 2, 3]
temp_list.clear()
print("After clear:", temp_list)

# -------------------------------
# 3. Modifying Elements
# -------------------------------

numbers[1] = 100
print("After modification:", numbers)

# -------------------------------
# 4. Sorting Elements
# -------------------------------

# Sort in ascending order
numbers.sort()
print("Sorted (Ascending):", numbers)

# Sort in descending order
numbers.sort(reverse=True)
print("Sorted (Descending):", numbers)

# -------------------------------
# 5. Reversing Elements
# -------------------------------

numbers.reverse()
print("Reversed List:", numbers)
