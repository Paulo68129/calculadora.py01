
        class Calculadora:
            def somar(self, a, b):
                return a + b

            def subtrair(self, a, b):
                return a - b

            def multiplicar(self, a, b):
                return a * b

            def dividir(self, a, b):
                if b == 0:
                    raise ValueError("Divisão por zero")
                return a / b


        class AplicacaoCalculadora:
            def __init__(self):
                self.calc = Calculadora()

            def executar(self):
                while True:
                    print("
1- Somar | 2- Subtrair | 3- Multiplicar | 4- Dividir | 0- Sair")
                    opcao = input("Escolha uma opção: ")

                    if opcao == '0':
                        break

                    try:
                        a = float(input("Digite o primeiro número: "))
                        b = float(input("Digite o segundo número: "))
                    except ValueError:
                        print("Entrada inválida")
                        continue

                    try:
                        if opcao == '1':
                            print("Resultado:", self.calc.somar(a, b))
                        elif opcao == '2':
                            print("Resultado:", self.calc.subtrair(a, b))
                        elif opcao == '3':
                            print("Resultado:", self.calc.multiplicar(a, b))
                        elif opcao == '4':
                            print("Resultado:", self.calc.dividir(a, b))
                        else:
                            print("Opção inválida")
                    except ValueError as e:
                        print(e)


        if __name__ == '__main__':
            AplicacaoCalculadora().executar()
