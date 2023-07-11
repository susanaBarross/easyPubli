/* -------------------------------- Global ------------------------------ */

const easyPub = "http://127.0.0.1:5000/webapi/";


const callEasyPubWS = async (page, method, body, handle_response) => {
    
    if (method == 'GET'){
        
        const response = await fetch(easyPub+page, 
                         {method: method,    
                          headers: {'Content-Type': 'application/json'}
                         });
      
       const myJson = await response.json(); //extract JSON from the http response
      
       handle_response(myJson);      
      
      
    }
    else{

        const response = await fetch(easyPub+page, 
                         {method: method,
                         body: JSON.stringify(body), // string or object
                         headers: {'Content-Type': 'application/json'}
                         });
      
      const myJson = await response.json(); //extract JSON from the http response
      
      handle_response(myJson);      
    } 
  
}


function alerta(message){
    if(message == "Sucesso"){
        Swal.fire({
                position: 'top',
                icon: 'success',
                title: message,
                showConfirmButton: false,
                timer: 3000,
                toast:true
             })
        
    }else{
        Swal.fire({
                position: 'top',
                icon: 'info',
                title: message,
                showConfirmButton: false,
                timer: 3000,
                toast:true
             })
    }
}



/* --------------------------------   Menu ------------------------------ */
function menu_add_user(){
    
    let user_id = get_param_user_id();
    
    document.getElementById("user_id").value = user_id;    
    document.getElementById("dashboardHref").href = "dashboard.html?user_id="+user_id;
    document.getElementById("produtosHref").href = "produtos.html?user_id="+user_id;
    document.getElementById("publicacoesHref").href = "publicacoes.html?user_id="+user_id;
    document.getElementById("publiChatHref").href = "publi_chatGPT.html?user_id="+user_id;
    document.getElementById("trendsHref").href = "trends.html?user_id="+user_id;
    document.getElementById("linksHref").href = "links.html?user_id="+user_id;
    
}


function load_profile_user(){
    
    let user_id = get_param_user_id();
    
    document.getElementById("perfil_link1").href = "perfil_oficial.html?user_id="+user_id;
    document.getElementById("perfil_link2").href = "perfil_oficial.html?user_id="+user_id;
     
    
}


/* --------------------------------   Usuario ------------------------------ */

function set_login_button_enviar(){
    var input = document.getElementById("password");

    input.addEventListener("keypress", function(event) {

        if (event.key === "Enter") {
            event.preventDefault();
            document.getElementById("entrar").click();
        }
    });
    
}  

function set_cadastro_button_enviar(){
    var input = document.getElementById("passwordCheck");

    input.addEventListener("keypress", function(event) {

        if (event.key === "Enter") {
            event.preventDefault();
            document.getElementById("btnEnviar").click();
        }
    });
    
}  




function get_param_user_id(){
    
    
    let user_id = "";
    const parametros = window.location.href.split('?')[1];
    const queryString = new URLSearchParams(parametros);

    for (let pair of queryString.entries()) {
       
        if(pair[0]=="user_id"){
            user_id = pair[1];
        }    
    } 
    
    
    return user_id;
    
}


function cadastro_handle_response(myJson){
    
    
    let result = myJson["result"];
    alerta(result);
    setTimeout(() => {  window.location.href="index.html"; }, 3000);    
    
}


function cadastro() {
    
      let callWS = true;
      
      let senha = document.getElementById("password").value;
      
      let senhaCheck = document.getElementById("passwordCheck").value;
      let email = document.getElementById("email").value;
        
      if (senha.length == "") {  
          alerta("Por favor informe uma senha");
          callWS = false;
      }
      if (email.length < 3) {
          alerta("Por favor informe um email.");
          callWS = false;
      }	
      
      if(senha != senhaCheck){
          alerta("As senhas não são iguais.");
          callWS = false;
      }
      
      
      if(callWS){
          json_user = {"email":email, "pwd":senha};
          
          callEasyPubWS(page="cadastro", 
                        method="POST",
                        body=json_user, 
                        handle_response=cadastro_handle_response);
      }             
                    
    
}


function perfil_handle_response(myJson){
    
    
    let result  = myJson["result"]
    alerta(result);
}

function perfil() {
      
      const user_id = document.getElementById("user_id").value;
      const nome = document.getElementById("nome").value;
      const sobrenome = document.getElementById("sobrenome").value;
      
      json_user = {"user_id": user_id, "nome":nome, "sobrenome":sobrenome};
      
      callEasyPubWS(page="perfil", 
                    method="POST",
                    body=json_user, 
                    handle_response=perfil_handle_response);
                    
    
}

function perfil_senha_handle_response(myJson){
    
    
    let result  = myJson["result"]
    alerta(result);
}

function perfil_senha() {
      
      const user_id   = document.getElementById("user_id").value;
      const nova_senha = document.getElementById("nova_senha").value;
      const confirma_senha = document.getElementById("confirma_senha").value;
      
      if(nova_senha != confirma_senha){
          alerta("Senhas não estão iguais.");
      }else{
          json_user = {"user_id": user_id , "nova_senha":nova_senha};
      
          callEasyPubWS(page="perfil_senha", 
                        method="POST",
                        body=json_user, 
                        handle_response=perfil_senha_handle_response);    
      }
      
      
                    
    
}


