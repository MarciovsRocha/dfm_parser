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
# file = PROJ_PATH+'\CPlanoInativo.dfm'
comom_path = 'C:\projects\HomePar\Fontes\Comum\Classes\\'

classe = str(input('Exemplo: CPlanoinativo.dfm\nDigite o nome do arquivo DFM sua classe:\n'))

file: str

try:
    classe.index('.dfm')
    file = comom_path+classe
except:
    file = comom_path+classe+'.dfm'

# ----------------------------------------------------------
# main script 
parser = DFMParser(file_path = file)
parser.parse()
lista_atributos = parser.get_lista_atributos()
lista_fields = parser.get_lista_fields()
estrutura_local = CriarEstruturaLocal(lista_atributos=lista_atributos, lista_fields=lista_fields)
arquivo_exportado = f'estrutura_local_{classe}.txt'
with open(arquivo_exportado, 'w') as fwrite:
    fwrite.write(estrutura_local)
input(f'Arquivo exportado para: {arquivo_exportado}\nAperte [Enter] para finalizar.')
