from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    is_valid: Union[bool, None] = None

app = FastAPI()

@app.get('/')
def intro():
    '''
    This is the introduction endpoint
    '''
    return 'Hello World';

@app.get('/{id}')
def intro_with_id(id: int, q: Union[str, None] = None):
    '''
    This is an alternate version of the initial introduction endpoint,
    which accespts an id parameter and an optional query parameter, q
    '''
    return {"Data": id, "q": q}

@app.put('/{id}')
def update_base(id: int, item: Item):
    return { "item": item, "id": id }