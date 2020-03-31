# README

## env
```
Python 3.6.6
pyenv 1.2.13
pip 19.2.1
```

## requirements.txt

module list like Gemfile of ruby
```
pip freeze > requirements.txt # create module list
pip install -r requirements.txt # import module list
```

## running with docker

```
cd $WORKDIR
git clone https://github.com/watarun54/analyze_paper_api.git
cd $WORKDIR/analyze_paper_api
docker-compose up -d
```

Access the web endpoint at [http://localhost:80/scrape_paper](http://localhost:80/scrape_paper)
