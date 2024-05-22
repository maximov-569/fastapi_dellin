from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


engine = create_async_engine(
    'sqlite+aiosqlite:///terminals.db'
)

new_session = async_sessionmaker(engine, expire_on_commit=False)


class BaseModel(DeclarativeBase):
    pass


class TerminalOrm(BaseModel):
    __tablename__ = 'terminals'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str | None]


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)


async def drop_tables():
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.drop_all)
