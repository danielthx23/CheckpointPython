from banco import inclui

mensagens = [
    {'assunto': 'Reunião', 'destinatario': 'usuario1@example.com', 'remetente': 'remetente1@example.com', 'conteudo': 'Olá, gostaria de marcar uma reunião para discutir o projeto.'},
    {'assunto': 'Orçamento', 'destinatario': 'usuario2@example.com', 'remetente': 'remetente2@example.com', 'conteudo': 'Por favor, envie o orçamento atualizado para nossa análise.'},
    {'assunto': 'Proposta', 'destinatario': 'usuario3@example.com', 'remetente': 'remetente3@example.com', 'conteudo': 'Anexo a proposta para sua consideração.'},
    {'assunto': 'Feedback', 'destinatario': 'usuario4@example.com', 'remetente': 'remetente1@example.com', 'conteudo': 'Gostaria de receber seu feedback sobre o relatório enviado.'},
    {'assunto': 'Agradecimento', 'destinatario': 'usuario1@example.com', 'remetente': 'remetente2@example.com', 'conteudo': 'Obrigado pela ajuda com o projeto, sua contribuição foi essencial.'},
    {'assunto': 'Urgente', 'destinatario': 'usuario2@example.com', 'remetente': 'remetente3@example.com', 'conteudo': 'Preciso de uma resposta imediata sobre a situação atual.'},
    {'assunto': 'Pergunta', 'destinatario': 'usuario3@example.com', 'remetente': 'remetente1@example.com', 'conteudo': 'Você pode me ajudar com uma dúvida que estou tendo?'},
    {'assunto': 'Confirmação', 'destinatario': 'usuario4@example.com', 'remetente': 'remetente2@example.com', 'conteudo': 'Por favor, confirme sua presença na reunião agendada.'},
    {'assunto': 'Novo Projeto', 'destinatario': 'usuario1@example.com', 'remetente': 'remetente3@example.com', 'conteudo': 'Estou animado para trabalhar no novo projeto com você!'},
    {'assunto': 'Atualização de Sistema', 'destinatario': 'usuario2@example.com', 'remetente': 'remetente1@example.com', 'conteudo': 'Informamos que o sistema será atualizado no próximo fim de semana.'},
    {'assunto': 'Dúvida sobre a Tarefa', 'destinatario': 'usuario3@example.com', 'remetente': 'remetente2@example.com', 'conteudo': 'Tive uma dúvida sobre a tarefa que você me passou, poderia esclarecer?'},
    {'assunto': 'Nova Versão', 'destinatario': 'usuario4@example.com', 'remetente': 'remetente3@example.com', 'conteudo': 'A nova versão do aplicativo já está disponível para download.'},
    {'assunto': 'Compromisso Agendado', 'destinatario': 'usuario1@example.com', 'remetente': 'remetente1@example.com', 'conteudo': 'Seu compromisso foi agendado para amanhã às 10h.'},
    {'assunto': 'Mudança de Endereço', 'destinatario': 'usuario2@example.com', 'remetente': 'remetente2@example.com', 'conteudo': 'Gostaria de informar que mudamos nosso endereço de correspondência.'},
    {'assunto': 'Férias', 'destinatario': 'usuario3@example.com', 'remetente': 'remetente3@example.com', 'conteudo': 'Estou de férias na próxima semana, por favor, entre em contato com meu colega.'},
    {'assunto': 'Almoço de Equipe', 'destinatario': 'usuario4@example.com', 'remetente': 'remetente1@example.com', 'conteudo': 'Vamos almoçar juntos na próxima sexta-feira?'},
    {'assunto': 'Lembrete', 'destinatario': 'usuario1@example.com', 'remetente': 'remetente2@example.com', 'conteudo': 'Este é um lembrete sobre a apresentação de amanhã.'},
    {'assunto': 'Encerramento de Projeto', 'destinatario': 'usuario2@example.com', 'remetente': 'remetente3@example.com', 'conteudo': 'Estamos nos preparando para o encerramento do projeto, obrigado a todos pelo esforço.'},
    {'assunto': 'Reunião de Feedback', 'destinatario': 'usuario3@example.com', 'remetente': 'remetente1@example.com', 'conteudo': 'Gostaria de agendar uma reunião para receber seu feedback sobre o último projeto.'},
    {'assunto': 'Novidades da Empresa', 'destinatario': 'usuario4@example.com', 'remetente': 'remetente2@example.com', 'conteudo': 'Temos algumas novidades emocionantes para compartilhar com todos!'}
]

if __name__ == "__main__":
    for mensagem in mensagens:
        inclui(mensagem)
    print("20 mensagens foram inseridas com sucesso!")
