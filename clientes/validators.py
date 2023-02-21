import re

def cpf_valido(numero_cpf):
    return len(numero_cpf) == 11
        
def nome_valido(nome):
    return nome.isalpha()

def celular_valido(numero_celular):
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, numero_celular)
    return resposta