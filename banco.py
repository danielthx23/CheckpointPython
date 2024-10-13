import oracledb
from oracledb import Connection as conn

def get_conexao() -> conn:
    return oracledb.connect(user='username', password='passwd', dsn='oracle.fiap.com.br/orcl')

def inclui(mensagem: dict):
    sql = """INSERT INTO tb_mensagem(assunto, destinatario, remetente, conteudo)
             VALUES (:assunto, :destinatario, :remetente, :conteudo)""" 
    with get_conexao() as conn:
        with conn.cursor() as cur:
            try:
                print(f"\nExecutando comando. Dados: {mensagem}\n")
                cur.execute(sql, mensagem)
                if cur.rowcount == 0:
                    print("Não foi possivel inserir a mensagem.")
                else:
                    print("Mensagem inserida com sucesso!\n")
            except oracledb.DatabaseError as e:
                erro, = e.args
                print(f"\nErro ao inserir mensagem. Dados: {mensagem}\nErro: {erro.message}")
        conn.commit()

def altera(mensagem: dict):
    sql = """UPDATE tb_mensagem 
             SET assunto = :assunto, destinatario = :destinatario, remetente = :remetente, conteudo = :conteudo 
             WHERE id = :id""" 
    with get_conexao() as conn:
        with conn.cursor() as cur:
            try:
                print(f"\nExecutando comando de atualização. Dados: {mensagem}\n")
                cur.execute(sql, mensagem)
                if cur.rowcount == 0:
                    print(f"Nenhuma mensagem encontrada com ID {mensagem['id']}.")
                else:
                    print("Mensagem atualizada com sucesso!\n")
            except oracledb.DatabaseError as e:
                erro, = e.args
                print(f"\nErro ao atualizar a mensagem de ID {mensagem.id}. Dados: {mensagem}\nErro: {erro.message}")
        conn.commit()

def recupera(id: int) -> dict:
    sql = "SELECT * FROM tb_mensagem WHERE id = :id"
    with get_conexao() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute(sql, {'id': id})
                resultado = cur.fetchone() 
                if resultado:
                    return {
                        'id': resultado[0],
                        'assunto': resultado[1],
                        'destinatario': resultado[2],
                        'remetente': resultado[3],
                        'conteudo': resultado[4]
                    }
                else:
                    return {}
            except oracledb.DatabaseError as e:
                erro, = e.args
                print(f"\nErro ao recuperar mensagem com ID: {id}\nErro: {erro.message}")
                return None

def recupera_assunto(assunto: str) -> list:
    sql = "SELECT * FROM tb_mensagem WHERE assunto LIKE :assunto"
    chaves_dicionario = ['id', 'assunto', 'destinatario', 'remetente', 'conteudo']
    with get_conexao() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute(sql, {'assunto': f'%{assunto}%'})
                resultado = cur.fetchall()
                return [dict(zip(chaves_dicionario, mensagem)) for mensagem in resultado]
            except oracledb.DatabaseError as e:
                erro, = e.args
                print(f"\nErro ao recuperar mensagens com assunto: {assunto}\nErro: {erro.message}")
                return None

def recupera_destinatario(destinatario: str) -> list:
    sql = "SELECT * FROM tb_mensagem WHERE destinatario = :destinatario"
    chaves_dicionario = ['id', 'assunto', 'destinatario', 'remetente', 'conteudo'] 
    with get_conexao() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute(sql, {'destinatario': f'{destinatario}'})
                resultado = cur.fetchall()
                return [dict(zip(chaves_dicionario, mensagem)) for mensagem in resultado]
            except oracledb.DatabaseError as e:
                erro, = e.args
                print(f"\nErro ao recuperar mensagens para destinatário: {destinatario}\nErro: {erro.message}")
                return None

def apaga(id: int):
    sql = "DELETE FROM tb_mensagem WHERE id = :id"
    with get_conexao() as conn:
        with conn.cursor() as cur:
            try:
                print(f"\nExecutando comando de deleção. ID: {id}\n")
                cur.execute(sql, {'id': id})
                if cur.rowcount == 0:
                    print(f"Nenhuma mensagem encontrada com ID {id}.")
                else:
                    print("Mensagem deletada com sucesso!\n")
            except oracledb.DatabaseError as e:
                erro, = e.args
                print(f"\nErro ao deletar mensagem com ID: {id}\nErro: {erro.message}")
        conn.commit()
