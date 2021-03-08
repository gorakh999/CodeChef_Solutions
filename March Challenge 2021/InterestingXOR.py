'''
You are given an integer C. Let d be the smallest integer 
such that 2d is strictly greater than C.

Consider all pairs of non-negative integers 
(A,B) such that A,B<2d and A⊕B=C (⊕ denotes the bitwise XOR operation). 
Find the maximum value of A⋅B over all these pairs.
'''
# import math
# def next_num(n):
#     pos = math.ceil(math.log2(n))
#     return int(math.pow(2, pos))

# a = int(input())
# for i in range(a):
#     n = int(input())
#     product = 1
#     rst = next_num(n)
#     for i in range(1, rst+1):
#         for j in range(1, rst+1):
#             if i ^ j == n:
#                 if i * j > product:
#                     product = i * j
#     print(product)

# print(l1)
import math
a = int(input())
sum1 = 0
k = 1
while (a >= sum1):
    sum1 = math.pow(2, k)
    k = k + 1
print(k)
j = math.pow(2, k-1)
v1 = sum1 - a
rst = (j-1) * ((j-1) * v1)
print(rst)