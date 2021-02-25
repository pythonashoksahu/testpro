from fastapi import FastAPI

app=FastAPI()


@app.get('/')
def index():
    return 'hiiii'


@app.get('/about')
def about(limit):
    return {'ashok':f'{limit} sahu'}

@app.get('/blog/{id}')
def blog(id:int):
    return {'ashok':id}