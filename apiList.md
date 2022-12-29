## api 목록



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

