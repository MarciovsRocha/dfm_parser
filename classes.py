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
    value: any
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
        if '' == name:
            raise AttributeError('Atributo "nome" nao informado para o funcao "get_property".')
        elif name not in self.__properties_names:
            raise AttributeError(f'Atributo com o nome "{nome}" nao existe no objeto atual.')
        return self.__properties[self.properties_names.index(name)].value
