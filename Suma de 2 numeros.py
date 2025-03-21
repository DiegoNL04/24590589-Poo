"""
            Ingenieria en Sistemas Computacionales
                Aguileta Argueta Mario Damián 
                        24590347
            Programación Orientada a Objetos

                    PROGRAMA HECHO EN CLASE 
                Y REVISADO EL 5 DE MARZO DE 2025
"""

#?Programa hecho con la estructura de POO sin paso de parametros
#?Donde solicitamos dos numeros dentro de la clase y los sumamos para mostrar el resultado

class SumaNumeros:
    def __init__(self):
        self.n1 = 0
        self.n2 = 0
        self.resultado = 0

    def pedir_numeros(self):
        self.n1 = float(input("Introduce el primer número: "))
        self.n2 = float(input("Introduce el segundo número: "))

    def sumar(self):
        self.resultado = self.n1 + self.n2

    def mostrar_resultado(self):
        print(f"La suma de {self.n1} y {self.n2} es: {self.resultado}")

mi_suma = SumaNumeros()
mi_suma.pedir_numeros()
mi_suma.sumar()
mi_suma.mostrar_resultado()
