
import tkinter as tk
from tkinter import messagebox

class Calculadora:
    def somar(self, a, b): return a + b
    def subtrair(self, a, b): return a - b
    def multiplicar(self, a, b): return a * b
    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Divisão por zero")
        return a / b

class CalculadoraGUI:
    def __init__(self, root):
        self.calc = Calculadora()
        root.title("Calculadora POO")

        tk.Label(root, text="Número 1").grid(row=0, column=0)
        tk.Label(root, text="Número 2").grid(row=1, column=0)

        self.n1 = tk.Entry(root)
        self.n2 = tk.Entry(root)
        self.n1.grid(row=0, column=1)
        self.n2.grid(row=1, column=1)

        tk.Button(root, text="+", command=self.somar).grid(row=2, column=0)
        tk.Button(root, text="-", command=self.subtrair).grid(row=2, column=1)
        tk.Button(root, text="*", command=self.multiplicar).grid(row=3, column=0)
        tk.Button(root, text="/", command=self.dividir).grid(row=3, column=1)

    def valores(self):
        return float(self.n1.get()), float(self.n2.get())

    def somar(self): self._executar(self.calc.somar)
    def subtrair(self): self._executar(self.calc.subtrair)
    def multiplicar(self): self._executar(self.calc.multiplicar)
    def dividir(self): self._executar(self.calc.dividir)

    def _executar(self, operacao):
        try:
            a, b = self.valores()
            messagebox.showinfo("Resultado", operacao(a, b))
        except Exception as e:
            messagebox.showerror("Erro", e)

if __name__ == '__main__':
    root = tk.Tk()
    CalculadoraGUI(root)
    root.mainloop()