function usuario_login_handle_response(myJson){
    
    
    if (myJson["result"]=="Sucesso"){window.location.href="dashboard.html?user_id="+myJson["id"];}
    else{alerta(myJson["result"]);}
}


function usuario_login() {
      
      const email = document.getElementById("email").value;
      const senha = document.getElementById("password").value;
      
      json_user = {"email":email, "pwd":senha};
      
      callEasyPubWS(page="login", 
                    method="POST",
                    body=json_user, 
                    handle_response=usuario_login_handle_response);
                    
    
}


function get_perfil_handle_response(myJson){
    
    
    document.getElementById("user_id").value = myJson["id"];
    document.getElementById("nome").value = myJson["name"];
    document.getElementById("sobrenome").value = myJson["last_name"];
    
}


function get_perfil() {
      
      const user_id   = get_param_user_id();      
      
      callEasyPubWS(page="perfil/"+user_id, 
                    method="GET",
                    body="", 
                    handle_response=get_perfil_handle_response);
                    
    
}


/* --------------------------------   Cadastro Produto  ------------------------------ */
function cadastro_produto_handle_response(myJson){
    
    
    document.getElementById("product_id").value = myJson["id"];
    let result = myJson["result"];
    alerta(result);
}


function cadastro_produto() {
      
      const user_id = document.getElementById("user_id").value;
      const product_id = document.getElementById("product_id").value;
      const produto = document.getElementById("produto").value;
      const plataforma = document.getElementById("plataforma").value;
      const preco_maximo = document.getElementById("preco_maximo").value;
      const comissao = document.getElementById("comissao").value;
      const qtd_vendida = document.getElementById("qtd_vendida").value; 
      const rvalue= document.getElementsByName("status");  
      const status = Array.from(rvalue).find(radio => radio.checked).value;      
      const divulgacao = document.getElementById("divulgacao").value;
      const link = document.getElementById("link").value;
      const observacao = document.getElementById("observacao").value;
      
      
      if(produto == "" || plataforma == "" || comissao == "" || qtd_vendida == ""){
          
          alerta("Preencha os campos obrigatórios"); 
          
      }else{
          
          if(preco_maximo != "" && +comissao > +preco_maximo){
              alerta("A comissão não pode ser maior que o preço máximo."); 
              
          }else{
          
              json_produto = {"produto":produto,
                              "plataforma":plataforma,
                              "preco_maximo": preco_maximo,
                              "comissao":comissao,
                              "qtd_vendida":qtd_vendida,                      
                              "status":status,
                              "divulgacao":divulgacao,
                              "link":link,
                              "observacao":observacao,
                              "user_id":user_id,
                              "product_id": product_id
                              };
              
              callEasyPubWS(page="produtos", 
                            method="POST",
                            body=json_produto, 
                            handle_response=cadastro_produto_handle_response);
          }
                        
      }                
                    
    
}

function add_produtos(item, index){
    
    var statusDesc = "";
    
    var table = document.getElementById("tprodutos");
    
    var row = table.insertRow(0);

  
    var checkPubli = row.insertCell(0);
    var produto = row.insertCell(1);
    var plataforma = row.insertCell(2);
    var preco_maximo = row.insertCell(3);
    var comissao = row.insertCell(4);
    var qtd_vendida = row.insertCell(5);
    var faturamento = row.insertCell(6);
    var status = row.insertCell(7);
    var divulgacao = row.insertCell(8);
    var link = row.insertCell(9);
    var observacao = row.insertCell(10);
    
    checkPubli.innerHTML = '<input type="checkbox" id="produto'+index+'" name="chkbx" value="'+index+'">'
                   + '<input type="hidden" id="user_id'+index+'" name="user_id'+index+'" value="'+item["user_id"]["$oid"]+'">'
                   + '<input type="hidden" id="product_id'+index+'" name="product_id'+index+'" value="'+item["_id"]["$oid"]+'">';                                             
    
    produto.innerHTML = item["produto"];
    plataforma.innerHTML = item["plataforma"];
    preco_maximo.innerHTML = item["preco_maximo"];
    comissao.innerHTML = item["comissao"];
    qtd_vendida.innerHTML = item["qtd_vendida"];
    faturamento.innerHTML = item["faturamento"];
    divulgacao.innerHTML = item["divulgacao"];
    link.innerHTML = '<a href='+item["link"]+ ' target="_blank">'+item["link"]+'</a>';
    observacao.innerHTML = item["observacao"];
    
    
    switch(item["status"]) {
       case "ativo":
           statusDesc = "Ativo";
           break;
       case "inativo":
         statusDesc = "Inativo";
         break;
       default:
         statusDesc = "Selecionado";
    }
    
    status.innerHTML = statusDesc;
    
    select_unselect_chkbx();
    
}


