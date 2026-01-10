from pyro.data.models import Component,Library
from pyro.data.db_loader import db_comp_get
from sympy import symbols, Eq, nsolve

#Функция - считает небходимое содержание компонентов по двум компонентам и желаемому окислительному балансу 
def oxy_calc(oxy_id:int,fuel_id:int,balance)->tuple [float,float]:
        try:
                oxy=db_comp_get(oxy_id,"oxy")
                fuel=db_comp_get(fuel_id,"fuel")
        except Exception as e :
                raise ValueError(f"Не поучилось загрузть компоненты {e}")
        if oxy.demidov_coeff==0 or fuel.demidov_coeff==0:
                raise ValueError("Коэффициент Демидова не может быть нулевым") 
        x1, x2,  = symbols('x1 ,x2')
        equations=[
        Eq(x1/oxy.demidov_coeff - x2/fuel.demidov_coeff , balance),
        Eq(x1 + x2 , 100),]
        try:
                initial_guess = [50, 50]
                oxy_part, fuel_part = nsolve(equations, (x1, x2), initial_guess)
        except:
                raise ValueError("Не удалось решить уравнение")
        if oxy_part <0 :
                raise ValueError("Массовая доля окислителя - меньше нуля выбереите более эффективное горючее или увеличте запрашиваемый ОБ")
        elif fuel_part <0 :
                raise ValueError("Массовая доля горючего - меньше нуля выбереите более эффективный окислитель или снизьте запрашиваемый ОБ")
        return round(oxy_part,3),round(fuel_part,3)
  


def _calculate_from_components(oxi: Component, fuel: Component, balance: float) -> tuple[float, float]:
    if oxi.demidov_coeff == 0 or fuel.demidov_coeff == 0:
        raise ValueError("Коэффициент Демидова не может быть нулевым")
    x1, x2 = symbols('x1 x2')
    equations = [
        Eq(x1 + x2, 100),
        Eq(x1 / oxi.demidov_coeff - x2 / fuel.demidov_coeff, balance)
    ]

    try:
        solution = nsolve(equations, (x1, x2), (50, 50))
        w_oxi, w_fuel = float(solution[0]), float(solution[1])
    except Exception as e:
        raise RuntimeError(f"Не удалось решить систему: {e}")

    if w_oxi < 0 or w_fuel < 0:
        raise ValueError(f"Отрицательные массовые доли — состав невозможен ")

    return round(w_oxi, 3), round(w_fuel, 3)

#Для дорботки по несколько компонентов
   # for i in comp_ids:
        #         comp=db_comp_get(i)
        #         if comp.type=="oxy":
        #                 dem_oxy+=comp.demidov_coeff
        #                 no_oxy_flag=False
        #         elif comp.type=="fuel":
        #                 dem_fuel+=comp.demidov_coeff
        #                 no_fuel_flag=False
        # if no_oxy_flag:
        #         print("Добавтье хотя бы один окислитель ")
        #         return
        # elif no_fuel_flag:
        #         print("Добавтье хотя бы одно горючее ")
        #         return
       