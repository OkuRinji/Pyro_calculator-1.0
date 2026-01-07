import tkinter as tk
from tkinter import messagebox
from pyro.core.calculator import oxy_calc  # ← только вызов, не логика!

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор окислительного баланса")
        self.root.geometry("400x300")

        # Поля ввода
        tk.Label(root, text="ID окислителя:").pack(pady=5)
        self.entry_oxy = tk.Entry(root)
        self.entry_oxy.pack()

        tk.Label(root, text="ID горючего:").pack(pady=5)
        self.entry_fuel = tk.Entry(root)
        self.entry_fuel.pack()

        tk.Label(root, text="Желаемый ОБ (%):").pack(pady=5)
        self.entry_balance = tk.Entry(root)
        self.entry_balance.pack()

        # Кнопка
        tk.Button(root, text="Рассчитать", command=self.calculate).pack(pady=15)

        # Результат
        self.result_label = tk.Label(root, text="", fg="blue", font=("Arial", 12))
        self.result_label.pack()

    def calculate(self):
        try:
            oxi_id = int(self.entry_oxy.get())
            fuel_id = int(self.entry_fuel.get())
            balance = float(self.entry_balance.get())

            w_oxi, w_fuel = oxy_calc(oxi_id, fuel_id, balance)

            self.result_label.config(
                text=f"Результат:\nОкислитель: {w_oxi}%\nГорючее: {w_fuel}%"
            )
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

def run_gui():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()