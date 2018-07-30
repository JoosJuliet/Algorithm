# n = 2 # 진법
# t = 4 # 구해야할 숫자 개수
# m = 2 # 게임 참여 인원
# p = 1 # 튜브 순서
# n = 16 # 진법
# t = 16 # 구해야할 숫자 개수
# m = 2 # 게임 참여 인원
# p = 1 # 튜브 순서
n = 16 # 진법
t = 16 # 구해야할 숫자 개수
m = 2 # 게임 참여 인원
p = 2 # 튜브 순서
answer = []
number = []
convert_number_to_alphabet ={
    '10' : 'A',
    '11' : 'B',
    '12' : 'C',
    '13' : 'D',
    '14' : 'E',
    '15' : 'F'
}

upper_num = 1000000
boundary = t*m+p
for num in range(upper_num):
    if len(answer) > boundary:
        break
    else:
        while num > 0 :
            remainder = num % n
            if remainder >= 10 :

                remainder = convert_number_to_alphabet[str(remainder)]
            number.append(remainder)
            num = num // n
        number.reverse()
        answer += number
        number = []

answer = [0] + answer
# 처음 0 때문에 이런다.
# print('answer', answer)

tube_answer = []
for i in range(0, t):
    order = i * m + p - 1
    #  -1한다 index니까
    tube_answer.append(answer[order])

print('tube_answer',tube_answer)
# print('0111')
# print('02468ACE11111111')
# print('13579BDF01234567')


#문제 url http://tech.kakao.com/2017/11/14/kakao-blind-recruitment-round-3/
