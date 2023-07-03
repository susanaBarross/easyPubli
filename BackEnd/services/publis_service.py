from models.Publis import Publis
from database.database_publis import DatabasePublis

import logging


class PublisService(object):

    def __init__(self):
        pass

    def merge_publi(self, publi: dict) -> str:

        try:

            id = publi["publi_id"]
            if id == "":
                id = None

            publi_obj = Publis(id=id,
                               titulo = publi["titulo"],
                               produto_divulgado = publi["produto_divulgado"],
                               midia = publi["midia"],
                               observacao = publi["observacao"],
                               user_id=publi["user_id"],
                               status=publi["status"])

            publi_db = DatabasePublis()

            # apply validations

            # create persistent product
            if publi_obj.id is None or publi_obj.id == "":
                print("debug3 create publis")
                result = publi_db.create_publis(publi_obj)
            else:
                print("debug3 update publis")
                result = publi_db.update_publi(publi_obj)

            print("service " + str(result))
            return result

        except Exception as e:
            logging.error("Error: " + str(e))
            return "Error " + str(e)



    def get_user_publis(self, user_id: str) -> str:

        try:


            publi_db = DatabasePublis()

            # apply validations

            # create persistent product
            print("debug1 call db ")
            result = publi_db.get_all_publis(user_id=user_id)
            print(result)
            return result

        except Exception as e:
            logging.error("Error: " + str(e))
            return "Error " + str(e)


    def get_user_one_publi(self, user_id: str, publi_id: str) -> str:

        try:


            publi_db = DatabasePublis()

            # apply validations

            # create persistent product
            print("debug1 call db ")
            result = publi_db.get_one_publi(user_id=user_id, publi_id=publi_id)
            print(result)
            return result

        except Exception as e:
            logging.error("Error: " + str(e))
            return "Error " + str(e)


    def delete_user_publi(self, publis: dict) -> str:

        try:


            publi_db = DatabasePublis()

            # apply validations

            # create persistent product
            print("debug1 call db ")
            result = publi_db.delete_user_publi(publis=publis)
            print(result)
            return result

        except Exception as e:
            logging.error("Error: " + str(e))
            return "Error " + str(e)