from fastapi import FastAPI

app = FastAPI()


@app.get('/healthcheck', status_code=200)
async def root():
    return {'message': 'ok'}
