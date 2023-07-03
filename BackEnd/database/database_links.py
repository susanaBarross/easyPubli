from database.mongodb_setup import MongoCollection
from models import Links
from bson import ObjectId
from bson.json_util import dumps, RELAXED_JSON_OPTIONS, loads
import logging


class DatabaseLinks(object):

    def __init__(self):
        pass

    def create_links(self, links: Links) -> str:

        try:
            mc = MongoCollection()
            col = mc.links()
            links_dict = vars(links)
            links_dict.pop("_id")
            links_dict["user_id"] = ObjectId(links_dict["user_id"])
            print("link datababse")
            print(links_dict)
            result = col.insert_one(links_dict).inserted_id
            print("database " + str(result))
            return result

        except Exception as e:
            logging.error("Error: " + str(e))
            return "Error: " + str(e)


    def update_links(self, links: Links) -> str:

        try:
            mc = MongoCollection()
            col = mc.links()
            links_dict = vars(links)
            print(links_dict)


            result = col.update_one({"_id": ObjectId(links_dict["_id"]), "user_id": ObjectId(links_dict["user_id"])}
                                   ,{"$set": {"reference": links_dict["reference"],
                                              "links": links_dict["links"]
                                              }})
            print("database " + str(result))
            return links_dict["_id"]

        except Exception as e:
            logging.error("Error: " + str(e))
            return "Error: " + str(e)


    def get_all_links(self, user_id: str) -> str:

        try:
            mc = MongoCollection()
            col = mc.links()
            print("call mongo")
            print(user_id)
            result = col.find({"user_id": ObjectId(user_id)})

            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            logging.error("Error: " + str(e))
            return "Error: " + str(e)


    def get_one_links(self, user_id: str, links_id: str) -> str:

        try:
            mc = MongoCollection()
            col = mc.links()
            print("call mongo")
            result = col.find_one({"_id": ObjectId(links_id), "user_id": ObjectId(user_id)})

            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            logging.error("Error: " + str(e))
            return "Error: " + str(e)


    def delete_user_links(self, links: dict) -> str:

        try:
            mc = MongoCollection()
            col = mc.links()
            print("call mongo")
            delete_result = ""
            print("link to be deleted")
            print(links)

            for link in links:
                print("start deleting")
                delete_result = col.delete_one({"user_id": ObjectId(link["user_id"]), "_id":ObjectId(link["link_id"])})
                print(delete_result.deleted_count)


            if delete_result.deleted_count > 0:
                return {"result": "Sucesso"}
            else:
                return {"Erro ao tentar deletar o(s) Links"}

        except Exception as e:
            logging.error("Error: " + str(e))
            return "Error: " + str(e)