# project_3..

![image](https://user-images.githubusercontent.com/97435321/190987213-4ea62a9f-9cac-43db-820a-38fddb09ee6b.png)

Date : 2022.4.18~2022.4.21

Tags : `MongoDB` `Flask` `Dashboard` 

Link : 

[https://github.com/ssuzzang/project_3.git](https://github.com/ssuzzang/project_3.git)

발표영상 : 

[포폴2](https://youtu.be/3WPXy63P1Ew)

---

 - 목차

![image](https://user-images.githubusercontent.com/97435321/190988146-8d093000-bad1-4bd6-9e2d-6b0e035a39c2.png)

1. 1회부터 최근 당첨 번호데이터를 수집합니다.
2. 수집한 데이터를 딥러닝 알고리즘인 LSTM을 통하여 모델학습을 하였습니다.

---
![image](https://user-images.githubusercontent.com/97435321/190988206-87988324-1b30-43aa-a7b7-612aa495413f.png)

- 데이터 수집은 동행복권 공식 홈페이지에서 최신 회차 데이터까지 모두 다운 후 전처리 합니다.

---

![image](https://user-images.githubusercontent.com/97435321/190988240-a825b8b5-d045-4fe6-90fc-83bb521ef9f8.png)


- 딥러닝 모델은 RNN계열의 LSTM 으로 학습합니다.

---

![image](https://user-images.githubusercontent.com/97435321/190988308-e146150e-9c27-447f-8a67-f639d9f53981.png)


몽고DB에 올린 전체 회차별 데이터베이스

---

![image](https://user-images.githubusercontent.com/97435321/190988380-2b402efd-bb6c-47cd-b6cb-ca445a0c7826.png)

몽고DB를 이용한 데시보드

---

![image](https://user-images.githubusercontent.com/97435321/190987990-2d5d63ce-0f3b-469e-8813-4273f4878185.png)

다음 회자 예측

---

-느낀점
  - 로또 같은 독립시행 확률을 가지는 것은 예측모델이 의미가 없다
  - 광고에서 로또 1등 번호를 준다는 것은 다 거짓이다.. 도박을 하지말자!
