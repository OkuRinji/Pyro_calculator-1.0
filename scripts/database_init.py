from pyro.data import db_loader,loaders
db_loader.init_db()
lib_fuel=loaders.load_library_from_excel("data/comp_lib_fuel.xlsx")
lib_oxi=loaders.load_library_from_excel("data/comp_lib_oxy.xlsx")
db_loader.lib_db_insert(lib_oxi)
db_loader.lib_db_insert(lib_fuel)

