import os
import logging
from database.database_chatgpt_answers import DatabaseChatGPTAnswers
from models.ChatGPTAnswers import ChatGPTAnswer
import openai
from services.log_service import log

class ChatGPTService(object):

    def __init__(self):
        pass

    def merge_answer(self, answer: dict) -> str:

        try:

            id = answer["chatgpt_id"]
            if id == "":
                id = None

            ans_obj = ChatGPTAnswer(id=id,
                                    pergunta = answer["pergunta"],
                                    classificacao = answer["classificacao"],
                                    produto_relacionado = answer["produto_relacionado"],
                                    midia = answer["midia"],
                                    resposta=answer["resposta"],
                                    user_id=answer["user_id"])

            answer_db = DatabaseChatGPTAnswers()

            # apply validations

            # create persistent product
            if ans_obj.id is None or ans_obj.id == "":
                print("debug3 create chat")
                result = answer_db.create_gpt_answers(ans_obj)
            else:
                print("debug3 update chat")
                result = answer_db.update_answers(ans_obj)

            print("service " + str(result))
            return result

        except Exception as e:
            logging.error("Error: " + str(e))
            return "Error " + str(e)



    def get_user_answers(self, user_id: str) -> str:

        try:


            answer_db = DatabaseChatGPTAnswers()

            # apply validations

            # create persistent product
            print("debug1 call db ")
            result = answer_db.get_all_answers(user_id=user_id)
            print(result)
            return result

        except Exception as e:
            logging.error("Error: " + str(e))
            return "Error " + str(e)


    def get_user_one_answer(self, user_id: str, answer_id: str) -> str:

        try:


            answer_db = DatabaseChatGPTAnswers()

            # apply validations

            # create persistent product
            print("debug1 call db ")
            result = answer_db.get_one_answer(user_id=user_id, chatgpt_answer_id=answer_id)
            print(result)
            return result

        except Exception as e:
            logging.error("Error: " + str(e))
            return "Error " + str(e)


    def delete_user_answer(self, answers: dict) -> str:

        try:


            answer_db = DatabaseChatGPTAnswers()

            # apply validations

            # create persistent product
            print("debug1 call db ")
            result = answer_db.delete_user_answers(answers=answers)
            print(result)
            return result

        except Exception as e:
            logging.error("Error: " + str(e))
            return "Error " + str(e)

    @staticmethod
    def get_api_control() -> str:

        return os.environ.get("API_CONTROL")


    def call_chatgpt(self, question: str) -> str:

        log("start chatgpt call")
        openai.api_key = self.get_api_control()

        print(openai.api_key)

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                      {"role": "user", "content": question["pergunta"]},
            ]
        )

        result = ''
        for choice in response.choices:
            result += choice.message.content

        log("chatgpt resposta " + result)

        return {"result": "Sucesso",  "answer": result}