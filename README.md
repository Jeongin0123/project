instagram-clone/
│
├── backend/                # FastAPI 서버
│   ├── main.py             # FastAPI 실행 진입점
│   ├── database.py         # DB 연결 (SQLAlchemy)
│   ├── models.py           # User, Post, Comment, Like 등 DB 모델
│   ├── schemas.py          # 요청/응답 Pydantic 스키마
│   ├── crud.py             # DB 접근 함수
│   ├── auth.py             # JWT 로그인/회원가입
│   └── routers/            # API 라우터
│       ├── users.py
│       ├── posts.py
│       ├── comments.py
│       └── likes.py
│
├── frontend/               # React (Vite 기반)
│   ├── src/
│   │   ├── App.jsx         # 라우팅/전체 레이아웃
│   │   ├── main.jsx        # React 진입점
│   │   ├── index.css
│   │   ├── pages/          # 화면 단위
│   │   │   ├── Login.jsx
│   │   │   ├── Register.jsx
│   │   │   ├── Feed.jsx
│   │   │   ├── Upload.jsx
│   │   │   └── Profile.jsx
│   │   └── components/     # 재사용 컴포넌트
│   │       ├── Navbar.jsx
│   │       ├── PostCard.jsx
│   │       └── CommentBox.jsx
│   ├── App.css
│   ├── index.html
│   └── vite.config.js
│
└── README.md
