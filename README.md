
# Checkpoint Python

### Integrantes 
| Nome | RM | 
|------------------------|--------| 
| Daniel Saburo Akiyama | 558263 | 
| João Pedro R. | 558199 | 

## Guia de como rodar o Checkpoint

### Pré-requisitos

-  **Python**: Certifique-se de que o Python esteja instalado em seu sistema.

### Instalação de Dependências

- Instale as dependências necessárias utilizando o seguinte comando:

```bash

	pip install oracledb

```

### Configuração de Credenciais

-  Edite o arquivo [banco.py](./banco.py) e insira suas credenciais do Oracle DB:

```bash

	user=<usuario_oracle_db>

	passwd=<senha_oracle_db>

```

### Criação das Tabelas

- Execute o arquivo Python [criar_tabelas.py](./criar_tabelas.py) para criar as tabelas que estão no diretório `/tabelas`. Os comandos nos arquivos `.sql` vão remover (dropar) as tabelas existentes para evitar erros de duplicidade e criar novas tabelas com os atributos exigidos.

 ```sql 
	DROP TABLE TB_MENSAGEM;
	-- Remove a tabela de tb_mensagem juntamente com seus dados

	CREATE  TABLE  TB_MENSAGEM (
			id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
			assunto VARCHAR2(50),
			destinatario VARCHAR2(50),
			remetente VARCHAR2(50),
			conteudo VARCHAR2(1000)
	);
	-- Cria a tabela de tb_mensagem com os atributos
```

### Inserção de mensagens

- Para inserir 20 mensagens de exemplo na tabela `tb_mensagem`, execute o arquivo Python [insere_mensagens.py](./insere_mensagens.py). Todos os resultados serão impressos no terminal.

### Simulação das Funções

- Por fim, execute o arquivo Python   [simula_funcoes_banco.py](./simula_funcoes_banco.py) para simular todas as funções (exceto a função `inclui()`) do arquivo  [banco.py](./banco.py). Todos os resultados serão impressos no terminal.
