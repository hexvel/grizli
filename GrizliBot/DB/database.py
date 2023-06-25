import uvicorn
import json

from typing import Optional
from fastapi import FastAPI
from tortoise import Tortoise
from loguru import logger as log

from BaseModel.Get_Base import searchBase
from BaseModel.Marriage import Marriage

app = FastAPI()


@app.on_event("startup")
async def startup():
    log.success('Tortoise is running')
    await Tortoise.init(
        db_url='sqlite://hexvel.sqlite3',
        modules={'models': ['BaseModel.MainModel', 'BaseModel.Marriage']}
    )
    await Tortoise.generate_schemas()


@app.on_event('shutdown')
async def close_connect():
    await Tortoise.close_connections()


@app.get('/createTemplate/')
async def createTemplate(params: Optional[str], bases: Optional[str]) -> Optional[dict]:
    bases = searchBase(base=bases)
    params = json.loads(params)
    await bases.create(**params)
    return {'running': True, 'data': True}


@app.get('/all/')
async def all():
    marriages = await Marriage.all()
    return {'running': True, 'marry': marriages}


@app.get('/getter/')
async def getter(filters: Optional[str], bases: Optional[str]) -> Optional[dict]:
    bases = searchBase(base=bases)
    filters: Optional[dict] = json.loads(filters)
    Object = bases.filter(**filters)
    if await Object.first() is None:
        return {'running': False, 'data': None}
    else:
        return {'running': True, 'data': await Object.first()}


@app.get('/creaters')
async def creater(filters: Optional[str], params: Optional[str], bases: Optional[str]) -> Optional[dict]:
    bases = searchBase(base=bases)
    filters = json.loads(filters)
    params = json.loads(params)
    Object = bases.filter(**filters)
    if await Object.first() is None:
        await bases.create(**params)
        return {'running': True, 'data': await Object.first()}
    return {'running': False, 'data': None}


@app.get('/deleter')
async def deleter(filters: Optional[str], bases: Optional[str]) -> Optional[dict]:
    bases = searchBase(base=bases)
    filters = json.loads(filters)
    Object = bases.filter(**filters)
    if await Object.first() is None:
        return {'running': False, 'data': None}
    else:
        await Object.delete()
        return {'running': True, 'data': True}


@app.get('/updater/')
async def updater(filters: Optional[str], params: Optional[str], bases: Optional[str]) -> dict:
    bases = searchBase(base=bases)
    filters: Optional[dict] = json.loads(filters)
    params: Optional[dict] = json.loads(params)
    Object = bases.filter(**filters)
    if await Object.first() is None:
        return {'running': False, 'data': None}
    else:
        await Object.update(**params)
        return {'running': True, 'data': await Object.first()}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8088, log_level='info')