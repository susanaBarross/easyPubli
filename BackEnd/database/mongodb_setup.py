from pymongo import MongoClient
import os
import logging


def mongopy_conn():

    try:
        client = MongoClient()

        db = client.easyPlub
        return db
    except Exception as e:
        return "Error " + str(e)


db_conn = mongopy_conn()


class MongoCollection(object):

    def users(self):

        try:
            collection = db_conn.users
            return collection

        except Exception as e:
            logging.error("Error: " + str(e))
            return -1

    def publis(self):

        try:
            collection = db_conn.publis
            return collection

        except Exception as e:
            logging.error("Error: " + str(e))
            return -1

    def products(self):

        try:
            collection = db_conn.products
            return collection

        except Exception as e:
            logging.error("Error: " + str(e))
            return -1

    def links(self):

        try:
            collection = db_conn.links
            return collection

        except Exception as e:
            logging.error("Error: " + str(e))
            return -1


    def chatgpt_answers(self):

        try:
            collection = db_conn.chatgpt_answers
            return collection

        except Exception as e:
            logging.error("Error: " + str(e))
            return -1


if __name__ == '__main__':
    print("test execution of file mongodb")
