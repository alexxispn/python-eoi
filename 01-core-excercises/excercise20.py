v1 = [4, 3, 8, 1]
v2 = [9, 2, 7, 3]
scale_product = 0
for op1, op2 in zip(v1, v2):
    scale_product += op1 * op2

print(scale_product)
