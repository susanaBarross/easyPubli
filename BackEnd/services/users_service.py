from models.Users import Users
from database.database_users import DatabaseUsers
from werkzeug.security import generate_password_hash, check_password_hash
import logging


class UsersService(object):

    def __init__(self):
        pass

    def create_user(self, user: dict) -> str:

        try:

            user_obj = Users(email=user["email"],
                             pwd=generate_password_hash(user["pwd"], method='sha256', salt_length=24)
                             )

            user_db = DatabaseUsers()

            # apply validations
            if user_db.is_user_exists(email=user["email"]) is not None:
                return {"result": "Usuário já possui conta. Por favor faça o login!"}

            # create persistent user
            result = user_db.create_user(user_obj)
            return result

        except Exception as e:
            logging.error("Error: " + str(e))
            return "Error " + str(e)


    def login_user(self, user: dict) -> str:

        try:

            user_obj = Users(email=user["email"],
                             pwd=user["pwd"])

            user_db = DatabaseUsers()

            # apply validations
            if user_db.is_user_exists(email=user_obj.email) is None:
                return {"result":"Usuário não possui conta. Por favor faça o cadastro!"}

            # check if the user has account
            result = user_db.login_user(user_obj)
            if result is None:
                return "Error: Senha inválida"
            else:
                return result

        except Exception as e:
            logging.error("Error: " + str(e))
            return "Error " + str(e)

    def get_user(self, username: str) -> dict:

        try:
            user_db = DatabaseUsers()
            result = user_db.get_user(username=username)
            return result

        except Exception as e:
            logging.error("Error: " + str(e))
            return {}


    def perfil(self, user: dict) -> str:

        try:

            user_obj = Users(email=None,
                             pwd=None,
                             id=user["user_id"],
                             name=user["nome"],
                             last_name=user["sobrenome"])

            print(vars(user_obj))

            user_db = DatabaseUsers()

            # apply validations

            # check if the user has account
            result = user_db.perfil(user_obj)
            if result is None:
                return "Error: Perfil nao atualizdo"
            else:
                return result

        except Exception as e:
            logging.error("Error: " + str(e))
            return "Error " + str(e)

    def perfil_pwd(self, user: dict) -> str:

        try:

            user_db = DatabaseUsers()
            result = user_db.perfil_pwd(user)

            return resul

        except Exception as e:
            logging.error("Error: " + str(e))
            return "Error " + str(e)

    def get_perfil(self, user_id: str) -> dict:

        try:

            user_db = DatabaseUsers()
            print("perfil sevice")
            result = user_db.get_perfil(user_id=user_id)

            return result

        except Exception as e:
            logging.error("Error: " + str(e))
            return "Error " + str(e)

    def perfil_change_pwd(self, user: dict) -> str:

        try:

            user_db = DatabaseUsers()
            result = user_db.perfil_change_pwd(user)

            return result

        except Exception as e:
            logging.error("Error: " + str(e))
            return "Error " + str(e)