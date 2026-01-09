from pyro.core.calculator import oxy_calc

def test_balanced_mixture():
    w1, w2 = oxy_calc(1, 1, 0.0)
    assert abs(w1 + w2 - 100) < 0.1
    assert w1 > 0 and w2 > 0