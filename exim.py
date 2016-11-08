import pandas as pd

def 수출입은행국제(경로):
    # 엑셀파일 읽기
    원본 = pd.read_excel(경로, skiprow=3, parse_cols="C:K", header=None)
    
    # 빈줄 정리
    원본 = 원본.dropna(how='all')
    #빈 줄 정리로 고르지 않은 색인 재설정
    원본 = 원본.reset_index(drop=True)
    
    # 표 잘라내기
    표범위목록 = 표범위추출(원본)
    표목록 = []
    for 범위 in 표범위목록:
        시작, 끝 = 범위
        # 표의 길이가 2보다 작으면 제외
        if 끝 - 시작 < 2:
            continue
        
        표 = 원본[시작:끝]                
        표 = 표.reset_index(drop=True)
        # 색인제목 추출
        색인제목 = 표.ix[0,0]
        # 열제목 추출
        열제목 = 표.ix[1, 1:]
        열제목.name = '' # 기존의 값
        # 색인과 열제목 설정
        표 = 표[2:].set_index(0)
        표.index.name = 색인제목
        표.columns = 열제목
        
        표목록.append(표)
    return 표목록

def 표범위추출(프레임):
    # 표범위 = [(0,9), (9,17), (17,25), (25,30), (30,45)]
    제목인가 = 프레임.notnull().sum(1) == 1
    시작지점 = list(프레임[제목인가].index)
    끝지점 = 시작지점[1:] + [len(프레임)]
    표범위 = list(zip(시작지점, 끝지점))
    return 표범위