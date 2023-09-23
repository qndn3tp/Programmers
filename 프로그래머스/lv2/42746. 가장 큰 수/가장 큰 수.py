def solution(numbers):
    # 사전 순으로 정렬하기위해 문자 리스트로 변경
    numbers = list(map(str, numbers))
    # 끝자리가 0인 수 처리 -> 숫자를 2번 반복해서 해결
    numbers.sort(key = lambda x: x * 3, reverse=True)
    
    # 원소가 0뿐인 경우
    if numbers[0] == "0":
        return "0"
    return "".join(numbers)