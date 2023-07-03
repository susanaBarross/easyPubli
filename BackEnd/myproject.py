from flask import Flask, request, jsonify
from flask_cors import CORS
from bson.json_util import dumps
from services.users_service import UsersService
from services.publis_service import PublisService
from services.product_service import ProductsService
from services.links_service import LinksService
from services.chatgpt_service import ChatGPTService
from services.dashboard_service import DashboardService
import logging


app = Flask(__name__)
CORS(app)


@app.route('/webapi/cadastro', methods=['POST'], endpoint="cadastro")
@app.route('/webapi/login', methods=['POST'], endpoint="login")
@app.route('/webapi/perfil', methods=['POST'], endpoint="perfil")
@app.route('/webapi/perfil_senha', methods=['POST'], endpoint="perfil_senha")
@app.route('/webapi/perfil/<string:user_id>', methods=['GET'], endpoint="get_perfil")
def usuario(user_id: str = None):

    try:
        request_endpoint = request.endpoint
        user_srv = UsersService()

        if request.method == 'POST':
            user = request.get_json(silent=True)

            if request_endpoint == "cadastro":
                result = user_srv.create_user(user=user)
                print(result)
                if str(result)[0:5] == "Error":
                    return {"result": result}, 400

                return result

            if request_endpoint == "login":
                result = user_srv.login_user(user=user)
                try:
                     if result["result"][0:3] == "Usu":
                         return result
                except:
                    pass


            if request_endpoint == "perfil":
                print(user)
                result = user_srv.perfil(user=user)
                return result


            if request_endpoint == "perfil_senha":
                result = user_srv.perfil_change_pwd(user=user)
                if str(result)[0:5] == "Error":
                    return {"result": result}, 400

                return result

        if request.method == 'GET':

            if request_endpoint == "get_perfil":
                print("user_id " + user_id)
                result = user_srv.get_perfil(user_id=user_id)


        if str(result)[0:5] == "Error":
            return {"result": result}, 400
        else:
            print("before sending: ")
            print(result)
            id = result["_id"]
            print({"result": "Sucesso", "id": str(id), "name": result["name"], "last_name": result["last_name"]})
            return {"result": "Sucesso", "id": str(id), "name": result["name"], "last_name": result["last_name"]}, 201

    except Exception as e:
        logging.error("Error: " + str(e))
        return {}

@app.route('/webapi/produtos/<string:param_user_id>', methods=['GET'], endpoint="get_products")
@app.route('/webapi/produtos/<string:param_user_id>/<string:param_product_id>', methods=['GET'], endpoint="get_one_product")
@app.route('/webapi/produtos', methods=['POST','PUT'], endpoint="cadastro_produtos")
@app.route('/webapi/produtos', methods=['DELETE'], endpoint="delete_produtos")
def produtos(param_user_id=None, param_product_id=None):

    try:
        request_endpoint = request.endpoint
        pro_srv = ProductsService()

        if request.method in ('POST','PUT'):
            produto = request.get_json(silent=True)

            result = pro_srv.merge_product(product=produto)
            print("app " + str(result))

            if str(result)[0:5] == "Error":
                return {"result": result}, 400
            else:
                return {"result": "Sucesso", "id": str(result)}, 201


        if request.method == 'GET':
            print("debug1 call service " )
            print("user_id: " + param_user_id)

            if request_endpoint == "get_one_product":
                result = pro_srv.get_user_one_product(user_id=param_user_id, product_id=param_product_id)
            else:
                result = pro_srv.get_user_products(user_id=param_user_id)

            if str(result)[0:5] == "Error":
                return {"result": result}, 400
            else:
                print("result return")
                print(result)
                return jsonify(result), 201

        if request.method == 'DELETE':
            print("produto delete debug1 call service " )
            products = request.get_json(silent=True)
            print(products)
            result = pro_srv.delete_user_product(products=products)

            if str(result)[0:5] == "Error":
                return {"result": result}, 400
            else:
                print("result return")
                print(result)
                return jsonify(result), 201


    except Exception as e:
        logging.error("Error: " + str(e))
        return {}

@app.route('/webapi/publis/<string:param_user_id>', methods=['GET'], endpoint="get_publis")
@app.route('/webapi/publis/<string:param_user_id>/<string:param_publi_id>', methods=['GET'], endpoint="get_publi")
@app.route('/webapi/publis', methods=['POST','PUT'], endpoint="cadastro_publi")
@app.route('/webapi/publis', methods=['DELETE'], endpoint="delete_publi")
def publis(param_user_id=None, param_publi_id=None):

    try:
        request_endpoint = request.endpoint
        publi_srv = PublisService()

        if request.method in ('POST','PUT'):
            publi = request.get_json(silent=True)

            print(publi)
            result = publi_srv.merge_publi(publi=publi)
            print("app " + str(result))

            if str(result)[0:5] == "Error":
                return {"result": result}, 400
            else:
                return {"result": "Sucesso", "id": str(result)}, 201


        if request.method == 'GET':
            print("publi debug1 call service " )

            if request_endpoint == 'get_publi':
                result = publi_srv.get_user_one_publi(user_id=param_user_id, publi_id=param_publi_id)
            else:
                result = publi_srv.get_user_publis(user_id=param_user_id)

            if str(result)[0:5] == "Error":
                return {"result": result}, 400
            else:
                print("result return")
                print(result)
                return jsonify(result), 201


        if request.method == 'DELETE':
            print("publi delete debug1 call service " )
            publis = request.get_json(silent=True)
            print(publis)
            result = publi_srv.delete_user_publi(publis=publis)

            if str(result)[0:5] == "Error":
                return {"result": result}, 400
            else:
                print("result return")
                print(result)
                return jsonify(result), 201


    except Exception as e:
        logging.error("Error: " + str(e))
        return {}