function get_produtos_handle_response(myJson){
    
    
    const produtosArray = JSON.parse(myJson);
    
    produtosArray.forEach(add_produtos);
    
    
}


function get_produtos (){
     
      const user_id = get_param_user_id();
      document.getElementById("cadastro_produto").href = "produto_form.html?user_id="+user_id; 
      
      callEasyPubWS(page="produtos/"+user_id, 
                    method="GET",
                    body="", 
                    handle_response=get_produtos_handle_response);
    
}


function get_produto_update_handle_response(myJson){
    
    const produtoJson = JSON.parse(myJson);
    
    let status = produtoJson["status"];
    
    document.getElementById("user_id").value = produtoJson["user_id"]["$oid"];
    document.getElementById("product_id").value = produtoJson["_id"]["$oid"];
    document.getElementById("produto").value = produtoJson["produto"];
    document.getElementById("plataforma").value = produtoJson["plataforma"];
    document.getElementById("preco_maximo").value = produtoJson["preco_maximo"];
    document.getElementById("comissao").value = produtoJson["comissao"];
    document.getElementById("qtd_vendida").value = produtoJson["qtd_vendida"];        
    document.getElementById(status).checked = true;    
    document.getElementById("divulgacao").value = produtoJson["divulgacao"];
    document.getElementById("link").value = produtoJson["link"];
    document.getElementById("observacao").value = produtoJson["observacao"];
    
}

function get_produto_update (){
    
    let product_id = null;
    let user_id = null;
    const parametros = window.location.href.split('?')[1];
    const queryString = new URLSearchParams(parametros);

    for (let pair of queryString.entries()) {
        
        if(pair[0] == "user_id"){
            user_id = pair[1];
        }else{
            product_id = pair[1];   
        }
        
    } 
      
    if (product_id != null){
        callEasyPubWS(page="produtos/"+user_id+"/"+product_id, 
                    method="GET",
                    body="", 
                    handle_response=get_produto_update_handle_response);
    }                
    
}

function update_produto(){
    
    //get count of rows
    let rows = document.getElementById("tprodutos").rows.length;
    let user_id = null;
    let product_id = null;    
    let escolhido = false;
    let qtd_escolhidos = 0;
    
    for (let i = 0; i < rows; i++) {
        
        let elementIndex = "produto"+i;
        let elementUser  = "user_id"+i;
        let elementProduto = "product_id"+i;
        
        if (document.getElementById(elementIndex).checked == true){
            
            user_id = document.getElementById(elementUser).value;
            product_id = document.getElementById(elementProduto).value;
            
            escolhido = true;
            
            qtd_escolhidos ++;
        
        }    
         
    }
    
    if (!escolhido || qtd_escolhidos > 1){
        alerta("Escolha um registro para fazer o update");
    }else{
        window.location.href = "produto_form.html?user_id="+user_id+"&produto_id="+product_id;    
        
    }
    
}


function delete_produto_handle_response(myJson){
    
    alerta(myJson["result"]);
    setTimeout(() => {  location.reload(); }, 2000); 
}

function delete_produto(){    

    
    //get count of rows
    let rows = document.getElementById("tprodutos").rows.length;
    let user_id = "";
    let product_id = "";    
    let escolhido = false;
    const produtosArray = []
    
    for (let i = 0; i < rows; i++) {
        
        let elementIndex = "produto"+i;
        let elementUser  = "user_id"+i;
        let elementProduto = "product_id"+i;
        
        if (document.getElementById(elementIndex).checked == true){
            
            user_id = document.getElementById(elementUser).value;
            product_id = document.getElementById(elementProduto).value;
            
            json_produto = {"user_id": user_id,
                            "product_id": product_id                             
                           };
            
            
            escolhido = true;
            
            produtosArray.push(json_produto);            
        
        }    
            
    }
    
    if (!escolhido){
        alerta("Escolha um registro para fazer o delete");
    }else{
        
        callEasyPubWS(page="produtos", 
                      method="DELETE",
                      body=produtosArray, 
                      handle_response=delete_produto_handle_response);
        
    } 
          
}

/* --------------------------------   Publicacao ------------------------------ */


function cadastro_publi_handle_response(myJson){
    
    alerta("Cadastro publi " + myJson["result"]);
    document.getElementById("publi_id").value = myJson["id"];
}


function cadastro_publi () {
      
      const user_id = document.getElementById("user_id").value;
      const publi_id = document.getElementById("publi_id").value;
      const titulo = document.getElementById("titulo").value;
      const produto_divulgado = document.getElementById("produto_divulgado").value;
      const midia = document.getElementById("midia").value;
      const observacao = document.getElementById("observacao").value;
      const rvalue= document.getElementsByName("status");  
      const statusR = Array.from(rvalue).find(radio => radio.checked).value;      
      
      let method = "POST";
 

      if(titulo == "" || midia == ""){
          
          alerta("Preencha os campos obrigatórios"); 
          
      }else{
      
      
          
          
          if(user_id){
             method = "PUT";           
          } 
          
          json_publi = {"user_id": user_id,
                        "publi_id": publi_id,   
                        "titulo":titulo,
                        "produto_divulgado":produto_divulgado,
                        "midia": midia,
                        "observacao":observacao,
                        "status":statusR                    
                       };
          
          callEasyPubWS(page="publis", 
                        method=method,
                        body=json_publi, 
                        handle_response=cadastro_publi_handle_response);
                        
      }                   
    
}

