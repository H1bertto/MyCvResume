# MyCvResume

```sh
python -m venv env
activate.bat
pip install -r requirements.txt
```
Ajuste settings.py de acordo com suas informações
Após isso segue os comandos

```sh
python manage.py migrate
python manage.py collectstatic
gsutil -m rsync -R static/ gs://<YOUR_BUCKET>/static/
gcloud app deploy
```