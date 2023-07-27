def bf_match(txt: str, pat: str) -> int:

    pt = 0  # 검색되는 쪽의 문자열인 txt를 따라가는 커서
    pp = 0  # 찾아내는 문자열 인 pattern 을 따라가는 커서

    while pt != len(txt) and pp != len(pat): # 각자의 커서가 끝부분으로 도착하면 그만 둠
        if txt[pt] == pat[pp]: # 문자열끼리 일치할 경우, 다음 문자가 맞는지 확인
            pt += 1
            pp += 1
        else: # 문자끼리 일치 하지 않을 경우, 텍스트 커서 위치를 일치했던 순간 까지 이동시키고, 패턴의 커서는 맨 처음으로 이동시킴
            pt = pt - pp +1
            pp = 0

    # 패턴이 자신의 크기만큼 탐색을 했다면, 텍스트와 패턴이 완전 일치했다는 것
    #  텍스트 커서 현재 위치와 현재 패턴 위치를 빼면 맞는 텍스트위치를 알 수 있음
    return pt - pp if pp == len(pat) else -1 