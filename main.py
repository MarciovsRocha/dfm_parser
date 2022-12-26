from dfmparser import DFMParser
from utils import PROJ_PATH
file = PROJ_PATH+'\CPlanoInativo.dfm'

parser = DFMParser(file_path = file)
parser.parse()

