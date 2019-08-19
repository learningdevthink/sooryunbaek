number = input("정수 입력> ")
number = int(number)

if number % 2 == 0:
    print("짝수입니다")

else:
    print("홀수입니다")


import datetime
now = datetime.datetime.now()
month = now.month

if 3 <= month <= 5:
    print("현재는 봄입니다")
elif 6 <= month <= 8:
    print("현재는 여름입니다")
elif 9 <= month <= 11:
    print("현재는 가을입니다")
else:
    print("현재는 겨울입니다")

score = float(input("학점 입력>"))

if score == 4.5:
    print("신")
elif 4.2 <= score:
    print("상등신")


print("#if 조건문에 0넣기")
if 0:
    print("0은 true로 변환됩니다")
else:
    print("0은 false로 변환됩니다")
print()

print("#if 조건문에 빈 문자열 넣기")
if "":
    print("빈 문자열은 true로 변환됩니다")
else:
    print("빈 문자열은 false로 변환됩니다")




    