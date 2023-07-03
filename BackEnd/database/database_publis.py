from database.mongodb_setup import MongoCollection
from models import Publis
from bson import ObjectId
from bson.json_util import dumps, RELAXED_JSON_OPTIONS, loads
import logging


class DatabasePublis(object):

    def __init__(self):
        pass

    def create_publis(self, publis: Publis) -> str:

        try:
            mc = MongoCollection()
            col = mc.publis()
            publi_dict = vars(publis)
            publi_dict.pop("_id")
            publi_dict["user_id"] = ObjectId(publi_dict["user_id"])
            result = col.insert_one(publi_dict).inserted_id
            print("database " + str(result))
            return result

        except Exception as e:
            logging.error("Error: " + str(e))
            return "Error: " + str(e)


    def update_publi(self, publis: Publis) -> str:

        try:
            mc = MongoCollection()
            col = mc.publis()
            publi_dict = vars(publis)
            print(publi_dict)


            result = col.update_one({"_id": ObjectId(publi_dict["_id"]), "user_id": ObjectId(publi_dict["user_id"])}
                                   ,{"$set": {"titulo": publi_dict["titulo"],
                                              "produto_divulgado": publi_dict["produto_divulgado"],
                                              "midia": publi_dict["midia"],
                                              "observacao": publi_dict["observacao"],
                                              "status": publi_dict["status"]
                                              }})
            print("database " + str(result))
            return publi_dict["_id"]

        except Exception as e:
            logging.error("Error: " + str(e))
            return "Error: " + str(e)


    def get_all_publis(self, user_id: str) -> str:

        try:
            mc = MongoCollection()
            col = mc.publis()
            print("call mongo")
            result = col.find({"user_id": ObjectId(user_id)})

            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            logging.error("Error: " + str(e))
            return "Error: " + str(e)


    def get_one_publi(self, user_id: str, publi_id: str) -> str:

        try:
            mc = MongoCollection()
            col = mc.publis()
            print("call mongo")
            result = col.find_one({"_id": ObjectId(publi_id), "user_id": ObjectId(user_id)})

            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            logging.error("Error: " + str(e))
            return "Error: " + str(e)


    def delete_user_publi(self, publis: dict) -> str:

        try:
            mc = MongoCollection()
            col = mc.publis()
            print("call mongo")
            delete_result = ""

            for publi in publis:
                delete_result = col.delete_one({"user_id": ObjectId(publi["user_id"]), "_id":ObjectId(publi["publi_id"])})
                print(delete_result.deleted_count)


            if delete_result.deleted_count > 0:
                return {"result": "Sucesso"}
            else:
                return {"Erro ao tentar deletar a(s) publicações"}

        except Exception as e:
            logging.error("Error: " + str(e))
            return "Error: " + str(e)