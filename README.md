# Algorithm
백준 및 프로그래머스 문제 누적



(참고)
### Python 함수 시간 복잡도
https://wiki.python.org/moin/TimeComplexity

### Python 2차원 리스트 초기화 시 주의 사항
- 특정 크기의 2차원 리스트를 초기화할 때는 반드시 리스트 컴프리헨션 이용할 것.
- 내부적으로 포함된 리스트가 모두 동일한 객체에 대한 레퍼런스로 인식되기 때문에, 의도치 않은 결과로 이어질 수 있다.
- https://velog.io/@gndan4/%ED%8C%8C%EC%9D%B4%EC%8D%AC-2%EC%B0%A8%EC%9B%90-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EC%B4%88%EA%B8%B0%ED%99%94-%EC%8B%9C-%EC%A3%BC%EC%9D%98%EC%82%AC%ED%95%AD

### input 보단, sys.stdin.readline 사용
- input = sys.stdin.readline 선언 후 input 사용
- 이 속도 차이로, 성공/시간초과로 갈리는 문제들이 있다.


### 속도 관련 주의 사항

- 어떤 수의 K제곱은 O(logK)만에 구할 수 있다.
- big-O 표기법에서 log는 밑이 2인 로그
- for문 1억 번 당 1초 (중첩일 경우 한 for문의 연산 갯수들을 곱한 수)
- for문에 연루된 수식 연산을 줄이면(레지스터에 저장하면), 그 만큼 연산이 시간이 줄어든다.


### 피보나치수
https://www.acmicpc.net/blog/view/28
![image](https://user-images.githubusercontent.com/39516757/160544006-fd13c72e-ae58-41eb-9869-4367420fa30a.png)
