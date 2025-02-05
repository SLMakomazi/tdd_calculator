from calculator import add, multiply

# Test addition
print("Addition Examples:")
print(f"1 + 2 = {add(1, 2)}")
print(f"-1 + (-1) = {add(-1, -1)}")
print(f"1 + 2 + 3 + 4 + 5 = {add(1, 2, 3, 4, 5)}")

print("\nMultiplication Examples:")
print(f"1 × 3 = {multiply(1, 3)}")
print(f"-1 × 3 = {multiply(-1, 3)}")
print(f"1 × 2 × 3 × 4 × 5 = {multiply(1, 2, 3, 4, 5)}")
