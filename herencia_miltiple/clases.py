class A:
    def metodo_a(self):
        print('Este es de la clase A')

class B:
    def metodo_b(self):
        print('Este es de la calse B')

class C(A, B):
    def metodo_c(self):
        print('Este de la clase C')