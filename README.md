# python-backend
It is a backend service providing rest api to render data. It is built with flask + sqlalchemy.

API design doc: https://www.notion.so/API-Doc-75ad818df5a64b74995ef3d1cca46cdf

API Mock-up: https://app.apiary.io/xpander/editor

API list: https://private-f7f12f4-xpander.apiary-mock.com/

# database setup
The development environment is python 3.7
Steps to setup database:
- ```pip install -r requirements.txt```
- put the desired parameters (USERNAME, PASSWORD, IP, PORT, DB) into /data_model/db_update.py
- ```python3.7 /data_model/db_update.py```
