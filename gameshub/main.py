from typing import List

from fastapi import FastAPI, Path, status
from pydantic import BaseModel, Field


import parser
from exceptions import ExceptionHandlers

app = FastAPI(
    title="Adimplere GamesHUB",
    version="1.0.0",
    openapi_url="/openapi.json",
    docs_url="/",
)

class GameShort(BaseModel):
    uuid: str = Field(..., description="Content Identifier")
    short_description: str = Field(..., description="Content short description")   

class GameDetail(BaseModel):
    uuid: str = Field(..., description="Content Identifier")
    long_description: str = Field(..., description="Content long description")

@app.get(
    "/games",
    status_code=status.HTTP_200_OK,
    summary="List All Games",
    response_model=List[GameShort],
    responses={
        status.HTTP_200_OK: {"model": List[GameShort]},
    },
)        

async def games():
    return parser.parse_all()


@app.get(
    "/games/{name}",
    status_code=status.HTTP_200_OK,
    summary="Detail one Game",
    response_model=GameDetail,
    responses={
        status.HTTP_200_OK: {"model": GameDetail},
    },
)
async def games(name: str = Path(..., description="game name")):
    return parser.parse_one(name)


app.add_exception_handler(Exception, ExceptionHandlers.unhandled_exception)