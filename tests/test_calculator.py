from pyro.core.calculator import oxy_calc,_calculate_from_components
import pytest
from pyro.data.models import Component

@pytest.fixture
def nh4no3():
    return Component(
        type="oxy",
        name="NH4NO3",
        enthalpy=-1090.2,
        demidov_coeff=5.003,
        molar_mass=128.74,
        formula={"O": 37.4, "H": 50.0, "N": 25.0}
    )

@pytest.fixture
def mg():
    return Component(
        type="fuel",
        name="Mg",
        enthalpy=0.0,
        demidov_coeff=1.52,
        molar_mass=24.32,
        formula={"Mg": 100.0}
    )

class TestBalanceCalculator():
    def test_zero_balance(self,nh4no3, mg):
        w_oxi, w_fuel = _calculate_from_components(nh4no3, mg, balance=0.0)
        
        # Проверяем, что доли положительные
        assert w_oxi > 0
        assert w_fuel > 0
        
        # Проверяем, что сумма ~100%
        assert abs(w_oxi + w_fuel - 100) < 0.1

    # Тест 2: нулевой коэффициент → ошибка
    def test_zero_demidov_coeff(self,nh4no3):
        bad_fuel = Component(type='fuel',name="Bad",enthalpy= 999,demidov_coeff= 0,molar_mass= 0.0,formula={})
        with pytest.raises(ValueError, match="не может быть нулевым"):
            _calculate_from_components(nh4no3, bad_fuel, 0.0)

    # Тест 3: физически невозможный ОБ → отрицательные доли
    def test_impossible_balance(self,nh4no3, mg):
        with pytest.raises(ValueError, match="Отрицательные"):
            _calculate_from_components(nh4no3, mg, balance=1000.0)


