import re
from validate_docbr import CPF

def cpf_valido(numero_do_cpf):
    cpf = CPF()
    return cpf.validate(numero_do_cpf)    

def nome_valido(nome):
    return nome.isalpha()

def rg_valido(rg):
    return len(rg) == 9
   

def celuar_valido(numero_celular):
    """Verifica se o celular é valido (11 9999-9999)"""
    modelo = '[0-9]{2} [9]{1}[0-9]{4}-[0-9]{4}'
    reposta = re.findall(modelo, numero_celular)
    return reposta
