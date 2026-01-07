from pyro.data import db_loader
from pyro.data import models
from pyro.data import loaders
from pyro.core.calculator import oxy_calc
from pyro.ui.tk_ui import run_gui

# db_loader.init_db()
# lib_fuel=loaders.load_library_from_excel("data/comp_lib_fuel.xlsx")
# lib_oxi=loaders.load_library_from_excel("data/comp_lib_oxy.xlsx")
# db_loader.lib_db_insert(lib_oxi)
# db_loader.lib_db_insert(lib_fuel)


if __name__ == "__main__":
    run_gui()
