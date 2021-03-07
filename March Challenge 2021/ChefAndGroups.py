<<<<<<< HEAD
'''
PROBLEM NAME : CHEF AND GROUPS
PROBLEM CODE : GROUPS

There are N seats in a row. You are given a string S with length N; 
for each valid i, the i-th character of S is '0' 
if the i-th seat is empty or '1' if there is someone sitting in that seat.

Two people are friends if they are sitting next to each other. 
Two friends are always part of the same group of friends. 
Can you find the total number of groups?
'''

# Contributed By - GORAKH GUPTA

# cook your dish here
n = int(input())
for _ in range(n):
    a = input()
    count = 0
    if a[0] == '1':
        count = count + 1
    for i in range(1, len(a)):
        if a[i] == '1' and a[i] != a[i-1]:
            count += 1
    print(count)