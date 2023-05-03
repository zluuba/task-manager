# Task Manager

[![Actions Status](https://github.com/zluuba/python-project-52/workflows/hexlet-check/badge.svg)](https://github.com/zluuba/python-project-52/actions)
[![Project Check](https://github.com/zluuba/python-project-52/actions/workflows/project-check.yml/badge.svg)](https://github.com/zluuba/python-project-52/actions/workflows/project-check.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/69e4fd04562de82f7d48/maintainability)](https://codeclimate.com/github/zluuba/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/69e4fd04562de82f7d48/test_coverage)](https://codeclimate.com/github/zluuba/python-project-52/test_coverage)


This is a task management system. <br>
Plan, organize, and collaborate on any project with task management that will fit every need. <br>
Task Manager can **set tasks**, change their **statuses** and **assign responsibility**. <br>
**Log in** or **register** to take advantage of all the features.

It's [hosted on Railway](https://railway.app/). If link doesn't work, you can run the app locally.
Check the description below.


![Task-manager](https://user-images.githubusercontent.com/87614163/235889951-af73f69f-479f-4663-a55a-4ef839f13355.gif)


[See more demos](https://github.com/zluuba/python-project-52#demos)



### Requirements

- [python](https://www.python.org/), version 3.9 or higher
- [poetry](https://python-poetry.org/docs/#installation), version 1.0.0 or higher


### Installation

Clone this repo or download it with pip:
```ch
git clone https://github.com/zluuba/task-manager.git
```
```ch
pip install --user git+https://github.com/zluuba/task-manager.git
```

Go to the downloaded dir and install dependencies:
```ch
cd task-manager
make install
```

### Create .env file

```ch
nano .env
```
Write down the following environment variables (paste your data):
```ch
SECRET_KEY = 'AnySecretKey'
ACCESS_TOKEN = 'AnyCharactersForAccessToken'
```

### After all package ready to go
Run WSGI server and follow the [link you will see](http://0.0.0.0:8000):
```ch
make start
```
Or you can use django development server:
```ch
make dev
```
//write about DEBUG in settings.py//

### Afterword
This project use //technology list//


### Demos

#### Package setup


#### Usage


**by [zluuba](https://github.com/zluuba)**
