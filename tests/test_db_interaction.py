import pytest
from pyro.data.models import Component
from pyro.data import db_loader
from pydantic import ValidationError

pytest.mark.parametrize('component', [
        Component(type="топливо",name="Mg",enthalpy=0.0,demidov_coeff=1.52,molar_mass=24.32,formula={"Mg": 100.0}),
        Component(type="fuel",name="123",enthalpy=0.0,demidov_coeff=1.52,molar_mass=24.32,formula={"Mg": 100.0}),
        Component(type="fuel",name="Mg",enthalpy='0.0',demidov_coeff=1.52,molar_mass=24.32,formula={"Mg": 100.0}),
        Component(type="fuel",name="Mg",enthalpy=0.0,demidov_coeff='1.52',molar_mass=24.32,formula={"Mg": 100.0}),
        Component(type="fuel",name="Mg",enthalpy=0.0,demidov_coeff=1.52,molar_mass='24.32',formula={"Mg": 100.0}),
        Component(type="fuel",name="Mg",enthalpy=0.0,demidov_coeff=1.52,molar_mass=24.32,formula=["Mg", 100.0]),
    ])
 
def test_insert_component(component):
    with pytest.raises(ValidationError | TypeError):
            db_loader.comp_insert(component)



