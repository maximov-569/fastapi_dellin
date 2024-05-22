from fastapi import FastAPI

from contextlib import asynccontextmanager

from database import create_tables, drop_tables
from router import router as terminals_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await drop_tables()
    print('Database clear')
    await create_tables()
    print('Ready to work')
    yield
    print('Drop App')


app = FastAPI(lifespan=lifespan)
app.include_router(terminals_router)

