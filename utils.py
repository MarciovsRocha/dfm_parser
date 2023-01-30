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
def get_username():
    """ Get login from user """
    os.getlogin()


# -----------------------------------------------
def get_date():
    """ format actual date to str in dd/MM/YYY """
    date.today().strftime("%d/%m/%Y")


# -----------------------------------------------
def validar_atributos_obrigatorios(**kwargs):
    """ validate attributes """
    for arg in kwargs.items():
        if (type(kwargs[arg]) in [str , list]) and (0 >= len(kwargs[arg])):
            raise AttributeError(f'Attribute {arg} not informed.')


# -----------------------------------------------
def load_json(nome: str = ''):
    """ carregar arquivo JSON para objeto DICT python """
    validar_atributos_obrigatorios(nome=nome)
    path = os.path.realpath(nome)
    with open(path , 'r', encoding='utf-8') as file:
        python_dict = json.load(file)
    return python_dict


# -----------------------------------------------
def load_template(nome: str = ""):
    """
        * TODO: transformar este modelo para trabalhar com colheita
        * carregar arquivo template para python string
    """
    validar_atributos_obrigatorios(nome=nome)
    with open(nome, encoding='utf-8') as template_file:
        s = Template(template_file.read())
    return s


# -----------------------------------------------
def get_project_path():
    """ retornar o caminho do projeto """
    return os.path.dirname(os.path.abspath(__file__))


# -----------------------------------------------
def null_or_empty(var: any):
    """ verificar se a variável está nula ou vazia """
    if type(var) in [str, list, tuple]:
        return (0 == len(var)) or (var is None)
    return var is None


# -----------------------------------------------
def single_quote_str(string: str):
    """ Adicionar apostrofos na string """
    return f'\'{string}\''


# -----------------------------------------------
def double_quote_str(string: str):
    """ adicionar aspas na string """
    return f'"{string}"'


# ----------------------------------------------------------
def new_field(dict_obj: dict):
    """ creates new Field Def string """
    field_def = Template(TAB+'CDS.FieldDefs.Add(${name}, ${type}, ${size});') if 'size' in dict_obj else Template(TAB+'CDS.FieldDefs.Add(${name}, ${type});')
    return field_def.safe_substitute(dict_obj)


# ----------------------------------------------------------
def field_type_def(text: str):
    """ creates new Field Def string """
    return DELPHI_TYPES[text.lower()]


# ----------------------------------------------------------
def criar_estrutura_local(lista_atributos: list, lista_fields: list):
    """ cria estrutura local """
    body_estrutura_local = ''
    for att in lista_atributos:
        my_dict = {}
        if att.exists_property('DataField'):        
            my_dict['name'] = single_quote_str(att.name)
            att_field = att.get_property('DataField')
            for field in lista_fields:
                if att_field == field.name:
                    my_dict['type'] = field_type_def(field.get_property('type'))
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
        