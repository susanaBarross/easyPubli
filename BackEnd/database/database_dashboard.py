from database.mongodb_setup import MongoCollection
from models import Links
from bson import ObjectId
from bson.json_util import dumps, RELAXED_JSON_OPTIONS, loads
import logging


class DatabaseDashboard(object):

    def __init__(self):
        pass


    def get_user_dash_info(self, user_id: str) -> str:

        try:
            mc = MongoCollection()
            col_prod = mc.products()
            col_publi = mc.publis()

            # grf1 produtos - group by status
            result = col_prod.aggregate([{"$match": {"user_id": ObjectId(user_id)}},
                                         {"$group": {"_id": "$status",
                                                     "count": {"$sum": 1},
                                                    }}
                                        ])

            g1_series = []
            g1_labels = []
            for r in result:
                g1_series.append(r["count"])
                g1_labels.append(r["_id"].capitalize())

            # grf2 produtos - 4 produtos com maior faturamento
            result = col_prod.aggregate([{"$match": {"user_id": ObjectId(user_id)}},
                                         {"$group": {"_id": "$produto",
                                                     "total": {"$sum": "$faturamento"},
                                                     }},
                                         {"$sort": {"total": -1}}
                                        ])

            g2_data = []
            g2_categories = []
            for key, r in enumerate(result):

                if key > 4:
                    break

                g2_data.append(round(r["total"],2))
                g2_categories.append(r["_id"])

            # grf3 produtos - group by produtos ativos por plataforma
            result = col_prod.aggregate([{"$match": {"user_id": ObjectId(user_id), "status": "ativo"}},
                                         {"$group": {"_id": "$plataforma",
                                                     "count": {"$sum": 1},
                                                    }}
                                        ])

            g3_series = []
            g3_labels = []
            for r in result:
                g3_series.append(r["count"])
                g3_labels.append(r["_id"])

            # grf4 produtos - group by dos 4 primeiras plataformas com maior faturamento
            result = col_prod.aggregate([{"$match": {"user_id": ObjectId(user_id)}},
                                         {"$group": {"_id": "$plataforma",
                                                     "total": {"$sum": "$faturamento"},
                                                    }}
                                        ])

            g4_data = []
            g4_categories = []
            for r in result:
                g4_data.append(round(r["total"],2))
                g4_categories.append(r["_id"])

            # grf5 publi - group by status
            result = col_publi.aggregate([{"$match": {"user_id": ObjectId(user_id)}},
                                          {"$group": {"_id": "$status",
                                                      "count": {"$sum": 1},
                                                     }}
                                    ])

            g5_series = []
            g5_labels = []
            for r in result:
                if r["_id"] == "analise":
                    r["_id"] = "Análise"

                if r["_id"] == "producao":
                    r["_id"] = "Produção"

                if r["_id"] == "publicado":
                    r["_id"] = "Publicado"

                g5_series.append(r["count"])
                g5_labels.append(r["_id"])

            # grf6 publi - group by de publicacoes por midia
            result = col_publi.aggregate([{"$match": {"user_id": ObjectId(user_id)}},
                                          {"$group": {"_id": "$midia",
                                                      "count": {"$sum": 1},
                                                     }}
                                    ])

            g6_data = []
            g6_categories = []
            for r in result:
                g6_data.append(r["count"])
                g6_categories.append(r["_id"])


            return dumps( {"grf1":{"series": g1_series,
                                   "labels": g1_labels}
                         , "grf2":{"data": g2_data,
                                   "categories": g2_categories}
                         , "grf3":{"series": g3_series,
                                   "labels": g3_labels}
                         , "grf4":{"data": g4_data,
                                   "categories": g4_categories }
                         , "grf5":{"series": g5_series,
                                   "labels": g5_labels }
                         , "grf6":{"data": g6_data,
                                   "categories": g6_categories}
                     } , json_options=RELAXED_JSON_OPTIONS)


        except Exception as e:
            logging.error("Error: " + str(e))
            return "Error: " + str(e)


