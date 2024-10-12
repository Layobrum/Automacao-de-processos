
# Projeto de Automação de Cadastro de Produtos

## Descrição
-------------
Este projeto visa automatizar o cadastro de produtos em um sistema de gerenciamento de estoque. Ele utiliza a biblioteca `pyautogui` para simular ações do usuário e a biblioteca `pandas` para ler e manipular os dados dos produtos.
É possível ver uma prévia do script funcionando em `Video demonstrativo.mp4`

## Arquivos do Projeto
----------------------
- `algoritmo.txt`: Documento que descreve o passo a passo da tarefa realizada no projeto;
- `main.py`: Script principal que executa a automação do cadastro de produtos;
- `posicao_mouse.py`: Script auxiliar que ajuda a determinar a posição do mouse na tela;
- `produtos.csv`: Arquivo de dados que contém as informações dos produtos a serem cadastrados;

## Funcionamento do Projeto
---------------------------
1) O script `main.py` lê os dados dos produtos do arquivo `produtos.csv` e os armazena em uma tabela
2) Em seguida, ele abre o navegador e acessa o sistema de gerenciamento de estoque
3) O script então faz login no sistema utilizando as credenciais definidas
4) Após o login, o script começa a cadastrar os produtos, um por um, utilizando as informações da tabela
5) Para cada produto, o script preenche os campos necessários e clica no botão de cadastro
6) O processo é repetido até que todos os produtos sejam cadastrados

### Requisitos
--------------
- Python;
- Bibliotecas pyautogui e pandas;
- Navegador instalado (no caso, o Opera);
- Sistema de gerenciamento de estoque acessível via navegador (caso seja via sistema é possível alterar o código para manter o funcionamento).

### Uso
-------
- Clone o repositório para o seu computador;
- Instale as bibliotecas necessárias utilizando o comando `pip install pyautogui pandas`;
- Edite o arquivo `main.py` para definir as credenciais de login e o caminho para o arquivo `produtos.csv`;
- Execute o script `main.py` para iniciar a automação do cadastro de produtos.

## Observações
--------------
- Este projeto é apenas um exemplo de automação e pode precisar ser adaptado para o seu sistema de gerenciamento de estoque específico;
- É importante testar o script em um ambiente de teste antes de executá-lo em produção;
- O uso de automação pode ser sujeito a restrições e políticas de segurança do sistema de gerenciamento de estoque.

# Créditos
-----------
- Este projeto foi criado por Layo "MrBrum" como prática da `Jornada Python` by *Hashtag Treinamentos*.
- Se você tiver alguma dúvida ou sugestão, por favor entre em contato comigo pelo meu [Linkedin](https://www.linkedin.com/in/layo-brum/).


