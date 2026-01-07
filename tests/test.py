from models import Component, Library

comp = Component(
    name="NH4NO3",
    number=1,
    enthalpy=-1090.2,
    demidov_coeff=5.003,
    molar_mass=128.74,
    formula={"O": 37.47, "H": 49.97, "N": 24.98}
)

lib = Library()
lib.add_component(comp)

# Должен вернуть объект, а не None!
c = lib.get_component(1)
print(c.name)  # ← если тут ошибка — значит, нет return

# Должен пройти без ошибок
for c in lib:
    print(c)