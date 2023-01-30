"""
----------------------------------------------------------
created by: dev.marcio.rocha@gmail.com
date: 26-12-2022
observation: Delphi Form Files parser
----------------------------------------------------------
"""

# -----------------------------------------------
# imports
import utils
from  classes import Property

# -----------------------------------------------
# Delphi Form File Parser
class DFMParser():
    """
    * Simple Delphi Form File parser, that extracts file properties
    * Created by: dev.marcio.rocha@gmail.com
    """
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
    def open_file(self):
        """
            Method that ensire the FileStream is oppened
        """
        if not utils.null_or_empty(self.file_path):
            self.__file_stream = open(self.file_path, encoding='utf-8')
        self.__file_oppened = True
        return self

    # -----------------------------------------------
    def close_file(self):
        """
            Method that ensure the FileStream is Closed.
        """
        if self.__file_stream is not None:
            self.__file_stream.close()
        self.__file_oppened = False
        self.__file_stream = None
        return self

    # -----------------------------------------------
    def set_file(self, file_path: str):
        """
            Method that alters file of FileStream
        """
        if self.__file_oppened:
            self.close_file()
        self.file_path = file_path
        return self

    # -----------------------------------------------
    def parse(self):
        """
            Parse attribute section
        """
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

    # -----------------------------------------------
    def get_lista_atributos(self):
        """
            Returns attributes list
        """
        return self.__atributos

    # -----------------------------------------------
    def get_lista_fields(self):
        """
            Returns Fields List
        """
        return self.__fields
