word = "asfasf"
guesses = ""
for char in word :
    #정답 단어 내에 추측 문자가 포함되어 있는 경우
    if char in guesses :
        # 추측 단어 출력
        print(char, end = "")
    else :
        # 기본, 틀린 경우 대시로 처리
        print("_", end = " ")

print("아톰을 사용해서 처음으로 깃허브 연동해봤당~~ 유후")
