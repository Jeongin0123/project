from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymysql

# DB 접속 정보
USER = "root"
PASSWORD = "doitmysql"   # ← 본인 비밀번호
HOST = "localhost"
PORT = 3306
DB_NAME = "instagram_clone"

# SQLAlchemy용 URL
DATABASE_URL = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"

# 데이터베이스 없으면 자동 생성
def create_database_if_not_exists():
    connection = pymysql.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        port=PORT,
        charset='utf8mb4',
        autocommit=True
    )
    with connection.cursor() as cursor:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME} "
                      "CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
    connection.close()

create_database_if_not_exists()

# SQLAlchemy 엔진
engine = create_engine(DATABASE_URL, echo=True)

# 세션
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base
Base = declarative_base()

# DB 세션 종속성
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
