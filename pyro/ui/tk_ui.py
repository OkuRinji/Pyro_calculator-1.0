import tkinter as tk
from tkinter import ttk,messagebox
from pyro.core.calculator import oxy_calc  # ← только вызов, не логика!
from pyro.data.db_loader import db_get_comps_by_type

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор окислительного баланса")
        self.root.geometry("400x300")

        try:
            self.oxydizers=db_get_comps_by_type('oxy')
            self.fuels=db_get_comps_by_type('fuel')
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить компоненты:\n{e}")
            root.destroy()
            return

        # Поля ввода
        tk.Label(root, text="Выберите окислитель").pack(pady=10)
        self.combo_oxy=ttk.Combobox(root,state='readonly',width=30)
        self.combo_oxy['values']=[name for _,name in self.oxydizers]
        self.combo_oxy.pack()

        tk.Label(root, text="Выберите горючее").pack(pady=10)
        self.combo_fuel=ttk.Combobox(root,state='readonly',width=30)
        self.combo_fuel['values']=[name for _,name in self.fuels]
        self.combo_fuel.pack()
        
        tk.Label(root, text="Желаемый ОБ (%):").pack(pady=5)
        self.entry_balance = tk.Entry(root)
        self.entry_balance.insert(0, "0")
        self.entry_balance.pack()

        # Кнопка
        tk.Button(root, text="Рассчитать", command=self.calculate).pack(pady=15)

        # Результат
        self.result_label = tk.Label(root, text="", fg="blue", font=("Arial", 12))
        self.result_label.pack()

    def calculate(self):
        try:
            oxy_name = self.combo_oxy.get()
            fuel_name = self.combo_fuel.get()
            if not oxy_name or not fuel_name:
                raise ValueError("Выберите окислитель и горючее")
            balance = float(self.entry_balance.get())
            oxy_id=next(id for id , name in self.oxydizers if name==oxy_name )
            fuel_id=next(id for id , name in self.fuels if name==fuel_name )

            w_oxy, w_fuel = oxy_calc(oxy_id, fuel_id, balance)

            self.result_label.config(
                text=f"Результат:\nОкислитель: {w_oxy}%\nГорючее: {w_fuel}%"
            )
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

def run_gui():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()