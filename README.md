<div>
    <h1>
        Delivery API
    </h1>
    <br>
        <p>Vídeo de demonstração do Delivery API: https://www.youtube.com/watch?v=xP1k_agfcSk&list=LL6tHg2GmPgGBgCmTMltgO-A</p>
    <br>
    <p>
        Uma API de pedidos de delivery, com possibilidade de CRUD e alteração do estado dos pedidos.
    </p>
    <p>
        Essa API foi desenvolvida utilizando a arquitetura MVC, com as seguintes regras:
    </p>
</div>

* Os ```Models``` são os responsáveis pela manipulação dos dados, o ```models/Connection.py``` faz a conexão com o arquivo .json e retorna as funções de leitura e gravação de dados.
* Os ```Controllers``` recebem as requisições do Client, envia para o ```Model``` responsável pela ação requisitada e retorna uma resposta para o Client com o status da requisição. Os ```Controllers``` também são responsáveis pelo tratamento de erros na aplicação.
* O ```routes/routes.py``` é responsável por definir as rotas da aplicação e acionar o controller responsável pelo tratamento das rotas
* O arquivo ```App.py``` é a base da aplicação, é o arquivo que gerencia as PORTAS que serão usadas e o arquivo que fará a aplicação iniciar.

<br>

<div>
    <h2>
        Ferramentas utilizadas:
    </h2>
    <ul>
        <li>Flask</li>
        <li>Docker</li>
    </u>
</div>

<hr>
<br>

<div>
    <h2>
        Instruções para o uso:
    </h2>
    <h3>
        Pré-requisitos:
    </h3>
    <ul>
        <li>Python</li>
        <li>Docker</li>
    </u>
</div>

### Passo a passo:
* Clone o repositório github para a sua máquina e abra o CMD no local onde o repositório foi clonado.
* Com o docker rodando, execute o comando ```docker build .``` para gerar a imagem docker.
* Após a imagem ter sido gerada, execute o comando ```docker image ls``` e copie o ID da imagem que acabou de ser gerada.
* Execute o comando ```docker run -p 8081:8081 <imageID>``` substituindo o espaço ```<imageID>``` pelo ID da imagem que foi copiado.
* Prontinho, a aplicação está rodando.

<hr>
<br>

## Rotas
* Endpoint: ```/get-order/:orderId```
* Methods: ```GET```
* Body: ```None```
<p>Retorna um pedido com base em seu ID.</p>

<hr>

* Endpoint: ```/create```
* Methods: ```POST```
* Body: ```{ cliente: str, produto: str, valor: float }```
<p>Cadastra um novo pedido com estado RECEIVED.</p>

<hr>

* Endpoint: ```/update/:orderId```
* Methods: ```PUT```
* Body: ```{ cliente: str, produto: str, valor: float }```
<p>Atualiza os dados de um pedido existente com base em seu ID.</p>

<hr>

* Endpoint: ```/delete/:orderId```
* Methods: ```DELETE```
* Body: ```None```
<p>Exclui um pedido com base em seu ID.</p>

<hr>

* Endpoint: ```/change-state/:orderId/:orderState```
* Methods: ```PUT```
* Body: ```None```
* Estados possíveis: ```RECEIVED,
CONFIRMED, DISPATCHED, DELIVERED e CANCELED.```
<p>Altera o estado de um pedido, estando de acordo com as regras de negócio da aplicação, com base em seu ID. </p>
