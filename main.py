from fastapi import FastAPI

app = FastAPI(title='API de Nicollas e Daniel')

@app.get("/")
def helloWorld():
    return{"message":"Hello World!"}
