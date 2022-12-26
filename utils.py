# ----------------------------------------------------------
# created by: dev.marcio.rocha@gmail.com
# date: dd-MM-yyyy
# description: simple python script
# ----------------------------------------------------------

# -----------------------------------------------
# imports
from datetime import date
import os
import json
from string import Template


# -----------------------------------------------
# return username
def get_username():
    os.getlogin()


# -----------------------------------------------
# format actual date to str in dd/MM/YYY
def get_date():
    date.today().strftime("%d/%m/%Y")


# -----------------------------------------------
# validate attributes
def validar_atributos_obrigatorios(**kwargs):
    for arg in kwargs:
        if type(kwargs[arg]) in [str , list]:
            if 0 >= len(kwargs[arg]):
                raise AttributeError(f'Attribute {arg} not informed.')


# -----------------------------------------------
# carregar arquivo JSON para objeto DICT python
def load_json(nome: str = ''):
    validar_atributos_obrigatorios(nome=nome)
    path = os.path.realpath(nome)
    with open(path , 'r') as file:
        python_dict = json.load(file)
    return python_dict


# -----------------------------------------------
# TODO: transformar este modelo para trabalhar com colheita
# carregar arquivo template para python string
def load_template(nome: str = ""):
    validar_atributos_obrigatorios(nome=nome)
    with open(nome) as template_file:
        s = Template(template_file.read())
    return s


# -----------------------------------------------
# retornar o caminho do projeto
def get_project_path():
    return os.path.dirname(os.path.abspath(__file__))


# -----------------------------------------------
# verificar se a variável está nula ou vazia
def NullOrEmpty(var: any):
    if type(var) in [str, list, tuple]:
        return (0 == len(var)) or (var is None)
    return var is None


# some Variables
PROJ_PATH = get_project_path()
