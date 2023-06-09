# -*- coding: utf-8 -*-
"""11차 과제

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1P2G9sqkNkuEo4SCfz9mrVaJqooauf35w

# (실습) 파일

**기본 설정**

파일 저장 경로와 파일 서버 주소를 지정에 필요한 기본 설정을 지정한다.
"""

from pathlib import Path
from urllib.request import urlretrieve

"""데이터가 저장된 텍스트 파일 서버 주소는 다음과 같다."""

base_url = "https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/data/"

"""현재 작업 디렉토리의 `data` 하위 디렉토리에 파일을 다운로드해서 저장할 준비를 한다."""

# 저장위치 지정과 생성
data_path = Path() / "data"
data_path.mkdir(parents=True, exist_ok=True)

"""`myWget()` 함수는 파일 서버에서 지정된 파일을 동일한 파일명으로 지정된 디렉토리에 저장한다."""

def myWget(filename):
    # 다운로드 대상 파일 경로
    file_url = base_url + filename

    # 저장 경로와 파일명
    target_path = data_path / filename

    return urlretrieve(file_url, target_path)

"""**쇼핑몰 파일 관련**

**문제 1**

`shopA.txt` 파일은 쇼핑몰A에서 판매하는 상품의 가격을 담고 있음을 확인해보자.
먼저 해당 파일을 다운로드 한다.
"""

myWget("shopA.txt")

"""이제 파일 전체 내용을 출력하는 코드를 작성하라.

힌트: `with-as` 명령문, `open()` 함수, `readlines()` 또는 `read()` 파일 메서드.
"""

with open("./data/shopA.txt", encoding='utf-8') as f:
    for line in f:
        print(line.strip())

"""**문제 2**

`shopA.txt` 파일의 내용을 확인하면, 오타가 있다. 
'오레ㄴ지' 를 '오렌지'로 변경한 후에
`shopA.txt` 파일을 열어 오타가 수정되었는지를 확인하여라.  

힌트: 파일의 `read()` 메서드, 문자열의 `replace()` 메서드

* 파일 읽기: `read()` 메서드 활용
"""

# 파일내용을 하나의 문자열로 생성하는 코드를 작성하라.
name = open("./data/shopA.txt", encoding='utf-8')
name_str = name.read()

"""* 오타 수정: `replace()` 문자열 메서드 활용"""

# 오타를 수정하는 코드를 작성하라.
name_replace = name_str.replace('오레ㄴ지', '오렌지')

"""* 파일 저장"""

# 오타가 수정된 문자열을 파일로 저장하는 코드를 작성하라.
with open("./data/shopA.txt", 'w', encoding='utf-8') as t:
    t.write(name_replace)

"""* 파일 내용 확인"""

# 오타가 수정되었음을 확인하는 코드를 작성하라.
result = open("./data/shopA.txt", mode='r', encoding='utf-8')
print(result.read())

"""**문제 3**

상품명과 가격을 키-값의 쌍으로 갖는 아래 모양의 딕셔너리를 만들어라.
단, 오타가 수정된 파일을 이용해야 한다.

```python
{'우유': 2540,
 '계란': 7480,
 '생수': 980,
 '짜장라면': 3220,
 '두부': 1450,
 '콩나물': 1680,
 '김': 5480,
 '닭고기': 5980,
 '식빵': 2480,
 '바나나': 4980,
 '오렌지': 990,
 '카레': 2480,
 '만두': 6980,
 '어묵': 7980,
 '참치': 11880,
 '김치': 7980,
 '간장': 10800}
```
"""

result_dic = {}
with open("./data/shopA.txt", 'r', encoding='utf-8') as f:
    for line in f:
        try:
            key, value = line.strip().split()
            if key != '#쇼핑몰':
                result_dic[key] = value
        except:
            continue

print(result_dic)

"""**문제 4**

`shopA.txt` 와 같이 상품명과 가격으로 이루어진 쇼핑 리스트가 포함된 파일의 이름을 입력받으면
상품명과 가격을 각각 키와 값으로 갖는 사전 객체를 반환하는 함수 `shopping()` 을 구현하라.

힌트: 문제 3을 해결하기 위해 작성한 코드를 이용한다.
"""

# 아래 코드를 완성하라. 

def shopping(shop_file):
    shop_dict = {} # 생성할 사전 객체
    
    with open(f"./data/{shop_file}", 'r', encoding='utf-8') as f:
        for line in f:
            try:
                key, value = line.strip().split()
                if key != '#쇼핑몰':
                    shop_dict[key] = value
            except:
                continue

    return shop_dict
print(shopping("shopA.txt"))

"""**문제 5**

쇼핑 리스트와 상품을 인자로 지정하면 상품의 가격을 반환하는 함수 `item_price()` 를 구현하라.

힌트: `shopping()` 함수를 이용한다.
"""

# 함수를 완성하라.

def item_price(shop_file, item):
    result = shopping(shop_file).get(item)

    return result
print(item_price("shopA.txt", '김치'))

"""**문제 6**

`shopB.txt` 파일은 쇼핑몰B에서 판매하는 상품의 가격을 담고 있으며,
`shopA.txt` 파일과 동일한 방식으로 다운로드할 수 있다.
"""

myWget("shopB.txt")

"""사용자가 상품을 입력하면, 쇼핑몰A와 쇼핑몰B 중 어느 쇼핑몰에서 구입하는 것이 얼마나 저렴한지를 보여주는
함수 `price_comparison()`를 작성하라.
"""

# 코드를 완성하라.

def price_comparison(item):
    cheap = item_price("shopA.txt", item) <= item_price("shopB.txt", item)
    if cheap == True:
        return item_price("shopA.txt", item)
    else:
        return item_price("shopB.txt", item)
    
print(price_comparison('김치'))

"""**다이빙 기록 관련**

**문제 7**

[5미터 다이빙 기록 에서 등수를 확인하는 작업](https://codingalzi.github.io/pybook/files.html#sec-exp-diving-5m)과 
동일한 작업을 10미터 다이빙 기록에 대해 진행하라.
"""

myWget("results10m.txt")

# 코드를 작성하라.
score_10m = {}

with open("./data/results10m.txt", 'r', encoding="utf-8") as t:
    for line in t:
        name, score = line.split()

        try:
            score_10m[name] = float(score)
        
        except:
            continue
score_10m_sorted = sorted(score_10m.items(), key=lambda item: item[1], reverse=True)
count = 1
for item in score_10m_sorted:
    print(f"{count:>3}등: {item[0]} {item[1]}")
    count += 1

"""**문제 8**

5미터 다이빙 기록과 10미터 다이빙 기록의 합에 대해 등수를 확인하는 코드를 작성하라.
"""

# 코드를 작성하라.

myWget("results5m.txt")
myWget("results10m.txt")

def score_add(file_name):
    empty = {}
    with open(f"./data/{file_name}", 'r', encoding='utf-8') as f:
        for line in f:
            name, score = line.split()

            try:
                empty[name] = float(score)
            except:
                continue
    return empty

score_5m = score_add("results5m.txt")
score_10m = score_add("results10m.txt")

score_5m_items = score_5m.items()
score_10m_items = score_10m.items()

add_score = {}
for n1, s1 in score_5m_items:
    for n2, s2 in score_10m_items:
        if n1 == n2:
            add_score[n1] = round(s1 + s2, 2)
        else:
            continue

result = sorted(add_score.items(), key=lambda item: item[1], reverse=True)
count = 1
for item in result:
    print(f"{count:>3}등: {item[0]} {item[1]}")
    count += 1