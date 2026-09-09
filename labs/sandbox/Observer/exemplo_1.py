# class Observador:
#     def __init__(self, nome):
#         self.nome = nome


#     def atualizar(self, mensangem):
#         """Fazer o que quiser com a msg."""
#         print(f'|{self.nome}| recebeu {mensangem}')

# class Ricardo(Observador):
#     def __init__(self):
#         self.nome = 'Ricardo'

#     ...

# --Observavel--
class Passaro:
    def __init__(self):
        self.observadores = []


    def adicionar_observadores(self, observador):
        self.observadores.append(observador)


    def notificar_observadores(self, msg):
        for observador in self.observadores:
            # observador.atualizar(msg)
            observador(msg)      


# ricardo = Observador('Ricardo')
# eduardo = Observador('Eduardo')
# fabricio = Observador('Fabricio')

# passaro = Passaro()
# passaro.adicionar_observadores(ricardo)
# passaro.adicionar_observadores(eduardo)
# passaro.adicionar_observadores(fabricio)

# passaro.notificar_observadores('Estou voando')

# --Push com funções--

def observador_ricardo(mensagem):
    print(f'Observador Ricardo recebeu a mensagem: {mensagem}')


def observador_eduardo(mensagem):
    print(f'Observador Eduardo recebeu a mensagem: {mensagem}')


obs = Passaro()
obs.adicionar_observadores(observador_ricardo)
obs.adicionar_observadores(observador_eduardo)
obs.notificar_observadores('O passaro abriu asas')