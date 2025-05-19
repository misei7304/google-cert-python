# 모듈 2 - 기본 Python 구문 평가 문제 정리

# 문제 1: IP 주소와 호스트 이름을 문자열로 연결
IP_address = "192.168.1.10"
host_name = "Printer Server 1"
print(IP_address + " is the IP address of " + host_name)

# 문제 2: 대소문자 비교는 False
expression_result = "blue" == "Blue"
print("문제 2 결과:", expression_result)  # False

# 문제 3: 조건문 분기
number = 4
if number * 4 < 15:
    print(number / 4)
elif number < 5:
    print(number + 3)
else:
    print(number * 2 % 5)

# 문제 4: 성적 판별 함수
def exam_grade(score):
    if score >= 95:
        grade = "Top Score"
    elif score >= 60:
        grade = "Pass"
    else:
        grade = "Fail"
    return grade

# 문제 5: 조건문 간단 연습
test_num = 12
if test_num > 15:
    print(test_num / 4)
else:
    print(test_num + 3)

# 문제 6: 문자 변환 함수
def letter_translator(letter):
    if letter == "a":
        letter_position = 1
    elif letter == "b":
        letter_position = 2
    elif letter == "c":
        letter_position = 3
    elif letter == "d":
        letter_position = 4
    else:
        letter_position = "unknown"
    return letter_position

# 문제 7: 함수로 차이 계산
def difference(x, y):
    z = x - y
    return z
print(difference(5, 3))  # 2

# 문제 8: 논리 연산식 결과
logic_result = (10 >= 5*2) and (10 <= 5*2)
print("문제 8 결과:", logic_result)  # True

# 문제 9: 0으로 나누기 방지 함수
def safe_division(numerator, denominator):
    if denominator == 0:
        result = 0.0
    else:
        result = numerator / denominator
    return result

# 문제 10: 명확한 코드 = Clear code 또는 Readable code

