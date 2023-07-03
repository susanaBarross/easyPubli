from database.mongodb_setup import MongoCollection
from models import Users
import logging
from werkzeug.security import generate_password_hash, check_password_hash
from bson import ObjectId
from bson.json_util import dumps, RELAXED_JSON_OPTIONS, loads

class DatabaseUsers(object):

    def __init__(self):
        pass

    def get_user(self, username: str) -> dict:

        try:
            mc = MongoCollection()
            col = mc.users()
            return col.find_one({"username": username})

        except Exception as e:
            logging.error("Error: " + str(e))
            print(e)

    def create_user(self, user: Users ) -> str:

        try:
            mc = MongoCollection()
            col = mc.users()
            user_dict = vars(user)
            user_dict.pop("_id")
            result = col.insert_one(user_dict).inserted_id

            return {"result": "Sucesso"}

        except Exception as e:
            logging.error("Error: " + str(e))
            return "Error: " + str(e)


    def is_user_exists(self, email: str) -> str:

        try:
            mc = MongoCollection()
            col = mc.users()
            return col.find_one({"email": email})

        except Exception as e:
            logging.error("Error: " + str(e))
            print(e)


    def login_user(self, user: Users) -> str:

        try:
            mc = MongoCollection()
            col = mc.users()
            user_dict = vars(user)
            user_check = col.find({"email": user_dict["email"]})
            for u in user_check:
                if check_password_hash(u["pwd"], user_dict["pwd"]):
                    return {"_id": str(u["_id"]), "name": u["name"], "last_name": u["last_name"]}
                else:
                    return "Error: Senha inválida"

        except Exception as e:
            logging.error("Error: " + str(e))
            print(e)

    def perfil(self, user: Users) -> str:

        try:
            mc = MongoCollection()
            col = mc.users()
            user_dict = vars(user)
            user_dict.pop("email")
            user_dict.pop("pwd")
            print(user_dict["_id"])
            user_check = col.update_one({"_id": ObjectId(user_dict["_id"])},{"$set": {"name": user_dict["name"],
                                                                                      "last_name": user_dict["last_name"]}})

            return {"result":"Sucesso"}

        except Exception as e:
            logging.error("Error: " + str(e))
            print(e)


    def get_perfil(self, user_id: str) -> dict:

        try:
           mc = MongoCollection()
           col = mc.users()

           user = col.find_one({"_id": ObjectId(user_id)},{"email": 0, "pwd": 0})
           print(user)
           return user

        except Exception as e:
            logging.error("Error: " + str(e))
            print(e)

    def perfil_change_pwd(self, user: dict) -> str:

        try:
           mc = MongoCollection()
           col = mc.users()

           user_check = col.update_one({"_id": ObjectId(user["user_id"])},
                                       {"$set": {"pwd": generate_password_hash(user["nova_senha"], method='sha256', salt_length=24)}})
           return {"result":"Sucesso"}

        except Exception as e:
            logging.error("Error: " + str(e))
            print(e)
