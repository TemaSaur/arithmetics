from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI()
templates = Jinja2Templates(directory='templates')
counter = -1


@app.get("/")
async def index(request: Request, number = '0'): # number - url parameter
    global counter
    counter += 1
    return templates.TemplateResponse('index.html', {
        'request': request, # required for jinja2 to work
        'counter': counter,
        'number': int(number),
        'collection': ['banana', 'apple', 'strawberry'],
    })


app.mount('/static', StaticFiles(directory='static'), name='static')

