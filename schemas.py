from pydantic import BaseModel


class STerminalAdd(BaseModel):
    name: str
    description: str | None = None


class STerminal(STerminalAdd):
    id: int


class STerminalId(BaseModel):
    ok: bool = True
    terminal_id: int
