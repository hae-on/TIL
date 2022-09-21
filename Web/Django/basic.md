## Django 개발 환경 설정 가이드

### Django 설치

- Django 4.0 릴리즈로 인해 3.2(LTS) 버전을 명시해서 설치
  $ pip install django==3.2.13

- 패키지 목록 생성
  $ pip freeze > requirements.txt

### LTS란?

- Long Term Support (장기 지원 버전)
- 일반적인 경우보다 장기간에 걸쳐 지원하도록 고안된 소프트웨어의 버전
- 컴퓨터 소프트웨어의 제품 수명주기 관리 정책
- 배포자는 LTS 확정을 통해 장기적이고 안정적인 지원을 보장함

### Django Project

- 프로젝트 생성
  $ django-admin startproject firstpjt .

- 서버 실행
  $ python manage.py runserver

- 서버 접속
  http://127.0.0.1:8000/

- 포트 변경
  $ python manage.py runserver 8080
