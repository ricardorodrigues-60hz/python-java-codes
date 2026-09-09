# - Pub/Sub -
# http://www.code2succeed.com/pub-sub/
# https://www.oreilly.com/library/view/learning-javascrip-
# https://en.wikipedia.org/wiki/Publish-sub
# https://youtu.be/sbCJucr8aJg?list=PLOQgLBuj2-3IPHFlBmqhtbM4vLJg9tob4


from typing import Dict, Set, List
class Publisher:
    def __init__(self, topico, pub_sub):
        self.topico = topico
        self.mensagens = []
        self.pub = pub_sub

    def publicar(self, mensagem):
        msg = {'topico': self.topico, 'mensagem': mensagem}
        self.pub.receber_mensagem(msg)


class Inscriber:
    def __init__(self, nome):
        self.nome = nome


    def atualizar(self, topico, mensagem):
        print(f'|{topico}|\t{self.nome} recebeu: "{mensagem}"')


class PubSub:
    def __init__(self):
        self.inscrito_por_topico: Dict[str, Set] = {}
        self.fila_de_mensagem: List[Dict[str, str]] = []


    def adicionar_inscrito(self, topico, inscrito):
        if topico in self.inscrito_por_topico:
            self.inscrito_por_topico[topico].add(inscrito)
        else:
            self.inscrito_por_topico[topico] = {inscrito}


    def receber_mensagem(self, mensagem: Dict[str, str]):
        """{'topico': xpto, 'mensagem': xpto}"""
        self.fila_de_mensagem.append(mensagem)


    def _enviar_mensagens_por_topico(self, topico, mensagem):
        for inscrito in self.inscrito_por_topico[topico]:
            inscrito.atualizar(topico, mensagem)


    def broadcast(self):
        for msg in self.fila_de_mensagem:
            self._enviar_mensagens_por_topico(msg['topico'], msg['mensagem'])

        self.fila_de_mensagem = []


eduardo = Inscriber('Eduardo')
ricardo = Inscriber('Ricardo')
jose = Inscriber('josé')

bus = PubSub()

blog_1 = Publisher('Blog do zé', bus)
blog_2 = Publisher('PSF', bus)

bus.adicionar_inscrito('PSF', eduardo)
bus.adicionar_inscrito('PSF', jose)
bus.adicionar_inscrito('PSF', ricardo)
bus.adicionar_inscrito('Blog do zé', jose)

blog_1.publicar('Zé foi a feira')
blog_2.publicar('Zé, membr da psf foi a feira')

bus.broadcast()
