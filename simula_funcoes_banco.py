from banco import altera,recupera,recupera_assunto,recupera_destinatario,apaga

def print_resultado(titulo, resultado):
    print(f"{titulo}:")
    if isinstance(resultado, list) and len(resultado) > 0:
        for msg in resultado:
            print(f"\nID: {msg['id']}, \nAssunto: {msg['assunto']}, \nDestinatário: {msg['destinatario']}, \nRemetente: {msg['remetente']}, \nConteúdo: {msg['conteudo']}")
    elif isinstance(resultado, dict) and resultado:
        print(f"\nID: {resultado['id']}, \nAssunto: {resultado['assunto']}, \nDestinatário: {resultado['destinatario']}, \nRemetente: {resultado['remetente']}, \nConteúdo: {resultado['conteudo']}")
    else:
        print("\nNenhuma mensagem encontrada")

if __name__ == "__main__":
    print("\nSimulando funções do banco.py...")

    print("\nSimulando a alteração de uma mensagem:")
    altera({
        'id': 1,
        'assunto': 'Novo Assunto',
        'destinatario': 'usuario1@example.com',
        'remetente': 'remetente1@example.com',
        'conteudo': 'Conteúdo atualizado.'
    })

    
    print("\nSimulando a recuperação de uma mensagem:")
    resultado_consulta = recupera(1)
    print_resultado("Mensagens com o ID 1", resultado_consulta)

    
    print("\nSimulando a recuperação de mensagens por assunto:")
    resultado_assunto = recupera_assunto('Atualização')
    print_resultado("Mensagens com o assunto 'Atualização'", resultado_assunto)

    
    print("\nSimulando a recuperação de mensagens por destinatário:")
    resultado_destinatario = recupera_destinatario('usuario2@example.com')
    print_resultado("Mensagens para 'usuario2@example.com'", resultado_destinatario)

    
    print("\nSimulando a exclusão de uma mensagem:")
    apaga(1)
