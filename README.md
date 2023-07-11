# easyPubli
   
## Overview	
    A constante expansão da internet e dos negócios online tem movimentado o mercado de marketing digital no Brasil e no mundo. As diversas possibilidades de trabalho trazem oportunidades, mas também desafios a quem empreende nessa área. A organização de tarefas específicas, por exemplo, pode ser um motivo de preocupação. Com isso, aplicações que apoiem o usuário tornam-se muito importantes.

    Inserido fielmente nesse contexto, easy Publi é um sistema web responsivo direcionado a quem trabalha com marketing digital, mais especificamente com marketing de afiliados. Tem como principal objetivo facilitar a rotina no controle de produtos e divulgações, sendo também uma ferramenta de geração de ideias e conteúdos.

    easy Publi faz parte do projeto final da unidade curricular “Projeto de Desenvolvimento 2”, do Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas da Faculdade Senac Porto Alegre. Idealizado e desenvolvido durante o primeiro semestre de 2023.

# Instalação
    Para iniciar esse projeto você precisa seguir os passos a seguir

### Passo 1 - Clonar o projeto
    Faça o clone do projeto para o diretório local
    Abra o terminal e execute o comando a seguir
    $ git clone https://github.com/susanaBarross/easyPubli.git 

### Passo 2 (Instalar as bibliotecas obrigatórias)
    Navegue ao diretorio do projeto
    Execute o comando:
        $ py -m pip install -r requirements.txt 

### Passo 3 Instalar o MongoDB
    Faça o download a partir do link abaixo caso ainda não tenha instalado localmente
    https://www.mongodb.com/try/download/community
![](readme_img/mongodb.png)


### Passo 4 ChatGPT
    Faça o cadastro na openAI para gerar uma chave a ser usada na API
    Substitua a chave no arquivo myproject > services > chatgpt_service.py 
    openai.api_key = <atribua a chave gerada para esta variável>

### Passo 5 Execute o projeto
    Navegue: <diretorio local>/MyProject
	Execute os comandos:
	    export FLASK_APP=myproject
        python -m flask run
			  
		Esses comandos devem iniciar o servidor local com a mensagem abaixo:
		" * Serving Flask app "app"
          * Environment: production
          WARNING: This is a development server. Do not use it in a production deployment.
          Use a production WSGI server instead.
          * Debug mode: off
          * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
        "
		Caso contrário  retorne ao passo 2
          



