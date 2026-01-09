
# Класс компонента олицевторяет компонент пиротехничесого состава и некоторые его свойства
class Component():
    def __init__(self, type:str, name:str,enthalpy:float, demidov_coeff:float,molar_mass:float,formula: dict[str , float] ):
      self.type=type
      self.name = name
      self.enthalpy = enthalpy
      self.demidov_coeff =demidov_coeff
      self.molar_mass=molar_mass
      self.formula=formula 
    def __repr__(self):
        return f"Component(Number:{self.name} enthalpy {self.enthalpy} demidov coff {self.demidov_coeff} molarmass={self.molar_mass} formula={self.formula}) "


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
        
        
        
     

    
    
   
    