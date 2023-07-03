

class Publis(object):

    def __init__(self, id: str,titulo: str, midia : str, user_id: str, status:str,
                 produto_divulgado : str = None, observacao : str = None):

        self._id = id
        self.titulo = titulo
        self.produto_divulgado = produto_divulgado
        self.midia = midia
        self.observacao = observacao
        self.user_id = user_id
        self.status = status



    @property
    def id(self):
        return self._id

