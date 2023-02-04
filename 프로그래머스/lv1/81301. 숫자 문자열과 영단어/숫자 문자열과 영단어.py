def solution(s):
    table =  ["zero", "one", "two", "three", "four", 
          "five", "six", "seven", "eight", "nine"]

    answer = ""
    word = ""
    for i in range(len(s)):
        # 숫자일 경우
        if s[i].isdigit():
            answer += s[i]
            continue
            
        # 문자일 경우
        elif s[i].isalpha():
            word += s[i]

        # 숫자 단어가 만들어졌는지 판단
        if word in table:
            answer += str(table.index(word))
            word = ""
    
    return int(answer)