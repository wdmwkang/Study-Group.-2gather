import random 

# --------------------------------------------
# 1. max / min 구현하기 
#
# cmp라는 함수를 이용한 min/max 구현하기. 
# cmp는 두 원소 중 더 큰 것을 반환하는 함수. 
# --------------------------------------------

def cmp(x, y):
    if x < y:
        return -1
    elif x > y:
        return 1
    else:
        return 0

def my_max(lst, cmp):
    max_val = lst[0]
    for item in lst[1:]:
        if cmp(item, max_val) > 0:  # item이 max_val보다 크면 max_val을 item으로 갱신
            max_val = item
    return max_val

def my_min(lst, cmp):
    min_val = lst[0]
    for item in lst[1:]:
        if cmp(item, min_val) < 0:  # item이 min_val보다 작으면 min_val을 item으로 갱신
            min_val = item
    return min_val

# 테스트 예시
lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(my_max(lst, cmp))  # 출력: 9
print(my_min(lst, cmp))  # 출력: 1


# --------------------------------------------
# 2. sort 구현하기 
# 
# 1) 그냥 순서대로 오름차순으로 정렬하기 
# 2) 오름차순, 내림차순으로 정렬하기 
# 3) 주어진 기준 cmp에 맞춰서 오름차순, 내림차순으로 정렬하기 
# 4) 주어진 기준 cmp가 큰 element를 출력하거나, 같다는 결과를 출력하게 만들기 
# 5) cmp상 같은 경우 tie-breaking하는 함수 넣기
# --------------------------------------------

def sort1(lst):
    sorted_lst = sorted(lst)
    print(sorted_lst)

sort1(lst)

def sort2(lst, upper_to_lower=True):
    # upper_to_lower가 True일 때는 오름차순, False일 때는 내림차순
    return sorted(lst, reverse=not upper_to_lower)

# 테스트 예시
lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# 오름차순 정렬
print(sort2(lst, upper_to_lower=True))  # 출력: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

# 내림차순 정렬
print(sort2(lst, upper_to_lower=False))  # 출력: [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]

from functools import cmp_to_key

def sort3(lst, upper_to_lower=True, cmp=lambda x, y: x):
    # cmp 함수에 따라 오름차순 또는 내림차순 정렬을 수행하는 함수
    def custom_cmp(x, y):
        # upper_to_lower가 True면 오름차순, False면 내림차순
        result = cmp(x, y)
        return result if upper_to_lower else -result

    # cmp_to_key로 cmp 함수를 key로 변환하여 sorted에 전달
    return sorted(lst, key=cmp_to_key(custom_cmp))

# 테스트 예시
lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# 기본 cmp 함수를 사용하는 경우
print(sort3(lst, upper_to_lower=True))  # 오름차순 정렬, 출력: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
print(sort3(lst, upper_to_lower=False))  # 내림차순 정렬, 출력: [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]

# 커스텀 cmp 함수를 사용하는 경우 (예: 절대값 기준으로 정렬)
print(sort3([-3, 1, -4, 1, 5, -9, 2, 6, 5, -3, 5], upper_to_lower=True, cmp=lambda x, y: abs(x) - abs(y)))
# 출력: [1, 1, 2, -3, -3, 5, 5, 5, -4, 6, -9]


def sort4(lst, upper_to_lower=True, cmp=lambda x, y: x):
    def custom_cmp(x, y):
        result = cmp(x, y)
        if result > 0:
            return x if upper_to_lower else y
        elif result < 0:
            return y if upper_to_lower else x
        else:
            return "같음"
    
    sorted_lst = []
    for i in range(len(lst) - 1):
        sorted_lst.append(custom_cmp(lst[i], lst[i + 1]))
    
    return sorted_lst

# 테스트 예시
lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# 큰 요소 출력 (오름차순)
print(sort4(lst, upper_to_lower=True))  # 출력: [3, 4, 4, 5, 9, 9, 6, 6, 5]

# 큰 요소 출력 (내림차순)
print(sort4(lst, upper_to_lower=False))  # 출력: [1, 1, 1, 1, 2, 5, 5, 3, 3]

import random

def sort5(lst, upper_to_lower=True, cmp=lambda x, y: x, tie_breaker=lambda x, y: random.choice([x, y])):
    def custom_cmp(x, y):
        result = cmp(x, y)
        if result > 0:
            return x if upper_to_lower else y
        elif result < 0:
            return y if upper_to_lower else x
        else:
            # cmp의 결과가 같을 경우 타이 브레이커 적용
            return tie_breaker(x, y)
    
    sorted_lst = []
    for i in range(len(lst) - 1):
        sorted_lst.append(custom_cmp(lst[i], lst[i + 1]))
    
    return sorted_lst

# 테스트 예시
lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# 타이 브레이커 적용 (오름차순)
print(sort5(lst, upper_to_lower=True))  # 출력 예시: [3, 4, 4, 5, 9, 9, 6, 6, 5]

# 타이 브레이커 적용 (내림차순)
print(sort5(lst, upper_to_lower=False))  # 출력 예시: [1, 1, 1, 1, 2, 5, 5, 3, 3]


# --------------------------------------------
# os_file_concept.py 해보고 올 것 
# --------------------------------------------

# --------------------------------------------
# 3. safe pickle load/dump 만들기 
# 
# 일반적으로 pickle.load를 하면 무조건 파일을 읽어와야 하고, dump는 써야하는데 반대로 하면 굉장히 피곤해진다. 
# 이런 부분에서 pickle.load와 pickle.dump를 대체하는 함수 safe_load, safe_dump를 짜 볼 것.  
# hint. 말만 어렵고 문제 자체는 정말 쉬운 함수임.
# --------------------------------------------

def safe_load(pickle_path):
    pass 

def safe_dump(pickle_path):
    pass 


# --------------------------------------------
# 4. 합성함수 (추후 decorator)
# 
# 1) 만약 result.txt 파일이 없다면, 함수의 리턴값을 result.txt 파일에 출력하고, 만약 있다면 파일 내용을 읽어서 
#    '함수를 실행하지 않고' 리턴하게 하는 함수 cache_to_txt를 만들 것. txt 파일은 pickle_cache 폴더 밑에 만들 것.  
# 2) 함수의 실행값을 input에 따라 pickle에 저장하고, 있다면 pickle.load를 통해 읽어오고 없다면 
#    실행 후 pickle.dump를 통해 저장하게 하는 함수 cache_to_pickle을 만들 것. pickle 파일은 pickle_cache 폴더 밑에 만들 것. 
# 3) 함수의 실행값을 함수의 이름과 input에 따라 pickle에 저장하고, 2)와 비슷하게 진행할 것. pickle 파일은 pickle_cache 폴더 밑에, 각 함수의 이름을 따서 만들 것 
# --------------------------------------------

def cache_to_txt(function):
    pass 

def cache_to_pickle(function):
    pass 


