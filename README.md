# Netflix-Recommendation-System
Objetivo do projeto: 
O objetivo é criar um sistema de recomendação baseado em conteúdo. Isso significa que o sistema sugere títulos da Netflix semelhantes a um título fornecido pelo usuário, utilizando informações do próprio conteúdo (como descrição e gêneros).

-Utilizei a base de dados do kaggle: https://www.kaggle.com/datasets/shivamb/netflix-shows. 
-Utilizei as bibliotecas pandas (para manipulação e análise de dados em tabelas), numpy (para realizar as operações matemáticas) e re (para procurar padrões em strings).
-Utilizei a vetorização e similaridade de cosseno para medir a semelhança entre os vetores dos títulos.
-A função da recomendação busca o índice do título que o usuário digita, ordena os títulos parecidos com base na similaridade de cosseno e retorna uma lista de títulos recomendados.
-Também utilizei Flask para criar a interface. 


#Como rodar o projeto:

1. Clone o Repositório

2. Instale o Python

3. Crie um Ambiente Virtual
No diretório do projeto, crie um ambiente virtual para isolar as dependências:
comando: python -m venv venv

Ative o ambiente virtual:
- Windows: venv\Scripts\activate

- Mac/Linux: source venv/bin/activate
 

4. Instale as Dependências
Instale todas as bibliotecas necessárias usando o arquivo `requirements.txt`:
Comando: pip install -r requirements.txt

5. Prepare os Dados
Antes de rodar a aplicação Flask, você precisa processar os dados brutos. Para isso:
1. Certifique-se de que o arquivo `netflix_titles.csv` está na raiz do projeto.
2. Execute o script de processamento:
   Comando: python pythonscript.py
   Isso gerará um arquivo chamado `netflix_processed.csv` com os dados limpos.

6. Inicie a Aplicação Flask
Agora você pode rodar o servidor Flask:
Comando: python recommendation.py


7. Acesse a Aplicação
Abra um navegador e acesse "http://127.0.0.1:5000" e você verá a interface da aplicação.

8. Testando o Projeto
- No campo de texto, digite o nome de um título (por exemplo: `Grey's Anatomy`).
- Clique no botão "Recommend" para visualizar os títulos recomendados.

Arquivos do Projeto
- process_data.py : Script para processar os dados brutos e gerar o arquivo netflix_processed.csv.
- recommendation.py: Contém o código principal do Flask, incluindo a lógica de recomendação.
- templates/index.html: Front-end simples para a interação com o usuário.
- requirements.txt: Lista de dependências necessárias para o projeto.

