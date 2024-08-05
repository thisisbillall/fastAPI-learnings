from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def hello():
    names = ['Bilal', 'Vaibhav', 'Varun']
    return {"users":names}

@app.get('/login/{name}')
async def login(name: str):
    return {"msg":f"{name}, please login!"}