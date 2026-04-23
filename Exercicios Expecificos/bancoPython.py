# CONECTAR BANCO COM PYTHON

import mysql.connector

def obtemConexao(servidor, usuario, senha, bd):
    if obtemConexao.conexao == None:
        obtemConexao.conexao = mysql.connector.connect(
            host=f"{servidor}",
            user=f"{usuario}",
            password=f"{senha}",
            database=f"{bd}"
        )
    return obtemConexao.conexao
obtemConexao.conexao = None

# EXEMPLO FUNÇÃO DE CRIAR UM INSERT
# Suponhamos que já temos criado uma tabela chamada 'alunos' com os campos 'ra' INT PRIMARY KEY e 'nome' VARCHAR(80) NOT NULL
def insercao_de_aluno(ra, nome):
    comando = f"INSERT INTO alunos (ra, nome) VALUES ({ra}, '{nome}')"
    conexao = obtemConexao("172.16.12.14", "usuario", "senha", "usuario")
    
    #fornecer algo que é capaz de executar comandos SQL
    # peça para o banco de dados uma "caneta" para escrever o comando SQL
    cursor = conexao.cursor()
    cursor.execute(comando)

    # confirmar a execução do comando
    conexao.commit()

# EXEMPLO DE CRIAR UM INSERT NA TABELA ALUNOS
insercao_de_aluno(26001620, "Bruna Savelli")

# EXEMPLO FUNÇÃO DE SELECT
# SELECT não tem commit, pois não altera o banco de dados, apenas consulta
def selecao_de_aluno(ra):
    comando = f"SELECT * FROM alunos WHERE ra = {ra}"
    conexao = obtemConexao("172.16.12.14", "usuario", "senha", "usuario")
    cursor = conexao.cursor()
    cursor.execute(comando)

    # "pega" o resultado do comando SELECT e guarda na variável "linhas"
    linhas = cursor.fetchall()

    # caso o não venha nenhum resultado, retorna nulo
    # verificar se as linhas estão vazias, ou seja, se o comando SELECT não retornou nenhum resultado
    if linhas == []: return None

    # retorna a primeira linha do resultado (o aluno encontrado)
    return linhas [0]

# EXEMPLO DE CRIAR UM SELECT
linha = selecao_de_aluno(26001620)

# montrar na tela o ra e o nome do aluno encontrado
print(linha[0], linha[1])  # RESULTADO:     26001620 Bruna Savelli

# DESCONECTAR BANCO
def fecharConexao():
    conexao = obtemConexao("172.16.12.14", "usuario", "senha", "usuario")
    cursor = conexao.cursor()
    cursor.close()
    conexao.close()

# Maligno fez um CRUD completo, TESTAR EM CASA.