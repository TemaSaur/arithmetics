from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from user import User


app = FastAPI()
templates = Jinja2Templates(directory='templates')
counter = -1


users = {}


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


@app.get("/problemset")
async def problemset(request: Request, name='', tries=3):
	users[name] = User(name, tries)
	user = users[name]
	return templates.TemplateResponse('problemset.html', {
		'request': request,
		'problem': user.problem,
		'answer_base': user.answer_base
	})


@app.get("/results")
async def results(request: Request, name):
	user = users[name]
	results = list(user.get_results())
	mark = int(any(x['result'] for x in results))
	return templates.TemplateResponse('results.html', {
		'request': request,
		'results': results,
		'mark': mark
	})


@app.get("/api/check_answer")
async def check_answer(request: Request, name, answer):
	user = users[name]
	return user.check_answer(answer)


@app.get('/api/done')
async def check_answer(request: Request, name):
	user = users[name]
	print(user.done())
	return user.done()


app.mount('/static', StaticFiles(directory='static'), name='static')
