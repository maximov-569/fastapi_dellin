from database import new_session, TerminalOrm
from sqlalchemy import select

from schemas import STerminalAdd, STerminal


class TerminalRepository:
    @classmethod
    async def add_one(cls, *, data: STerminalAdd) -> int:
        async with new_session() as session:
            terminal_dict = data.model_dump()

            terminal = TerminalOrm(**terminal_dict)
            session.add(terminal)
            await session.flush()
            await session.commit()
            return terminal.id

    @classmethod
    async def find_all(cls) -> list[STerminal]:
        async with new_session() as session:
            query = select(TerminalOrm)
            result = await session.execute(query)
            terminal_models = result.scalars().all()
            terminal_models = [STerminal.model_validate(terminal) for terminal in terminal_models]
            return terminal_models
