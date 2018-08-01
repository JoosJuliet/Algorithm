# 문제 http://tech.kakao.com/2017/11/14/kakao-blind-recruitment-round-3/

# msg = input()
# msg = 'KAKAO'
# msg = 'TOBEORNOTTOBEORTOBEORNOT'
msg = 'ABABABABABABABAB'
ans=[]
dictionary = {}

for i in range(26):
    t = ord('A') + i
    dictionary[chr(t)] = i+1

tmp = ''

while len(msg) is not 0:
    for i in range(len(msg)):
        i = len(msg) - i
        # 일부로 숫자가 큰 것 부터 본다. 짧은 것 부터 하면 각 알파벳의  안에 모든 경우의 수가 들어가기 때문이다.
        if msg[0:i] in dictionary :
            # 무조건 dictionary에 있는 것들만 들어가게 한다.
            # 어차피 뒤에 있는 것들은 앞에 있는 것들에 의해 dictionary에 무조건 들어가기 때문이다.
            key = msg[0:i]
            next_key = msg[i:i+1] if len(msg) > i+1 else ''
            # 다음 것이 마지막이면 ''로 보낸다
            ans.append(dictionary[key])
            # dictionary에 있는 index를 넣는다.
            if next_key is not '' and key+next_key not in dictionary :
                # 이어진 애가 없으면 dictionary에 넣는다.
                dictionary[key + next_key] = len(dictionary) + 1
            msg = msg[len(key):]
            break

print(len(ans),ans)

# print(len(dictionary),dictionary)
# print(len(ans), ans)
# answer = [11, 1, 27, 15]
# answer = [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
answer = [1, 2, 27, 29, 28, 31, 30]
for i in range(len(answer)):
    if ans[i] ==  answer[i]:
        print(i)
print('answer',len(answer), answer)
