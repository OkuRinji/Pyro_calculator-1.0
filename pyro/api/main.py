from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from pyro.core.calculator import oxy_calc
from pyro.data.db_loader import db_comp_get,db_get_comps_by_type

app=FastAPI(title="Pyrotech Calculator API", version="1.0")

class ComponentItem(BaseModel):
    id:int
    name:str

class CalculatorRequest(BaseModel):
    oxidizer_id:int
    fuel_id:int 
    balance:int

class CalculatorResponse(BaseModel):
    oxidizer_name:str
    oxidizer_percent:float
    fuel_name:str
    fuel_percent:float

@app.post('/api/v1/calculate',response_model=CalculatorResponse,summary="Рассчитать окислительный баланс")
async def calculate(request:CalculatorRequest):
    try:
        oxy=db_comp_get(request.oxidizer_id,'oxy')
        fuel=db_comp_get(request.fuel_id,"fuel")

        w_oxi,w_fuel=oxy_calc(
            request.oxidizer_id,
            request.fuel_id,
            request.balance
        )

        return CalculatorResponse(
            oxidizer_name=oxy.name,
            oxidizer_percent=w_oxi,
            fuel_name=fuel.name,
            fuel_percent=w_fuel
        )

    except Exception as e :
        raise HTTPException(status_code=400 ,detail=e)
    except Exception as e :
        raise HTTPException(status_code=500 ,detail='Internal error')
@app.get('/api/v1/get_oxidizers',response_model=list[ComponentItem],summary="Получить список окислителей")
async def get_oxidizers():
    try:
        rows=db_get_comps_by_type("oxy")
        return [ComponentItem(id=id,name=name) for id,name in rows]
    except Exception as e:
        raise HTTPException(status_code=500,detail=f"Ошибка загрузки окислителей {e}")
@app.get('/api/v1/get_fuels',response_model=list[ComponentItem],summary="Получить список горючих")
async def get_oxidizers():
    try:
        rows=db_get_comps_by_type("fuel")
        return [ComponentItem(id=id,name=name) for id,name in rows]
    except Exception as e:
        raise HTTPException(status_code=500,detail=f"Ошибка загрузки горючих {e}")