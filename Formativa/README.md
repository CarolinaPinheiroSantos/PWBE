**API GERENCIAMENTO DE ESCOLA**\
\
Este projeto é uma API desenvolvida com Django e Django REST Framework para gerenciamento de professores, disciplinas e reservas de ambiente E JWT para autenticação\
Documentação: http://127.0.0.1:8000/swagger/

1. Criar area virtual:\
      python -m venv env e ative com env\Scripts\activate 

3. Instalar as bibliotecas
      pip install -r requirements.txt

4.  Configure no settings.py o banco dados local

5.  Crie o gestor
      python manage.py createsuperuser

JWT para autenticação \
Para acessar os endpoints logar no http://127.0.0.1:8000/login/ com usuário e senha e salvar o token para utilização.
