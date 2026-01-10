import pytest
from pyro.data.models import Component
from pyro.data import db_loader
from pydantic import ValidationError


def test_zero_component(component):
        with pytest.raises(ValidationError , TypeError):
                db_loader.comp_insert(component)








