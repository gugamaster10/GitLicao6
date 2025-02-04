def math_teste(x,y,z):
    
    """
    Função 1 para soma, 2 para subtração, 3 para multiplicação, 4 para divisão
    """
    if x == 1:
        soma = (y + z)
        return soma
    if x == 2:
        subtracao = (y - z)
        return subtracao
    if x == 3:
        multiplicacao = (y * z)
        return multiplicacao
    if x == 4 or x == ":":
        divisao = (y / z)
        return divisao
    else:
        return {"Insira um valor válido, ou acesse 'http://localhost:8000/docs' para acessar a documentação da api"}
    
def test_soma():
    assert math_teste(1, 2, 2) == 4

def test_sub():
    assert math_teste(2, 10, 5) == 5

def test_multi():
    assert math_teste(3, 5, 2) == 10
    
def test_div():
    assert math_teste(4, 10, 5) == 2

   