from models.Products import Products
from database.database_products import DatabaseProducts

import logging


class ProductsService(object):

    def __init__(self):
        pass

    def merge_product(self, product: dict) -> str:

        try:

            print("debug2 call db produtos object 1")
            id = product["product_id"]
            if id == "":
                id = None

            preco_max = product["preco_maximo"]

            if preco_max == "":
                preco_max = 0

            product_obj = Products(id=id,
                                   produto = product["produto"],
                                   plataforma = product["plataforma"],
                                   preco_maximo = float(preco_max),
                                   comissao = float(product["comissao"]),
                                   qtd_vendida = int(product["qtd_vendida"]),
                                   status = product["status"],
                                   divulgacao = product["divulgacao"],
                                   link = product["link"],
                                   observacao = product["observacao"],
                                   user_id = product["user_id"])



            product_db = DatabaseProducts()

            # apply validations

            # create persistent product



            if product_obj.id is None or product_obj.id == "":
                print("debug 3 create product")
                result = product_db.create_product(product_obj)
            else:
                result = product_db.update_product(product_obj)

            print("service " + str(result))
            return result

        except Exception as e:
            logging.error("Error: " + str(e))
            return "Error " + str(e)


    def get_user_products(self, user_id: str) -> str:

        try:


            prod_db = DatabaseProducts()

            # apply validations

            # create persistent product
            print("debug1 call db ")
            result = prod_db.get_all_products(user_id=user_id)
            print(result)
            return result

        except Exception as e:
            logging.error("Error: " + str(e))
            return "Error " + str(e)

    def get_user_one_product(self, user_id: str, product_id: str) -> str:

        try:

            product_db = DatabaseProducts()

            # apply validations

            # create persistent product
            print("debug1 call db ")
            result = product_db.get_one_product(user_id=user_id, product_id=product_id)
            print(result)
            return result

        except Exception as e:
            logging.error("Error: " + str(e))
            return "Error " + str(e)

    def delete_user_product(self, products: dict) -> str:

        try:

            product_db = DatabaseProducts()

            # apply validations

            # create persistent product
            print("debug1 call db ")
            result = product_db.delete_user_product(products=products)
            print(result)
            return result

        except Exception as e:
            logging.error("Error: " + str(e))
            return "Error " + str(e)