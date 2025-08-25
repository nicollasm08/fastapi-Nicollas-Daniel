from fastapi import FastAPI

app = FastAPI(title='API de Nicollas e Daniel')

@app.get("/")
def helloWorld():
    return{"message":"Hello World!"}

@app.get("/aluno/{nome_aluno}")
def get_aluno_by_name(nome_aluno: str):
    return {f"Olá, {nome_aluno}, seja muito bem-vindo(a) ao nosso app!"}