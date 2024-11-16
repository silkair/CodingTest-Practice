T = int(input())
dic = {0:"ZRO" , 1:"ONE", 2:"TWO", 3:"THR", 4:"FOR", 5:"FIV", 6:"SIX", 7:"SVN", 8:"EGT", 9:"NIN"}

for test_case in range(1, T + 1):

    # 테스트 케이스 번호 입력 받기
    tc = input().split()
    # 단어 리스트 입력
    word = input().split()

    #for문을 이용해서 단어 리스트를 정렬 후 출력

    #출력 할 정답 리스트 초기화
    answer = []
    #ZRO 부터 NIN까지 순회
    for i in range(10):
        count = word.count(dic[i]) #딕셔너리 1 부터 10 까지 순회
        answer.append(count) #순회 한 후 벨류 값이 각각 몇번 입력 되었는지 정답 리스트에 넣기

    #결과 출력
    print(f"#{test_case}")
    for j in range(len(answer)):
        print((dic[j] + " ")*answer[j], end="")
    print()