@app.route('/webapi/chatgpt_respostas/<string:param_user_id>', methods=['GET'], endpoint="get_respostas")
@app.route('/webapi/chatgpt_respostas/<string:param_user_id>/<string:param_resp_id>', methods=['GET'], endpoint="get_resposta")
@app.route('/webapi/chatgpt_respostas', methods=['POST','PUT'], endpoint="cadastro_resp")
@app.route('/webapi/chatgpt_respostas', methods=['DELETE'], endpoint="delete_resp")
@app.route('/webapi/call_chatgpt_resp/<string:param_user_id>', methods=['POST'], endpoint="call_chatgpt_resp")
def chatgpt(param_user_id=None, param_resp_id=None):

    try:
        request_endpoint = request.endpoint
        answer_srv = ChatGPTService()

        if request.method in ('POST','PUT'):
            ans = request.get_json(silent=True)

            if request_endpoint == "call_chatgpt_resp":
                print("pergunta: " + str(ans))
                result = answer_srv.call_chatgpt(question=ans);
                return result

            else:
                print(ans)
                result = answer_srv.merge_answer(answer=ans)
                print("app " + str(result))

            if str(result)[0:5] == "Error":
                return {"result": result}, 400
            else:
                return {"result": "Sucesso", "id": str(result)}, 201


        if request.method == 'GET':
            print("chat debug1 call service " )

            if request_endpoint == 'get_resposta':
                result = answer_srv.get_user_one_answer(user_id=param_user_id, answer_id=param_resp_id)
            else:
                result = answer_srv.get_user_answers(user_id=param_user_id)

            if str(result)[0:5] == "Error":
                return {"result": result}, 400
            else:
                print("result return")
                print(result)
                return jsonify(result), 201


        if request.method == 'DELETE':
            print("publi delete debug1 call service " )
            ans = request.get_json(silent=True)
            print(publis)
            result = answer_srv.delete_user_answer(answers=ans)

            if str(result)[0:5] == "Error":
                return {"result": result}, 400
            else:
                print("result return")
                print(result)
                return jsonify(result), 201


    except Exception as e:
        logging.error("Error: " + str(e))
        return {}


@app.route('/webapi/links/<string:param_user_id>', methods=['GET'], endpoint="get_links")
@app.route('/webapi/links/<string:param_user_id>/<string:param_links_id>', methods=['GET'], endpoint="get_link")
@app.route('/webapi/links', methods=['POST','PUT'], endpoint="cadastro_links")
@app.route('/webapi/links', methods=['DELETE'], endpoint="delete_links")
def publis(param_user_id=None, param_links_id=None):

    try:
        request_endpoint = request.endpoint
        links_srv = LinksService()

        if request.method in ('POST','PUT'):
            links = request.get_json(silent=True)

            print(links)
            result = links_srv.merge_links(links=links)
            print("app " + str(result))

            if str(result)[0:5] == "Error":
                return {"result": result}, 400
            else:
                return {"result": "Sucesso", "id": str(result)}, 201


        if request.method == 'GET':
            print("link debug1 call service ")

            if request_endpoint == 'get_link':
                result = links_srv.get_user_one_links(user_id=param_user_id, links_id=param_links_id)
            else:
                print(param_user_id)
                result = links_srv.get_user_links(user_id=param_user_id)

            if str(result)[0:5] == "Error":
                return {"result": result}, 400
            else:
                print("result return")
                print(result)
                return jsonify(result), 201


        if request.method == 'DELETE':
            print("link delete debug1 call service " )
            links = request.get_json(silent=True)
            print(links)
            result = links_srv.delete_user_links(links=links)

            if str(result)[0:5] == "Error":
                return {"result": result}, 400
            else:
                print("result return")
                print(result)
                return jsonify(result), 201


    except Exception as e:
        logging.error("Error: " + str(e))
        return {}


@app.route('/webapi/dashboard/<string:param_user_id>', methods=['GET'], endpoint="get_dash_info")
def dashboard(param_user_id=None):

    try:
        request_endpoint = request.endpoint
        dash_srv = DashboardService()

        if request.method == 'GET':
            print("dash debug1 call service ")

            result = dash_srv.get_user_dash_info(user_id=param_user_id)

            if str(result)[0:5] == "Error":
                return {"result": result}, 400
            else:
                print("result return")
                print(result)
                return jsonify(result), 201


    except Exception as e:
        logging.error("Error: " + str(e))
        return {}


@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

