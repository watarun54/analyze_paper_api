# README

* env
```
Python 3.6.6
pyenv 1.2.13
pip 19.2.1
```

* start project
```
pip install [module]
python app.py
```

* requirements.txt

module list like Gemfile of ruby
```
pip freeze > requirements.txt # create module list
pip install -r requirements.txt # import module list
```

* deploy flask with (ubuntu16.04/nginx/uWSGI)

```
git clone [this repos]
cd [this repos]
pyenv local 3.6.6
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
pip install uwsgi
...
```

[flask を uWSGI と Nginx でデプロイする](https://qiita.com/ekzemplaro/items/a570f79de254428a151d)

[How To Serve Flask Applications with uWSGI and Nginx on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-16-04)
