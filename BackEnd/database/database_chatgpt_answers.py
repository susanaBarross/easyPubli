from database.mongodb_setup import MongoCollection
from models import ChatGPTAnswers
from bson import ObjectId
from bson.json_util import dumps, RELAXED_JSON_OPTIONS, loads
import logging


class DatabaseChatGPTAnswers(object):

    def __init__(self):
        pass

    def create_gpt_answers(self, answers: ChatGPTAnswers) -> str:

        try:
            mc = MongoCollection()
            col = mc.chatgpt_answers()
            answers_dict = vars(answers)
            answers_dict.pop("_id")
            answers_dict["user_id"] = ObjectId(answers_dict["user_id"])
            result = col.insert_one(answers_dict).inserted_id
            print("database " + str(result))
            return result

        except Exception as e:
            logging.error("Error: " + str(e))
            return "Error: " + str(e)


    def update_answers(self, answers: ChatGPTAnswers) -> str:

        try:
            mc = MongoCollection()
            col = mc.chatgpt_answers()
            answers_dict = vars(answers)
            print(answers_dict)


            result = col.update_one({"_id": ObjectId(answers_dict["_id"]), "user_id": ObjectId(answers_dict["user_id"])}
                                   ,{"$set": {"pergunta": answers_dict["pergunta"],
                                              "classificacao": answers_dict["classificacao"],
                                              "produto_relacionado": answers_dict["produto_relacionado"],
                                              "midia": answers_dict["midia"],
                                              "resposta": answers_dict["resposta"]
                                              }})
            print("database " + str(result))
            return result

        except Exception as e:
            logging.error("Error: " + str(e))
            return "Error: " + str(e)


    def get_all_answers(self, user_id: str) -> str:

        try:
            mc = MongoCollection()
            col = mc.chatgpt_answers()
            print("call mongo")
            print(user_id)
            result = col.find({"user_id": ObjectId(user_id)})

            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            logging.error("Error: " + str(e))
            return "Error: " + str(e)


    def get_one_answer(self, user_id: str, chatgpt_answer_id: str) -> str:

        try:
            mc = MongoCollection()
            col = mc.chatgpt_answers()
            print("call mongo")
            print("answer id: " + chatgpt_answer_id)
            print("user id: " + user_id)
            result = col.find_one({"_id": ObjectId(chatgpt_answer_id), "user_id": ObjectId(user_id)})

            return dumps(result, json_options=RELAXED_JSON_OPTIONS)

        except Exception as e:
            logging.error("Error: " + str(e))
            return "Error: " + str(e)


    def delete_user_answers(self, answers: dict) -> str:

        try:
            mc = MongoCollection()
            col = mc.chatgpt_answers()
            print("call mongo")
            delete_result = ""

            for ans in answers:
                delete_result = col.delete_one({"user_id": ObjectId(ans["user_id"]), "_id":ObjectId(ans["chatgpt_id"])})
                print(delete_result.deleted_count)


            if delete_result.deleted_count > 0:
                return {"result": "Sucesso"}
            else:
                return {"Erro ao tentar deletar a(s) respostas"}

        except Exception as e:
            logging.error("Error: " + str(e))
            return "Error: " + str(e)