## api 목록



- 회원가입
  - 요청 주소: http://localhost:8000/api/accounts/v1/registration
  - method: post
  - {
        "email": "",
        "password1": "",
        "password2": ""
    }



- 로그인
  - 요청 주소: http://localhost:8000/api/accounts/v1/login/
  - method: post
  - {
        "email": "",
        "password": ""
    }



- 로그아웃
  - 요청 주소: http://localhost:8000/api/accounts/v1/logout/
  - method: post



- 유저정보
  - 요청 주소: http://localhost:8000/api/accounts/v1/user/
  - method: get



- 비밀번호 변경
  - 요청 주소: http://localhost:8000/api/accounts/v1/password/change/
  - method: post
  - {
        "new_password1": "",
        "new_password2": ""
    }