function add_publis(item, index){
    
    var statusDesc = "";
    
    var table = document.getElementById("tpublis");
    
    var row = table.insertRow(0);

    var checkPubli = row.insertCell(0);
    var titulo = row.insertCell(1);
    var produto_divulgado = row.insertCell(2);
    var midia = row.insertCell(3);
    var status = row.insertCell(4);
    var observacao = row.insertCell(5);
    
    checkPubli.innerHTML = '<input  class="form-check-input" type="checkbox" id="publi'+index+'" name="chkbx" value="'+index+'">'
                           + '<input type="hidden" id="user_id'+index+'" name="user_id" value="'+item["user_id"]["$oid"]+'">'
                           + '<input type="hidden" id="publi_id'+index+'" name="publi_id" value="'+item["_id"]["$oid"]+'">';                                                     
    
                            
    
    titulo.innerHTML = item["titulo"];    
    produto_divulgado.innerHTML = item["produto_divulgado"];    
    midia.innerHTML = item["midia"]    
    observacao.innerHTML = item["observacao"];
    
    switch(item["status"]) {
       case "analise":
           statusDesc = "Em Análise";
           break;
       case "producao":
         statusDesc = "Em Produção";
         break;
       default:
         statusDesc = "Publicado";
    }
    
    status.innerHTML = statusDesc;
    
    select_unselect_chkbx();
    
    
}


function get_publi_handle_response(myJson){
    
    
    const publisArray = JSON.parse(myJson);
    
    publisArray.forEach(add_publis);
    
    
}


function get_publis (){
     
      const user_id = get_param_user_id();
      document.getElementById("cadastro_publi").href = "publicacao_form.html?user_id="+user_id; 
      
      callEasyPubWS(page="publis/"+user_id, 
                    method="GET",
                    body="", 
                    handle_response=get_publi_handle_response);
    
}

function get_publi_update_handle_response(myJson){
    
    
    const publiJson = JSON.parse(myJson);
    
    let status = publiJson["status"];
    
    document.getElementById("user_id").value = publiJson["user_id"]["$oid"];
    document.getElementById("publi_id").value = publiJson["_id"]["$oid"];
    document.getElementById("titulo").value = publiJson["titulo"];
    document.getElementById("produto_divulgado").value = publiJson["produto_divulgado"];
    document.getElementById("midia").value = publiJson["midia"];
    document.getElementById("observacao").value = publiJson["observacao"];
    document.getElementById(status).checked = true;   
    
    
}

function get_publi_update (){
    
    let publi_id = null;
    let user_id = null;
    const parametros = window.location.href.split('?')[1];
    const queryString = new URLSearchParams(parametros);

    for (let pair of queryString.entries()) {
        
        if(pair[0] == "user_id"){
            user_id = pair[1];
        }else{
            publi_id = pair[1];   
        }
        
    } 
    
    
    if(publi_id != null){ 
            
        callEasyPubWS(page="publis/"+user_id+"/"+publi_id, 
                      method="GET",
                      body="", 
                      handle_response=get_publi_update_handle_response);
    }                  
    
}

function update_publi(){
    
    //get count of rows
    let rows = document.getElementById("tpublis").rows.length;
    let user_id = null;
    let publi_id = null;    
    let escolhido = false;
    let qtd_escolhidos = 0;
    
    for (let i = 0; i < rows; i++) {
        
        let elementIndex = "publi"+i;
        let elementUser  = "user_id"+i;
        let elementPubli = "publi_id"+i;
        
        if (document.getElementById(elementIndex).checked == true){
            
            user_id = document.getElementById(elementUser).value;
            publi_id = document.getElementById(elementPubli).value;
            
            
            escolhido = true;
            
            qtd_escolhidos ++;
        
        }    
        
         
    }
    
    if (!escolhido || qtd_escolhidos > 1){
        alerta("Escolha um registro para fazer o update");
    }else{
        
        window.location.href = "publicacao_form.html?user_id="+user_id+"&publi="+publi_id;    
        
    }
    
}


function delete_publi_handle_response(myJson){
    
    
    alerta(myJson["result"]);
    setTimeout(() => {  location.reload(); }, 2000);     
    
}

