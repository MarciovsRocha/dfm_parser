# ----------------------------------------------------------
# created by: dev.marcio.rocha@gmail.com
# date: 26-12-2022
# observation: Delphi Form Files parser
# ----------------------------------------------------------

# ----------------------------------------------------------
# imports
from dfmparser import DFMParser
from utils import criar_estrutura_local

# ----------------------------------------------------------
# CONSTANTS
# Delpgi Form File path
# file = PROJ_PATH+'\CPlanoInativo.dfm'

CLASSE = str(input('Exemplo: CPlanoinativo.dfm\nDigite o nome do arquivo DFM sua classe:\n'))

try:
    CLASSE.index('.dfm')
except ValueError:
    CLASSE = CLASSE+'.dfm'

# ----------------------------------------------------------
# main script 
parser = DFMParser(file_path = CLASSE)
parser.parse()
lista_atributos = parser.get_lista_atributos()
lista_fields = parser.get_lista_fields()
estrutura_local = criar_estrutura_local(lista_atributos=lista_atributos, lista_fields=lista_fields)
ARQUIVO_EXPORTADO = 'estrutura_local.txt'
with open(ARQUIVO_EXPORTADO, 'w', encoding='utf-8') as fwrite:
    fwrite.write(estrutura_local)
input(f'Arquivo exportado para: {ARQUIVO_EXPORTADO}\nAperte [Enter] para finalizar.')
