from models.Links import Links
from database.database_dashboard import DatabaseDashboard

import logging


class DashboardService(object):


    def __init__(self):
        pass


    def get_user_dash_info(self, user_id: str) -> str:

        try:


            dash_db = DatabaseDashboard()

            # apply validations

            # create persistent product
            print("debug1 call db ")
            result = dash_db.get_user_dash_info(user_id=user_id)
            print(result)
            return result

        except Exception as e:
            logging.error("Error: " + str(e))
            return "Error " + str(e)





