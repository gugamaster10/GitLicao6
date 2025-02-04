from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

@app.get("/")
async def root():
    return {
        "mensagem": "Bem vindo a api de operações básicas, cheque a documentação"
    }


class Operacoes(BaseModel):
    valor1: int
    valor2: int
    operacao: str


@app.post("/math")
async def math(opm: Operacoes):
    """
    Bem vindo a api que gera cálculos matemáticos simles. Acesse http://localhost:8000/docs para mais informações.
    :param opm: Informe os valores de valor1 e valor2 como números inteiros, e '+' para soma, '-' para subtração, 'x'
    para multiplicação, e '/' ou ':' para divisão.
    :return: Resultados das operações matemáticas.
    """
    if opm.operacao == "+":
        soma = (opm.valor1 + opm.valor2)
        return {"Soma": soma}
    if opm.operacao == "-":
        subtracao = (opm.valor1 - opm.valor2)
        return {"Subtração": subtracao}
    if opm.operacao == "x":
        multiplicacao = (opm.valor1 * opm.valor2)
        return {"Multiplicação": multiplicacao}
    if opm.operacao == "/" or opm.operacao == ":":
        divisao = (opm.valor1 / opm.valor2)
        return {"Divisão": divisao}
    else:
        return {"Insira um valor válido, ou acesse 'http://localhost:8000/docs' para acessar a documentação da api"}
    
 
