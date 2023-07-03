from models.Links import Links
from database.database_links import DatabaseLinks
from services.log_service import log

import logging


class LinksService(object):

    def __init__(self):
        pass

    def merge_links(self, links: dict) -> str:

        try:
            id = None
            if "link_id" in links:
                id = links["link_id"]

            link_obj = Links(id=id,
                             reference = links["referencia"],
                             links = links["links"],
                             user_id=links["user_id"])

            link_db = DatabaseLinks()


            if link_obj.id is None or link_obj.id == "":
                print("debug3 create publis")
                result = link_db.create_links(link_obj)
            else:
                print("debug3 update publis")
                result = link_db.update_links(link_obj)

            print("service " + str(result))
            return result

        except Exception as e:
            logging.error("Error: " + str(e))
            return "Error " + str(e)



    def get_user_links(self, user_id: str) -> str:

        try:


            link_db = DatabaseLinks()

            # apply validations

            # create persistent product
            print("debug1 call db ")
            result = link_db.get_all_links(user_id=user_id)
            print(result)
            return result

        except Exception as e:
            logging.error("Error: " + str(e))
            return "Error " + str(e)


    def get_user_one_links(self, user_id: str, links_id: str) -> str:

        try:


            link_db = DatabaseLinks()

            # apply validations

            # create persistent product
            print("debug1 call db ")
            result = link_db.get_one_links(user_id=user_id, links_id=links_id)
            print(result)
            return result

        except Exception as e:
            logging.error("Error: " + str(e))
            return "Error " + str(e)


    def delete_user_links(self, links: dict) -> str:

        try:

            log("test")

            link_db = DatabaseLinks()

            # apply validations

            # create persistent product
            print("link debug1 call db ")
            result = link_db.delete_user_links(links=links)
            print(result)
            return result

        except Exception as e:
            logging.error("Error: " + str(e))
            return "Error " + str(e)