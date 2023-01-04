## Project name

namu_board

## About namu_board

직무 기본 역량 평가를 받기 위람 익명게시판을 구축

## 구현 완료 순서

1. Django를 활용한 기본적인 CRUD
2. PostgreSQL와 Django 연결
3. React를 활용한 main, list view page


## 구현 중

1. Django와 React 연결 중

## 구현 예정

1. 주석 추가
2. secret key를 .env로 저장 후 .gitignore 추가
3. Refactoring


## 사용 기술

### Django

1. 내가 배운 python 기반의 웹프레임 워크
2. MVC가 아니라 MVT 패턴을 사용해서 큰 프로젝트 규모에서 유지보수가 유용해서 사용하기 좋음
3. App 단위로 개발해서 확장성이 좋음
4. ORM 지원해서 python 코드로 DB 조작 가능

### PostgreSQL

1. 일반적인 Realational Database
2. 데이터를 정규화해서 저장함
3. 속도보다 정확도가 중요함

### React

1. Single Page Application으로도 충분한 Project
2. component로 단순 반복 페이지 html을 재사용
3. 데이터가 html에 자동 반영
4. 제일 많이 사용하는 JS 라이브러리로 관련 정보가 많음
5. 추후 React 문법으로 모바일 앱 개발로 추가도 가능

## 개발 환경

OS : window 10

Code Editing : VScode

terminal : Git Bash

## 설치 환경

Python 3.9.12 가상환경

#### backend

    python==3.9.12
    django==3.1.6
    djangorestframework==3.12.2
    Pillow==22.0.4

#### Database

    PostgreSQL==15.1

#### frontend

    node==18.12.1
    npm==8.19.2
    
## 참고자료

Git : https://cocoon1787.tistory.com/708

Django : https://www.youtube.com/watch?v=q9KKEtBY7ho

PostgreSQL : https://doorbw.tistory.com/183, https://engineer-mole.tistory.com/108

Readme : https://backendcode.tistory.com/165

React : https://www.youtube.com/watch?v=00yJy7W0DQE&list=PLfLgtT94nNq0qTRunX9OEmUzQv4lI4pnP, https://antdev.tistory.com/77, https://anerim.tistory.com/226

React, Django Integrate : https://www.youtube.com/watch?v=FhkqMHxchZ8

