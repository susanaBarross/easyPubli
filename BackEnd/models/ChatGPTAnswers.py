

class ChatGPTAnswer(object):

    def __init__(self, id: str,pergunta: str, classificacao : str, produto_relacionado : str, midia : str, resposta: str,
                 user_id:str):

        self._id = id
        self.pergunta = pergunta
        self.classificacao = classificacao
        self.produto_relacionado = produto_relacionado
        self.midia = midia
        self.resposta = resposta
        self.user_id = user_id

    @property
    def id(self):
        return self._id

