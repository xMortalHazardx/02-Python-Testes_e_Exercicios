import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviar_email(destinatario, assunto, mensagem):
    # Configurações do servidor SMTP do Office 365
    smtp_host = 'smtp.office365.com'
    smtp_port = 587
    usuario = 'seuemail@outlook.com'
    senha = 'suasenha'

    # Criação da mensagem
    msg = MIMEMultipart()
    msg['From'] = usuario
    msg['To'] = destinatario
    msg['Subject'] = assunto
    msg.attach(MIMEText(mensagem, 'plain'))

    # Contexto SSL para a conexão segura
    context = ssl.create_default_context()

    try:
        # Conectando ao servidor SMTP
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.starttls(context=context)
            server.login(usuario, senha)
            server.sendmail(usuario, destinatario, msg.as_string())
            print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

# Exemplo de uso
destinatario = 'destinatario@exemplo.com'
assunto = 'Assunto do E-mail'
mensagem = 'Este é o corpo do e-mail.'
enviar_email(destinatario, assunto, mensagem)