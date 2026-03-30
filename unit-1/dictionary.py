# Dictionary operations

# Create dictionary
student = {"name": "Sanchit", "age": 18}

# Access elements
print("Name:", student["name"])

# Update dictionary
student["age"] = 18

# Add new element
student["course"] = "CSE"

# Remove element
student.pop("age")

# Merge dictionaries
extra = {"city": "Pune"}
student.update(extra)

print("Final dictionary:", student)
