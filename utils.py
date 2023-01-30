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


# -----------------------------------------------
# Adicionar apostrofos na string
def SingleQuoteStr(string: str):
    return f'\'{string}\''


# -----------------------------------------------
# adicionar aspas na string
def DoubleQuoteStr(string: str):
    return f'"{string}"'


# ----------------------------------------------------------
# creates new Field Def string
def new_field(dict_obj: dict):
    field_def = Template(TAB+'CDS.FieldDefs.Add(${name}, ${type}, ${size});') if 'size' in dict_obj else Template(TAB+'CDS.FieldDefs.Add(${name}, ${type});')
    return field_def.safe_substitute(dict_obj)


# ----------------------------------------------------------
# creates new Field Def string
def FieldTypeDef(t: str):    
    return DELPHI_TYPES[t.lower()]


def CriarEstruturaLocal(lista_atributos: list, lista_fields: list):
    body_estrutura_local = ''
    for att in lista_atributos:
        my_dict = {}
        if att.exists_property('DataField'):        
            my_dict['name'] = SingleQuoteStr(att.name)
            att_field = att.get_property('DataField')
            for field in lista_fields:
                if att_field == field.name:
                    my_dict['type'] = FieldTypeDef(field.get_property('type'))
                    if field.exists_property('Size'):
                        my_dict['size'] = field.get_property('Size')
                    break
            body_estrutura_local += new_field(dict_obj=my_dict)+'\n'
    return body_estrutura_local


# some Variables
PROJ_PATH = get_project_path()
# tabulation
TAB = (' '*2)
# Delphi Field Types
DELPHI_TYPES = {
        'tintegerfield': 'ftInteger'
        , 'tstringfield': 'ftString'
        , 'twordfield': 'ftWord'
        , 'tbcdfield': 'ftBCD'
        , 'tdatetimefield': 'ftDateTime'
        , 'tdatefield': 'ftDate'
        , 'tsmallintfield': 'ftSmallint'
        , 'tmemofield': 'ftMemo'
    }
        