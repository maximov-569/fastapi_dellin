from typing import Annotated

from fastapi import APIRouter, Depends

from repository import TerminalRepository
from schemas import STerminalAdd, STerminal, STerminalId

router = APIRouter(
    prefix='/terminals',
    tags=['Терминалы',]
)


@router.post('')
async def add_terminal(
        terminal: Annotated[STerminalAdd, Depends()],
) -> STerminalId:
    terminal_id = await TerminalRepository.add_one(data=terminal)
    return {'ok': True, 'terminal_id': terminal_id}


@router.get('')
async def get_terminals() -> list[STerminal]:
    terminals = await TerminalRepository.find_all()
    return terminals
