from Math_Operations import basic_operations, power_operations,apply_operations
result = basic_operations(8, 4)
print(result) # The results will be displayed in a dictionary format
result = power_operations(6,3)
print(result)
result = power_operations(6,3,modulus=5)
print(result)
operations = [(lambda x,y: x+y , (1,5)), (lambda x,y: x-y, (8,3))]
result = apply_operations(operations)
print(result)