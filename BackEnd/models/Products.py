

class Products(object):

    def __init__(self, id: str,produto: str, plataforma : str, comissao : float, qtd_vendida : int, status : str,
                 user_id: str, preco_maximo : float = None, divulgacao : str = None, link: str = None,
                 observacao: str = None):

        self._id = id
        self.produto = produto
        self.plataforma = plataforma
        self.preco_maximo = preco_maximo
        self.comissao = comissao
        self.qtd_vendida = qtd_vendida
        self.faturamento = round(qtd_vendida * comissao, 2)
        self.status = status
        self.divulgacao = divulgacao
        self.link = link
        self.observacao = observacao
        self.user_id = user_id

    @property
    def id(self):
        return self._id



