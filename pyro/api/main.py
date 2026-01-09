from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from pyro.core.calculator import oxy_calc
from pyro.data.db_loader import db_comp_get

app=FastAPI(title="Pyrotech Calculator API", version="1.0")

class CalculatorRequest(BaseModel):
    oxidizer_id:int
    fuel_id:int 
    balance:int

class CalculatorResponse(BaseModel):
    oxidizer_name:str
    oxidizer_percent:float
    fuel_name:str
    fuel_percent:float

@app.post('/api/v1/calculate',response_model=CalculatorResponse)
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
