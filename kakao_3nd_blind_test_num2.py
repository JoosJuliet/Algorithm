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
        if msg[0:i] in dictionary :
            key = msg[0:i]
            next_key = msg[i:i+1] if len(msg) > i+1 else ''
            ans.append(dictionary[key])
            if next_key is not '' and key+next_key not in dictionary :
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
