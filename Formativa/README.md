**API GERENCIAMENTO DE ESCOLA**\
\
Este projeto é uma API desenvolvida com Django e Django REST Framework para gerenciamento de professores, disciplinas e reservas de ambiente E JWT para autenticação\
Documentação: http://127.0.0.1:8000/swagger/
\
1. Criar area virtual e ative:
      python -m venv env \
      env\Scripts\activate \

2. Instalar as bibliotecas
      pip install -r requirements.txt

3.  Configure no settings.py o banco dados local

4.  Crie o gestor
      python manage.py createsuperuser

JWT para autenticação\
Para acessar os endpoints logar no http://127.0.0.1:8000/login/ com usuário e senha e salvar o token para utilização.
