import sys

words = sys.stdin.readline().strip().upper()    # 대문자로 출력하기위해 전처리
unique_words = list(set(words))

cnt_list = []
for x in unique_words:
    cnt_list.append(words.count(x))

if cnt_list.count(max(cnt_list)) > 1:
    print("?")
else:
    max_idx = cnt_list.index(max(cnt_list))
    print(unique_words[max_idx])