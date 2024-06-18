for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a. Count in 10s from 0 to 100
print("a. Count in 10s from 0 to 100:")
for i in range(0, 101, 10):
    print(i, end=' ')
print("\n")

# b. Count down from 20 to 1
print("b. Count down from 20 to 1:")
for i in range(20, 0, -1):
    print(i, end=' ')
print("\n")

# c. Print n stars
n = int(input("Enter the number of stars: "))
print("c. Print", n, "stars:")
for _ in range(n):
    print("*", end=' ')
print("\n")