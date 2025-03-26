# Python-Selenium-Pytest
This framework has been created for testing mobile version of [Twitch](https://m.twitch.tv/) application with Chrome browser.
## Setup Your Working Enviorment with terminal or CLI

* git clone
* cd to project directory 
* Install virtualenv:
```
py -m pip install --user virtualenv
```
* Create a virtual environment: 
```
py -m venv testenv
```
* Activate your virtual environment:
```
.\testenv\Scripts\activate
```
* install pipenv:
```
pip install pipenv
```
* install project dependencies using pipenv: 
```
pipenv install
```
## Setup work environment using IDE PyCharm
* download code as zip file from [Git](https://github.com/andrii-denysov/Python-Selenium-Pytest)
* Extract and open with Pycharm
* venv and dependencies will automatically setup and installed with notified pop-ups

## Run Tests

* Run according to tags:
```
pytest -k "<tag_name>" (e.g. pytest -k "smoke")
```