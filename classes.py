"""
----------------------------------------------------------
created by: dev.marcio.rocha@gmail.com
date: 26-12-2022
observation: Delphi Form Files parser
----------------------------------------------------------
"""

# -----------------------------------------------
class Property():
    """ Delphi Form File Parser """
    # private definitions
    __properties: list
    __properties_names: list
    # public definitions
    name: str
    value: any = None
    # -----------------------------------------------
    # constructor
    def __init__(self, **kwargs):
        self.__properties = []
        self.__properties_names = []
        if 'name' not in kwargs:
            raise AttributeError('Atributo "name" nao definido para construtor da classe "Property".')
        if 'value' in kwargs:
            self.value=kwargs['value']            
        self.name=kwargs['name']

    # -----------------------------------------------
    def get_properties(self):
        """ get properties from actual object """
        return self.__properties
   
    # -----------------------------------------------
    def new_property(self, property):        
        """ add new property Object to current object """
        if property.name not in self.__properties_names:
            self.__properties_names.append(property.name)
            self.__properties.append(property)
        else:
            raise NameError(f'Ja existe uma propriedade com nome "{property.name}" definida para o objeto atual.')
        return self

    # -----------------------------------------------
    def remove_property(self, name: str):
        """ remove property Object from current object """
        if '' == name:
            raise AttributeError('Atributo "name" nao informado para funcao "remove_property".')
        if name not in self.__properties_names:
            raise AttributeError(f'Nao existe propriedade com nome "{name}" definida para o objeto atual.')
        index = self.__properties_names.index(name)
        self.__properties.pop(index)
        self.__properties_names.pop(index)
        return self

    # -----------------------------------------------
    def __str__(self):
        """ remove property Object from current object """
        string = f'{self.name}'
        return string

    # -----------------------------------------------
    def get_property(self, name: str):
        """ return property value """
        if self.exists_property(name):
            return self.__properties[self.__properties_names.index(name)].value

    # -----------------------------------------------
    def to_json(self, **kwargs):
        """ exports property to JSON object """
        json_prop = {'name': '', 'value': ''}
        json_prop['name'] = self.name
        if self.value is not None:
            if 'Property' == type(self.value):
                json_prop['value'] = self.value.to_json()
            else:
                json_prop['value'] = self.value
        for item in self.__properties_names:
            json_prop[item] = self.__properties[self.__properties_names.index(item)].to_json()
        return json_prop

    # -----------------------------------------------
    def exists_property(self, name: str=''):
        """ verify if exists specified property """
        if '' == name:
            raise AttributeError('Atributo "nome" nao informado para o funcao "get_property".')
        return  name in self.__properties_names
