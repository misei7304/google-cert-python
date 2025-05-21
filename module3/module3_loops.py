# 문제 1
number = 1
while number <= 7:
    print(number, end=" ")
    number += 1
print("\n")

# 문제 2
for number in range(5, -1, -1):
    print(number)
print("\n")

# 문제 3
def even_numbers(n):
    count = 0
    current_number = 0
    while current_number <= n:
        if current_number % 2 == 0:
            count += 1
        current_number += 1
    return count

print(even_numbers(25))
print(even_numbers(144))
print(even_numbers(1000))
print(even_numbers(0))
print("\n")

# 문제 4
def sequence(low, high):
    for x in range(2):
        for y in range(high, low - 1, -1):
            if y == low:
                print(str(y))
            else:
                print(str(y), end=", ")

sequence(1, 3)
print("\n")

# 문제 5
def counter(start, stop):
    if start > stop:
        return_string = "Counting down: "
        while start >= stop:
            return_string += str(start)
            if start > stop:
                return_string += ","
            start -= 1
    else:
        return_string = "Counting up: "
        while start <= stop:
            return_string += str(start)
            if start < stop:
                return_string += ","
            start += 1
    return return_string

print(counter(1, 10))
print(counter(2, 1))
print(counter(5, 5))
print("\n")

# 문제 6
def even_numbers_string(maximum):
    return_string = ""
    for x in range(2, maximum + 1, 2):
        return_string += str(x) + " "
    return return_string.strip()

print(even_numbers_string(6))
print(even_numbers_string(10))
print(even_numbers_string(3))
print(even_numbers_string(2))
print(even_numbers_string(0))
print("\n")

# 문제 7
x = 1
sum = 5
while x <= 10:
    sum += x
    x += 1
print(sum)
print("\n")
# 답: SUM 변수가 잘못된 VALUE로 초기화되었습니다 (sum = 0으로 해야 함)

# 문제 8
for sum in range(5):
    sum += sum
    print(sum)
# 답: 5

print("\n")

# 문제 9
for outer_loop in range(2, 7):
    for inner_loop in range(outer_loop):
        if inner_loop % 2 == 0:
            print(inner_loop)
# 답: 2

print("\n")

# 문제 10
def count_to_ten():
    x = 1
    while x <= 10:
        print(x)
        x += 1  # 반드시 증가시켜야 함

count_to_ten()
# 답: 변수 x는 루프에서 증가하지 않습니다