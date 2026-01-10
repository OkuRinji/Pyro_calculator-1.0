from pydantic import BaseModel
from typing import Literal
# Класс компонента олицевторяет компонент пиротехничесого состава и некоторые его свойства


class Component(BaseModel):
      type:Literal['oxy','fuel']
      name :str
      enthalpy : float|int
      demidov_coeff :float|int
      molar_mass:float|int
      formula:dict 
#     def __repr__(self):
#         return f"Component(Number:{self.name} enthalpy {self.enthalpy} demidov coff {self.demidov_coeff} molarmass={self.molar_mass} formula={self.formula}) "


# Класс списка компонентов ( костыль для чтения из Excel веротяно уберу )
class Library:
        def __init__(self):
               self._components={}
                      
        def add_component(self, comp:Component):
              self._components[comp.name]=comp
        def get_component(self, name:str):
              if name not in self._components:
                    raise ValueError(f"Компонент с именем {name} не найден")
              return self._components.get(name)
        def __iter__ (self):
              return iter(self._components.values())
        def __len__(self) -> int:
            return len(self._components)
        
        
        
     

    
    
   
    