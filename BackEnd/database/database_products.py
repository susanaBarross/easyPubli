from database.mongodb_setup import MongoCollection
from models import Products
import logging
from bson import ObjectId
from bson.json_util import dumps, RELAXED_JSON_OPTIONS, loads

class DatabaseProducts(object):

    def __init__(self):
        pass

    def create_product(self, product: Products) -> str:

        try:

            print("debug2 call db produtos create")
            mc = MongoCollection()
            col = mc.products()
            pro_dict = vars(product)
            pro_dict.pop("_id")
            pro_dict["user_id"] = ObjectId(pro_dict["user_id"])
            result = col.insert_one(pro_dict).inserted_id
            print("database " + str(result))
            return result

        except Exception as e:
            logging.error("Error: " + str(e))
            return "Error: " + str(e)

    def update_product(self, product: Products) -> str:

        try:

            print("debug2 call db produtos update")
            mc = MongoCollection()
            col = mc.products()
            product_dict = vars(product)
            print("debug2 update product")
            print(product_dict)

            result = col.update_one({"_id": ObjectId(product_dict["_id"]), "user_id": ObjectId(product_dict["user_id"])}
                                   ,{"$set": {"produto": product_dict["produto"],
                                              "plataforma": product_dict["plataforma"],
                                              "preco_maximo": product_dict["preco_maximo"],
                                              "comissao": product_dict["comissao"],
                                              "qtd_vendida": product_dict["qtd_vendida"],
                                              "faturamento": product_dict["faturamento"],
                                              "status": product_dict["status"],
                                              "divulgacao": product_dict["divulgacao"],
                                              "link": product_dict["link"],
                                              "observacao": product_dict["observacao"]
                                              }})
            print("database " + str(result))
            return product_dict["_id"]

        except Exception as e:
            logging.error("Error: " + str(e))
            return "Error: " + str(e)



    def get_all_products(self, user_id: str) -> str:

        try:
            mc = MongoCollection()
            col = mc.products()
            print("call mongo")
            result = col.find({"user_id": ObjectId(user_id)})

            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            logging.error("Error: " + str(e))
            return "Error: " + str(e)



    def get_one_product(self, user_id: str, product_id: str) -> str:

        try:
            mc = MongoCollection()
            col = mc.products()
            print("call mongo")
            result = col.find_one({"_id": ObjectId(product_id), "user_id": ObjectId(user_id)})

            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            logging.error("Error: " + str(e))
            return "Error: " + str(e)


    def delete_user_product(self, products: dict) -> str:

        try:
            mc = MongoCollection()
            col = mc.products()
            print("call mongo")
            delete_result = ""

            for prd in products:
                delete_result = col.delete_one({"user_id": ObjectId(prd["user_id"]), "_id":ObjectId(prd["product_id"])})
                print(delete_result.deleted_count)


            if delete_result.deleted_count > 0:
                return {"result": "Sucesso"}
            else:
                return {"Erro ao tentar deletar o(s) produto(s)"}

        except Exception as e:
            logging.error("Error: " + str(e))
            return "Error: " + str(e)