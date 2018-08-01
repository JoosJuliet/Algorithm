msg = 'KAKAO'

d = {}

for i in range(26):
    t = ord('A') + i
    d[chr(t)] = i+1

answer = []
w = ''
j = 0

while True:
    w = msg[j]
    # print('w', w, j)
    while j<len(msg) and w in d:
        j += 1
        # j를 여기서 더했기 때문에 이 전의 것에서 다음 것을 처리하면 그 것을 여기서 뛰어넘을 수 있다.
        if j < len(msg):
            w += msg[j]
            # 글자가 늘어난다.
    if j>=len(msg):
        if w in d:
            print('d[w]',d[w])
            answer.append(d[w])
        break

    d[w] = len(d) + 1
    tmp = d[w[:-1]]
    answer.append(tmp)
    print('w[:-1] : ', w[:-1], 'w : ', w)

print(answer)
