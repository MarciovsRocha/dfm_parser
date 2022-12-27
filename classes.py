# ----------------------------------------------------------
# created by: dev.marcio.rocha@gmail.com
# date: 26-12-2022
# observation: Delphi Form Files parser
# ----------------------------------------------------------


# -----------------------------------------------
# Delphi Form File Parser 
class Property():
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
    # get properties from actual object
    def get_properties(self):
        return self.__properties
    
    # -----------------------------------------------
    # add new property Object to current object
    def new_property(self, property):        
        if property.name not in self.__properties_names:
            self.__properties_names.append(property.name)
            self.__properties.append(property)
        else:
            raise NameError(f'Ja existe uma propriedade com nome "{property.name}" definida para o objeto atual.')
        return self

    # -----------------------------------------------
    # remove property Object from current object
    def remove_property(self, name: str):
        if '' == name:
            raise AttributeError('Atributo "name" nao informado para funcao "remove_property".')
        if name not in self.__properties_names:
            raise AttributeError(f'Nao existe propriedade com nome "{name}" definida para o objeto atual.')
        index = self.__properties_names.index(name)
        self.__properties.pop(index)
        self.__properties_names.pop(index)
        return self

    # -----------------------------------------------
    # remove property Object from current object
    def __str__(self):
        s = f'{self.name}'
        return s

    # -----------------------------------------------
    # return property value
    def get_property(self, name: str):
        if self.exists_property(name):
            return self.__properties[self.__properties_names.index(name)].value

    # -----------------------------------------------
    # exports property to JSON object
    def to_json(self, **kwargs):
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
    # verify if exists specified property
    def exists_property(self, name: str=''):
        if '' == name:
            raise AttributeError('Atributo "nome" nao informado para o funcao "get_property".')
        return  name in self.__properties_names
