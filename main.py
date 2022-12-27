# ----------------------------------------------------------
# created by: dev.marcio.rocha@gmail.com
# date: 26-12-2022
# observation: Delphi Form Files parser
# ----------------------------------------------------------

# ----------------------------------------------------------
# imports 
from dfmparser import DFMParser
from utils import PROJ_PATH, CriarEstruturaLocal

# ----------------------------------------------------------
# CONSTANTS
# Delpgi Form File path
file = PROJ_PATH+'\CPlanoInativo.dfm'


# ----------------------------------------------------------
# main script 
parser = DFMParser(file_path = file)
parser.parse()
lista_atributos = parser.get_lista_atributos()
lista_fields = parser.get_lista_fields()
print(CriarEstruturaLocal(lista_atributos=lista_atributos, lista_fields=lista_fields))
