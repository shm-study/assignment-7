# Assignment 7. Class를 기반으로, 다음 문제를 풀어봅시다.

## Ex 01. Make Class

다음 조건에 맞는 삼각형 클래스를 만들어봅시다.

- class `Triangle`
    - attribute `base` : 삼각형의 밑변
    - attribute `height` : 삼각형의 높이
    - method `area()` : 삼각형의 넓이를 **반환**
    - 생성자를 이용해 `base`와 `height`를 초기화
    - 이 객체를 **출력**(`print()`)하면 "밑변은 `base` 이고 높이는 `height` 인 삼각형 입니다." 이 출력

```python
a = Triangle(3, 4)

print(a.area()) # 6
print(a) # 밑변은 3 이고 높이는 4 인 삼각형 입니다.
```