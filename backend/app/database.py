from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from collections.abc import AsyncGenerator

from env import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME

DATABASE = "mysql+aiomysql://%s:%s@%s/%s?charset=utf8" % (
    DB_USER,
    DB_PASSWORD,
    DB_HOST,
    DB_NAME,
)

engine = create_async_engine(DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

async def get_async_db() -> AsyncGenerator[AsyncSession, None]:
    """endpointからアクセス時に、Dependで呼び出しdbセッションを生成する
    エラーがなければ、commitする
    エラー時はrollbackし、いずれの場合も最終的にcloseする.
    """
    async with SessionLocal() as db:
        try:
            yield db
            await db.commit()
        except Exception:
            await db.rollback()
            raise
        finally:
            await db.close()

Base = declarative_base()