function delete_publi(){    

    
    //get count of rows
    let rows = document.getElementById("tpublis").rows.length;
    let user_id = null;
    let publi_id = null;    
    let escolhido = false;
    const publisArray = []
    
    for (let i = 0; i < rows; i++) {
        
        let elementIndex = "publi"+i;
        let elementUser  = "user_id"+i;
        let elementPubli = "publi_id"+i;
        
        if (document.getElementById(elementIndex).checked == true){
            
            user_id = document.getElementById(elementUser).value;
            publi_id = document.getElementById(elementPubli).value;
            
            json_publi = {"user_id": user_id,
                          "publi_id": publi_id                             
                         };
            
            
            escolhido = true;
            
            publisArray.push(json_publi);
            
        
        }    
        
          
    }
    
    if (!escolhido){
        alerta("Escolha um registro para fazer o delete");
    }else{
        
        callEasyPubWS(page="publis", 
                      method="DELETE",
                      body=publisArray, 
                      handle_response=delete_publi_handle_response);
        
    } 
          
}

/*---------------------------------   Links   ----------------------------------- */

function cadastro_links_handle_response(myJson){
    
    
    let result = myJson["result"];
    
    alerta(myJson["result"]);
    document.getElementById("link_id").value = myJson["id"]
}


function cadastro_links () {
      
      const user_id = document.getElementById("user_id").value;      
      const link_id = document.getElementById("link_id").value; 
      const referencia = document.getElementById("referencia").value;
      const links = document.getElementById("link").value;
    
      let method = "POST";
      
      
      if(referencia == "" || links == ""){
          
          alerta("Preencha os campos obrigatórios!");
          
      }else{
          
          if(link_id){
             method = "PUT";  
          }             
       
          
          json_link = {"user_id": user_id,
                        "link_id" : link_id,      
                        "referencia":referencia,
                        "links":links
                       };
                       
          
          callEasyPubWS(page="links", 
                        method=method,
                        body=json_link, 
                        handle_response=cadastro_links_handle_response);
     }                  
             
}

function add_links(item, index){
    
    
    var table = document.getElementById("tlinks");
    
    var row = table.insertRow(0);

    var checkLink = row.insertCell(0);
    var referencia = row.insertCell(1);
    var links = row.insertCell(2);
    
    
    checkLink.innerHTML = '<input  class="form-check-input" type="checkbox" id="link'+index+'" name="chkbx" value="'+index+'">'
                           + '<input type="hidden" id="user_id'+index+'" name="user_id'+index+'" value="'+item["user_id"]["$oid"]+'">'
                           + '<input type="hidden" id="link_id'+index+'" name="link_id'+index+'" value="'+item["_id"]["$oid"]+'">';                                                     
    
                            
    
    referencia.innerHTML = item["reference"];    
    links.innerHTML = '<a href='+item["links"]+ ' target="_blank">'+item["links"]+'</a>'; 

    select_unselect_chkbx();
    
}


function get_links_handle_response(myJson){
    
    
    const linksArray = JSON.parse(myJson);
    
    linksArray.forEach(add_links);
    
    
}


function get_links (){
     
      const user_id = get_param_user_id();
      
      document.getElementById("user_id").value = user_id;
      document.getElementById("cadastro_link1").href = "link_form.html?user_id="+user_id;      
      
      callEasyPubWS(page="links/"+user_id, 
                    method="GET",
                    body="", 
                    handle_response=get_links_handle_response);
    
}

function get_links_update_handle_response(myJson){
    
    const publiJson = JSON.parse(myJson);
    
    document.getElementById("user_id").value = publiJson["user_id"]["$oid"];
    document.getElementById("link_id").value = publiJson["_id"]["$oid"];
    document.getElementById("referencia").value = publiJson["reference"];
    document.getElementById("link").value = publiJson["links"];
    
}

function get_link_update (){
    
    let link_id = null;
    let user_id = null;
    const parametros = window.location.href.split('?')[1];
    const queryString = new URLSearchParams(parametros);
    

    for (let pair of queryString.entries()) {
        
        if(pair[0] == "user_id"){
            user_id = pair[1];
        }else{
            link_id = pair[1];   
        }
        
    } 
    
      
    if (link_id != null){
        callEasyPubWS(page="links/"+user_id+"/"+link_id, 
                      method="GET",
                      body="", 
                      handle_response=get_links_update_handle_response);
    }              
    
}

function update_link(){
    
    //get count of rows
    let rows = document.getElementById("tlinks").rows.length;
    let user_id = null;
    let link_id = null;    
    let escolhido = false;
    let qtd_escolhidos = 0;
    
    for (let i = 0; i < rows; i++) {
        
        let elementIndex = "link"+i;
        let elementUser  = "user_id"+i;
        let elementLink = "link_id"+i;
        
        if (document.getElementById(elementIndex).checked == true){
            
            user_id = document.getElementById(elementUser).value;
            link_id = document.getElementById(elementLink).value;
            
            escolhido = true;
            
            qtd_escolhidos ++;
        
        }    
       
    }
    
    if (!escolhido || qtd_escolhidos > 1){
        alerta("Escolha um registro para fazer o update");
    }else{
        
        window.location.href = "link_form.html?user_id="+user_id+"&link_id="+link_id;    
        
    }
    
}


function delete_links_handle_response(myJson){
    
    
    alerta(myJson["result"]);
    setTimeout(() => {  location.reload(); }, 2000); 
    
}

