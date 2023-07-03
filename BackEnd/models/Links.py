

class Links(object):

    def __init__(self, reference: str, links : str, user_id: str, id: str):

        self._id = id
        self.reference = reference
        self.links = links
        self.user_id = user_id

    @property
    def id(self):
        return self._id

