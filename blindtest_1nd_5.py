from collections import defaultdict, Counter
import re
# str1 = 'aa1+aa2'.upper()
# str2 = 'AAAA12'.upper()

str1 = 'aaa1+aa2'.upper()
str2 = 'AAAA'.upper()


# str1 = 'handshake'.upper()
# str2 = 'shake hands'.upper()

# str1 = 'E=M*C^2'.upper()
# str2 = 'e=m*c^2'.upper()

def make_list(str):
    str_list = []
    str_set = set()
    for _ in range(len(str)-1):
        tmp = str[0:2]
        str = str[1:]
        if bool(re.search(r'[^a-zA-Z]+', tmp)) is False :
            str_list.append(tmp)
            str_set.add(tmp)
    return str_list, str_set

str1_list, str1_set = make_list(str1)
str2_list, str2_set = make_list(str2)

duplicated_element = str1_set & str2_set

up = down = count = 0
tmp1 = Counter(str1_list)
tmp2 = Counter(str2_list)

for i in duplicated_element:
    tmp1_count = tmp1[i]
    tmp2_count = tmp2[i]
    if tmp1_count is not 1 or tmp2_count is not 1 :
        up += min(tmp1_count, tmp2_count)
        down += max(tmp1_count, tmp2_count)
        count += 1

up += (len(str2_set & str1_set) - count)
down += (len(str2_set | str1_set) - count)

print(up, down)
if down is 0 :
    print('65536')
else:
    print(int(up / float(down) * 65536))

import re
from collections import defaultdict

str1 = 'E=M*C^2'.upper()
str2 = 'E=M*C^2'.upper()

def get_dict(s):
    d = defaultdict(int)
    for i in range(len(s)-1):
        c = s[i:i+2]
        if bool(re.search('[^a-zA-Z]', c)) is False:
            d[c] += 1
    return d

d1 = get_dict(str1)
d2 = get_dict(str2)

u = n = 0

for key in d1:
    if key in d2:
        n += min(d1[key], d2[key])
        u += max(d1[key], d2[key])
    else:
        u += d1[key]

for key in d2:
    if key not in d1:
        u += d2[key]

print( int((n / float(u))*65536) if u != 0 else 65536)
