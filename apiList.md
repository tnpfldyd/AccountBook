# api 목록



## accounts app



- 회원가입
  - url: http://localhost:8000/api/accounts/registration/
  - method: post
  - {
        "email": "",
        "password1": "",
        "password2": ""
    }



- 로그인
  - url: http://localhost:8000/api/accounts/login/
  - method: "post"
  - data: {
        "email": "",
        "password": ""
    }



- 로그아웃
  - url: http://localhost:8000/api/accounts/logout/
  - method: "post"



- 유저정보
  - url: http://localhost:8000/api/accounts/user/
  - method: "get"



- 비밀번호 변경
  - url: http://localhost:8000/api/accounts/password/change/
  - method: "post"
  - data: {
        "new_password1": "",
        "new_password2": ""
    }

## books app

- 가계부 목록
  - url: http://localhost:8000/api/books/
  - method: "get"



- 가계부 생성

  - url: http://localhost:8000/api/books/

  - method: "post"

  - data: {
        "category": bool, # 수입, 지출 구분 type bool
        "amount_moved": 금액, # type int

    ​	"memo": "내용",

    }



- 가계부 상세
  - url: http://localhost:8000/api/books/pk/
  - method: "get"



- 가계부 수정

  - url: http://localhost:8000/api/books/pk/

  - method: "put"

  - data: {
        "category": bool, # 수입, 지출 구분 type bool
        "amount_moved": 금액, # type int

    ​	"memo": "내용",

    }



- 가계부 삭제
  - url: http://localhost:8000/api/books/pk/
  - method: "delete"



- 가계부 복제
  - url: http://localhost:8000/api/books/pk/copy/
  - method: "post"

- 가계부 공유
  - url: http://localhost:8000/api/books/pk/share/
  - method: "post"

- 단축 url
  - url: http://localhost:8000/api/books/단축url/ #8시간 뒤 삭제
  - method: "get"