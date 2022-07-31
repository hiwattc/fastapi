import uvicorn
from fastapi import FastAPI
from fastapi.requests import Request
from starlette.responses import JSONResponse

app = FastAPI()

@app.route('/')
async def homepage(req: Request):
    return JSONResponse({
        'hello':'world'
    })

if __name__ == '__main__'    :
    uvicorn.run(app, port=8000)
     