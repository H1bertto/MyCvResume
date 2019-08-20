# MyCvResume

### Site em Django de Portifolio

Este projeto foi desenvolvido para que eu possa mostrar meu perfil, desenvolvimentos e conhecimentos de uma forma mais dinâmica e interessante, para pessoas que possam se interessar pelo meu trabalho e possam entrar em contato para entrevisas, contratações, parceirias ou até mesmo para tirar dúvidas sobre a linguagem Python, Django e Scrapy.\
O projeto está disponivel e pronto para deploy, faça apenas seus ajustes e deixei o site com o seu estilo.


__NOTA:__ O template usado foi comprado e foi feito por [Siful Islam](https://www.linkedin.com/in/getsiful/)


## Requisitos

- [Python 3.6+](https://www.python.org/downloads/)
- [Git]()

## Start

Para começar a usar e a desenvolver seu Site Portifolio siga o passo a passo:

1. Clone o Repositório
```sh
git clone https://github.com/H1bertto/MyCvResume.git
```

2. Mude Para pasta do Projeto e rode o comando `start.bat` (se seu SO for Linux) para que ele configure e ative o Ambiente Virtual Python para você, até já instala os `requirements.txt`
```sh
cd MyCvResume
start.bat
```

Ou se for Windows rode o comando `win-start.bat` 

```sh
cd MyCvResume
win-start.bat
```

3. Aplique a migração dos dados do models para serem aplicados ao banco de dados
```sh
python manage.py migrate
```

4. Crie um super usuario
```sh
python manage.py createsuperuser
```

5. Inicie sua aplicação
```sh
python manage.py runserver
```

__NOTA:__ Antes de você abrir o site *http://localhost:8000/*, você rpecisa entrar no */admin* e cadastrar o seu *Profile* com suas informações


## Deploy

Aqui vai uma opção de Deploy da sua aplicação no Google Cloud:

- Baixe e instale o GSUTIL
- Crie uma instância MySQL no Google Cloud
- Ajuste o DATABASE em `settings.py` de acordo com as informações da sua instância
- Com sua instância MySQL ativa, rode os comandos

```sh
python manage.py migrate
python manage.py collectstatic
```

- Crie um bucket no Google Cloud para seus arquvios estáticos da pasta `static`

```sh
gsutil mb gs://<YOUR_BUCKET>/
gsutil -m rsync -R static/ gs://<YOUR_BUCKET>/static/
```

- Troque o comentário das linhas abaixo em `settings.py`:

De:
```
STATIC_URL = '/static/'
# STATIC_URL = 'https://storage.googleapis.com/<YOUR_BUCKET>/static/'
```

Para:
```
# STATIC_URL = '/static/'
STATIC_URL = 'https://storage.googleapis.com/<YOUR_BUCKET>/static/'
```

__NOTA:__ Lembre-se de trocar `<YOUR_BUCKET>` pelo nome do seu Bucket


- Pronto, sua aplicação está pronta para o Deploy, rode o comando:

```sh
gcloud app deploy
```