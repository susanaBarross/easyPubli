

class Users(object):

    def __init__(self,  email: str, pwd: str, id: str = None,name: str = None, last_name: str = None):

        self._id = id
        self.email = email
        self.pwd = pwd
        self.name = name
        self.last_name = last_name

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id