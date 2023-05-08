# Task Manager

[![Actions Status](https://github.com/zluuba/python-project-52/workflows/hexlet-check/badge.svg)](https://github.com/zluuba/python-project-52/actions)
[![Project Check](https://github.com/zluuba/python-project-52/actions/workflows/project-check.yml/badge.svg)](https://github.com/zluuba/python-project-52/actions/workflows/project-check.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/69e4fd04562de82f7d48/maintainability)](https://codeclimate.com/github/zluuba/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/69e4fd04562de82f7d48/test_coverage)](https://codeclimate.com/github/zluuba/python-project-52/test_coverage)


Plan, organize, and collaborate on any project with task management that will fit every need. <br>
Task Manager can **set tasks**, change their **statuses** and **assign responsibility**. <br>
**Log in** or **register** to take advantage of all the features.

It's [hosted on Railway](https://task-manager-production-70cb.up.railway.app/). If link doesn't work, you can run the app locally.
Check the description below.


![Task-manager](https://user-images.githubusercontent.com/87614163/235889951-af73f69f-479f-4663-a55a-4ef839f13355.gif)

[See more demos](https://github.com/zluuba/task-manager#demos)



### Requirements

- [python](https://www.python.org/), version 3.9 or higher
- [poetry](https://python-poetry.org/docs/#installation), version 1.2.0 or higher


### Installation

Open terminal window.
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

Create .env file
```ch
nano .env
```

Write down the following environment variables (paste your data):
```ch
SECRET_KEY = 'AnySecretKey'
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
If you choose development server, you can also enable bedug mode by writing the following line in the .env file:
"**DEBUG = True**"


### Demos

#### Package setup

https://user-images.githubusercontent.com/87614163/235921770-0c2b1414-44d7-4207-859d-42d79d69af6b.mp4


#### Usage: users

https://user-images.githubusercontent.com/87614163/235933792-a5efbd2b-8923-4a1e-840e-73378466ab49.mp4

#### Usage: creating

https://user-images.githubusercontent.com/87614163/235934025-755e9264-c34e-445a-9eb2-94d83937fb0a.mp4

#### Usage: updating & deleting

https://user-images.githubusercontent.com/87614163/235934169-9f074a30-ff34-47b2-9db7-8e59863759f6.mp4


---

**by [zluuba](https://github.com/zluuba)**