function delete_link(){    

    
    //get count of rows
    let rows = document.getElementById("tlinks").rows.length;
    let user_id = null;
    let link_id = null;    
    let escolhido = false;
    const linksArray = []
    
    for (let i = 0; i < rows; i++) {
        
        let elementIndex = "link"+i;
        let elementUser  = "user_id"+i;
        let elementLink = "link_id"+i;
        
        if (document.getElementById(elementIndex).checked == true){
            
            user_id = document.getElementById(elementUser).value;
            link_id = document.getElementById(elementLink).value;
            
            json_links = {"user_id": user_id,
                          "link_id": link_id                             
                         };
            
            
            escolhido = true;
            
            linksArray.push(json_links);
            
        
        }    
        
         
    }
    
    if (!escolhido){
        alerta("Escolha um registro para fazer o delete");
    }else{
        
        callEasyPubWS(page="links", 
                      method="DELETE",
                      body=linksArray, 
                      handle_response=delete_links_handle_response);
        
    } 
          
}
/* --------------------------------   Chat GPT ------------------------------ */


function set_button_enviar(){
    var input = document.getElementById("pergunta");

    input.addEventListener("keypress", function(event) {

        if (event.key === "Enter") {
            event.preventDefault();
            document.getElementById("enviar").click();
        }
    });
    
}    


function set_button_salvar(){
    var input = document.getElementById("midia");

    
    input.addEventListener("keypress", function(event) {

        if (event.key === "Enter") {
            event.preventDefault();
            cadastro_chatgpt();
        }
    });
    
}  


function cadastro_chatgpt_handle_response(myJson){
    
    alerta(myJson["result"]);
    setTimeout(() => {  location.reload(); }, 3000); 
    
    
}


function cadastro_chatgpt () {
      
      const user_id = document.getElementById("user_id").value;   
      const chatgpt_id = document.getElementById("chatgpt_id").value;      
      const pergunta = document.getElementById("pergunta").value;
      const classificacao = document.getElementById("classificacao").value;
      const produto_relacionado = document.getElementById("produto_relacionado").value;
      const midia = document.getElementById("midia").value;
      const resposta= document.getElementById("resposta").value;  
      
      let method = "POST";
      
      
      if(pergunta == "" || resposta == ""){
          
          alerta("Preencha os campos obrigatórios"); 
          
      }else{
      
          if(user_id){
             method = "PUT";           
          } 
          
          json_chatgpt = {"user_id": user_id, 
                          "chatgpt_id":chatgpt_id,          
                          "pergunta":pergunta,
                          "classificacao":classificacao,
                          "produto_relacionado": produto_relacionado,
                          "midia":midia,
                          "resposta":resposta                    
                         };
          
          callEasyPubWS(page="chatgpt_respostas", 
                        method=method,
                        body=json_chatgpt, 
                        handle_response=cadastro_chatgpt_handle_response);
                        
     }
}

function add_chatgpt_respostas(item, index){
    
    
    var table = document.getElementById("trespostas");
    
    var row = table.insertRow(0);

    var checkGPT = row.insertCell(0);
    var pergunta = row.insertCell(1);
    var classificacao = row.insertCell(2);
    var produto_relacionado = row.insertCell(3);
    var midia = row.insertCell(4);
    var resposta = row.insertCell(5);

    // Add some text to the new cells:
    
    
    checkGPT.innerHTML = '<input  class="form-check-input" type="checkbox" id="chatgpt'+index+'" name="chkbx" value="'+index+'">'
                           + '<input type="hidden" id="user_id'+index+'" name="user_id" value="'+item["user_id"]["$oid"]+'">'
                           + '<input type="hidden" id="chatgpt_id'+index+'" name="chatgpt_id" value="'+item["_id"]["$oid"]+'">';                                                     
    
                            
    
    if(item["pergunta"].length > 30){
        pergunta.innerHTML = item["pergunta"].slice(0,30) + "..."; 
    }else{
        pergunta.innerHTML = item["pergunta"];        
    }
    
    classificacao.innerHTML = item["classificacao"];    
    produto_relacionado.innerHTML = item["produto_relacionado"]
    midia.innerHTML = item["midia"];
    if(item["resposta"].length > 30){
        resposta.innerHTML = item["resposta"].slice(0,30) + "...";    
    }else{
        resposta.innerHTML = item["resposta"];
    }
    
    
    select_unselect_chkbx();
}


function get_chatgpt_resposta_handle_response(myJson){
    
    
    const respostasArray = JSON.parse(myJson);
    
    respostasArray.forEach(add_chatgpt_respostas);
    
    
}


function get_chatgpt_respostas (){
     
      const user_id = get_param_user_id();
      
      callEasyPubWS(page="chatgpt_respostas/"+user_id, 
                    method="GET",
                    body="", 
                    handle_response=get_chatgpt_resposta_handle_response);
    
}

