# ----------------------------------------------------------
# created by: dev.marcio.rocha@gmail.com
# date: 26-12-2022
# observation: Delphi Form Files parser
# ----------------------------------------------------------

# -----------------------------------------------
# imports
import utils
from  classes import Property

# -----------------------------------------------
# Delphi Form File Parser 
class DFMParser():
    # private declarations
    __file_oppened: bool    
    __file_stream = None
    __atributos: list
    __fields: list
    # public variables
    file_path: str

    # -----------------------------------------------
    # constructor
    def __init__(self, **kwargs):
        if 'file_path' in kwargs:
            self.file_path = kwargs['file_path']
        self.__file_oppened = False
        self.__file_stream = None
        self.__atributos = []
        self.__fields = []

    # -----------------------------------------------
    # ensure that file is oppened 
    def open_file(self):
        if not utils.NullOrEmpty(self.file_path):
            self.__file_stream = open(self.file_path)
        self.__file_oppened = True
        return self

    # -----------------------------------------------
    # ensure that file is closed
    def close_file(self):
        if None != self.__file_stream:
            self.__file_stream.close()
        self.__file_oppened = False
        self.__file_stream = None
        return self

    # -----------------------------------------------
    # alter value from 
    def set_file(self, file_path: str):
        if self.__file_oppened:
            self.close_file()        
        return self

    # -----------------------------------------------
    # parse atrib section
    def parse(self):
        if not self.__file_oppened:
            self.open_file()
        lista_atributos = Property(name='Atributos')
        atrib_prop = False
        item_prop = False
        item = {}
        fields_prop = False
        for line in self.__file_stream:            
            line = line.replace('\n', '')
            if 'atributos' in line.lower():
                atrib_prop = True            
            elif 'item' in line.lower():
                item_prop = True
            elif atrib_prop and item_prop and ('=' in line):
                name,value = line.replace(' ', '').replace('\'','').split('=')
                item[name] = value
            elif atrib_prop and item_prop and ('end' in line.lower()):
                item_prop = False
                atributo = Property(name=item['Nome'])
                for val in item:
                    if 'nome' not in val.lower():
                        atributo.new_property(Property(name=val, value=item[val]))
                item = {}
                lista_atributos.new_property(atributo)                
                self.__atributos.append(atributo)
            elif 'end>' in line.lower():
                atrib_prop = False
                item_prop = False        
                item = {}
            elif ('object' in line.lower()) and ('field' in line.lower()):
                fields_prop = True
                item = {}
                item['type'] = line.split(' ')[len(line.split(' '))-1]
            if fields_prop and ('=' in line):
                name, value = line.replace(' ', '').replace('\'','').split('=')
                item[name] = value
            elif fields_prop and ('end' in line.lower()):
                fields_prop = False
                field = Property(name=item['FieldName'])
                for val in item:
                    if 'fieldname' not in val.lower():
                        field.new_property(Property(name=val, value=item[val]))
                self.__fields.append(field)              
                item = {}
        self.close_file()            
        return lista_atributos