function get_chatgpt_respostas_update_handle_response(myJson){
    
    const respostasJson = JSON.parse(myJson);
    
    document.getElementById("user_id").value = respostasJson["user_id"]["$oid"];
    document.getElementById("chatgpt_id").value = respostasJson["_id"]["$oid"];
    document.getElementById("pergunta").value = respostasJson["pergunta"];
    document.getElementById("classificacao").value = respostasJson["classificacao"];
    document.getElementById("produto_relacionado").value = respostasJson["produto_relacionado"];
    document.getElementById("midia").value = respostasJson["midia"];
    document.getElementById("resposta").value = respostasJson["resposta"];
    
    
}



function update_chatgpt_resposta(){
    
    //get count of rows
    let rows = document.getElementById("trespostas").rows.length;
    let user_id = null;
    let chatgpt_id = null;    
    let escolhido = false;
    let qtd_escolhidos = 0;
    
    for (let i = 0; i < rows; i++) {
        
        let elementIndex = "chatgpt"+i;
        let elementUser  = "user_id"+i;
        let elementResp = "chatgpt_id"+i;
        
        if (document.getElementById(elementIndex).checked == true){
            
            user_id = document.getElementById(elementUser).value;
            chatgpt_id = document.getElementById(elementResp).value;
            
            escolhido = true;
            
            qtd_escolhidos ++;
        
        }    
        
    }
    
    if (!escolhido || qtd_escolhidos > 1){
        alerta("Escolha um registro para fazer o update");
    }else{
        
        callEasyPubWS(page="chatgpt_respostas/"+user_id+"/"+chatgpt_id, 
                      method="GET",
                      body="", 
                      handle_response=get_chatgpt_respostas_update_handle_response);
        
    }
    
}


function delete_chatgpt_resposta_handle_response(myJson){
    
    alerta(myJson["result"]);
    setTimeout(() => {  location.reload(); }, 2000); 
}

function delete_resposta(){    

    
    //get count of rows
    let rows = document.getElementById("trespostas").rows.length;
    let user_id = null;
    let chatgpt_id = null;    
    let escolhido = false;
    const respostasArray = []
    
    for (let i = 0; i < rows; i++) {
        
        let elementIndex = "chatgpt"+i;
        let elementUser  = "user_id"+i;
        let elementResp = "chatgpt_id"+i;
        
        if (document.getElementById(elementIndex).checked == true){
            
            user_id = document.getElementById(elementUser).value;
            chatgpt_id = document.getElementById(elementResp).value;
            
            json_chatgpt= {"user_id": user_id,
                          "chatgpt_id": chatgpt_id                             
                         };
            
            
            escolhido = true;
            
            respostasArray.push(json_chatgpt);
            
        
        }    
        
    }
    
    if (!escolhido){
        alerta("Escolha um registro para fazer o delete");
    }else{
        
        callEasyPubWS(page="chatgpt_respostas", 
                      method="DELETE",
                      body=respostasArray, 
                      handle_response=delete_chatgpt_resposta_handle_response);
        
    } 
          
}


function call_chatgpt_resposta_handle_response(myJson){
    
    
    const resposta = myJson;
    
    document.getElementById("resposta").value = resposta["answer"];
    
    
}


function call_chatgpt_resp(){
     
      const user_id = get_param_user_id();
      
      const pergunta = document.getElementById("pergunta").value;
      
      if(pergunta == ""){
          alerta("Faça uma pergunta para enviar!");
      }else{
           
          json_pergunta = {"user_id": user_id,
                         "pergunta": pergunta                             
                        };
          
          callEasyPubWS(page="call_chatgpt_resp/"+user_id, 
                        method="POST",
                        body=json_pergunta, 
                        handle_response=call_chatgpt_resposta_handle_response);
      }
      
    
}


function copy_chatgpt_resposta() {  
  const copyResposta = document.getElementById("resposta");
  copyResposta.select();
  let respostaCopiada = document.execCommand('copy');
  
  if(respostaCopiada){
      alerta("Resposta copiada ");
  }else{
      alerta("Erro ao copiar a resposta.");
  }
  
}


/* --------------------------------   Dashboard   ------------------------------ */


function get_user_dash_handle_response(myJson){
    
    
    if(myJson["name"] == "" || myJson["name"] == undefined){
        document.getElementById("nome_usuario1").innerHTML = "Olá Usuário!";
        document.getElementById("nome_usuario2").innerHTML = "Olá Usuário!";
    }
    else{    
        document.getElementById("nome_usuario1").innerHTML = "Olá " + myJson["name"] + "!";
        document.getElementById("nome_usuario2").innerHTML = "Olá " + myJson["name"] + "!";
    }
    
}


function get_user_perfil(user_id) {
      
      callEasyPubWS(page="perfil/"+user_id, 
                    method="GET",
                    body="", 
                    handle_response=get_user_dash_handle_response);                    
    
}



function get_user(){
    
    let user_id = get_param_user_id();
    
    
    get_user_perfil(user_id) ;
    
    document.getElementById("user_id").value = user_id;
    document.getElementById("perfil_link1").href = "perfil_oficial.html?user_id="+user_id;
    document.getElementById("perfil_link2").href = "perfil_oficial.html?user_id="+user_id;
     
    
}


function load_dash_graficos_handle_response(myJson){

    
    const graficoInfo = JSON.parse(myJson);
    
    let el1 = document.getElementById("grafico1");
    let options1 = {
      series: graficoInfo["grf1"]["series"],
      chart: {
      width: 480,
      type: 'pie',
    },
    labels: graficoInfo["grf1"]["labels"],
    responsive: [{
      breakpoint: 992,
      options: {
        chart: {
          width: 280
        },
        legend: {
          position: 'bottom'
        }
      }
    }]
    }; 

    let chart1 = new ApexCharts(el1, options1)
    chart1.render()
 
  

  

    let el2 = document.getElementById("grafico2");
    let options2 = {
        chart: {
            type: 'bar',
            height: 350,
            width: 450
        },
        series: [
            {
                name: 'Faturamento',
                data: graficoInfo["grf2"]["data"]
            }

        ],
        xaxis: {
            categories: graficoInfo["grf2"]["categories"]
        },
        colors: ['#68e9e9'],
        responsive: [{
        breakpoint: 992,
         options: {
         chart: {
            height: 190,
            width: 240
        },
      }
    }]
    };  

    let chart2 = new ApexCharts(el2, options2)
    chart2.render()



    let el3 = document.getElementById("grafico3");
    let options3 = {
      series: graficoInfo["grf3"]["series"],
      labels: graficoInfo["grf3"]["labels"],
      chart: {
      width: 480,
      type: 'donut',
    },
    plotOptions: {
      pie: {
        startAngle: -90,
        endAngle: 270
      }
    },
    dataLabels: {
      enabled: false
    },
    fill: {
      type: 'gradient',
    },
    legend: {
      formatter: function(val, opts) {
        return val + " - " + opts.w.globals.series[opts.seriesIndex]
      }
    },
    title: {
      text: ''
    },
    responsive: [{
      breakpoint: 1000,
      options: {
        chart: {
          width: 290
        },
        legend: {
          position: 'bottom'
        }
      }
    }]
    };

    let chart3 = new ApexCharts(el3, options3)
    chart3.render()


    let el4 = document.getElementById("grafico4");
    let options4 = {
        chart: {
            type: 'bar',
            height: 350,
            width: 450
        },
        series: [
            {
                name: 'Plataforma',
                data: graficoInfo["grf4"]["data"]
            }
        ],
        xaxis: {
            categories: graficoInfo["grf4"]["categories"]
        },
        plotOptions:{
            bar: {
                horizontal: false,
                dataLabels: {
                    position: 'top'
                }
            }
        },
        yaxis:{
            min: 0,
            max: 10000
        },
        grid: {
            show: true,
            xaxis: {
                lines: {
                    show: true
                }
            }
        },
        colors: ['#FF6688'],
        responsive: [{
        breakpoint: 992,
         options: {
         chart: {
            height: 190,
            width: 240
        },
      }
    }]
    }
    let chart4 = new ApexCharts(el4, options4)
    chart4.render()


    let el5 = document.getElementById("grafico5");
    let options5 = {
      series: graficoInfo["grf5"]["series"],
      labels: graficoInfo["grf5"]["labels"],
      chart: {
      width: 480,
      type: 'donut',
    },
    responsive: [{
      breakpoint: 1000,
      options: {
        chart: {
          width: 290
        },
        legend: {
          position: 'bottom'
        }
      }
    }]
    };


    let chart5 = new ApexCharts(el5, options5)
    chart5.render()





    let el6 = document.getElementById("grafico6");
    let options6 = {
        chart: {
            type: 'bar',
            height: 350,
            width: 450
        },
        series: [
            {
                name: 'Publicações',
                data: graficoInfo["grf6"]["data"]
            }

        ],
        xaxis: {
            categories: graficoInfo["grf6"]["categories"]
        },
        responsive: [{
        breakpoint: 992,
         options: {
         chart: {
            height: 190,
            width: 240
        },
      }
    }]
    };  

    let chart6 = new ApexCharts(el6, options6)
    chart6.render()
    
}    

function load_dash_graficos() {
    
      let user_id = get_param_user_id();
      
      callEasyPubWS(page="dashboard/"+user_id, 
                    method="GET",
                    body="", 
                    handle_response=load_dash_graficos_handle_response);                    
    
}



/* ---------------------------  checkboxes -------------------------------------*/

function select_unselect_chkbx(){

    let checkbox = document.getElementById("allCheckBoxes");

    checkbox.addEventListener('change', function() {
      if (this.checked) {        
        selectAll();
        
      } else {        
        UnSelectAll();
      }
    });

}

function selectAll() {
    var items = document.getElementsByName('chkbx');
    for (var i = 0; i < items.length; i++) {
            if (items[i].type == 'checkbox')
                items[i].checked = true;
        }
}

function UnSelectAll() {
    var items = document.getElementsByName('chkbx');
    for (var i = 0; i < items.length; i++) {
            if (items[i].type == 'checkbox')
                items[i].checked = false;
        }
}	