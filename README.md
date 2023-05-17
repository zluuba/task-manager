# Task Manager

[![Actions Status](https://github.com/zluuba/python-project-52/workflows/hexlet-check/badge.svg)](https://github.com/zluuba/python-project-52/actions)
[![Project Check](https://github.com/zluuba/python-project-52/actions/workflows/project-check.yml/badge.svg)](https://github.com/zluuba/python-project-52/actions/workflows/project-check.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/69e4fd04562de82f7d48/maintainability)](https://codeclimate.com/github/zluuba/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/69e4fd04562de82f7d48/test_coverage)](https://codeclimate.com/github/zluuba/python-project-52/test_coverage)


Plan, organize, and collaborate on any project with task management that will fit every need. <br>
Task Manager can **set tasks**, change their **statuses** and **assign responsibility**. <br>
**Log in** or **register** to take advantage of all the features.

It's [hosted on Railway](https://task-manager-production-70cb.up.railway.app/). <br>
If link doesn't work, you can run the app locally. Check the description below.


![Task-manager](https://user-images.githubusercontent.com/87614163/235889951-af73f69f-479f-4663-a55a-4ef839f13355.gif)

[See more demos](https://github.com/zluuba/task-manager#demos)


## Requirements

- [python](https://www.python.org/), version 3.9 or higher
- [poetry](https://python-poetry.org/docs/#installation), version 1.2.0 or higher


## Installation

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


## Environment

**Create .env file**. I prefer the text editor Nano, but you can do it any way you want:
1. Create .env file and open it with Nano:
    ```ch
    nano .env
    ```
2. Write down the secret key variable (paste your data after the equal sign):
    ```
    SECRET_KEY=AnySecretKey
    ```
3. Save this file using **CTRL + O** and Enter.
4. And close it with **CTRL + X**.


## Migrations, linter & tests

First of all, it is necessary to apply all **migrations** in this project. <br>
The next command creates migrations and applies them:
```ch
make migrations
```

This command starts the **linter** (using flake8) and checks the current project for cleanliness:
```ch
make lint
```

You can also run **tests** and make sure that the project works correctly with this command:
```ch
make test
```

Check the Makefile at the root of this project to see all available commands.


## After all package ready to go

Run WSGI server:
```ch
make start
```
Or you can use django development server:
```ch
make dev
```

And follow the [link you will see](http://0.0.0.0:8000) in the terminal window. <br>


## Additional environment variables

There are other useful environment variables in this project. <br>
To enable it, insert any of the following variables into the **.env** file on a new line >>

1. **Debug**. To enable debug mode and include all detailed data on errors, add this variable:
   ```ch
   DEBUG=True
   ```
2. **Rollbar** access token. **[Rollbar](https://rollbar.com/)** - crash reporting, error tracking, logging and error monitoring,
   he will warn you if something goes wrong. To enable it, you need to get an access token in your personal Rollbar account and add it as follows:
   ```ch
   ACCESS_TOKEN=YourRollbarAccessToken
   ```


## Demos

### Package setup
https://user-images.githubusercontent.com/87614163/235921770-0c2b1414-44d7-4207-859d-42d79d69af6b.mp4

### Usage: users
https://user-images.githubusercontent.com/87614163/235933792-a5efbd2b-8923-4a1e-840e-73378466ab49.mp4

### Usage: creating
https://user-images.githubusercontent.com/87614163/235934025-755e9264-c34e-445a-9eb2-94d83937fb0a.mp4

### Usage: updating & deleting
https://user-images.githubusercontent.com/87614163/235934169-9f074a30-ff34-47b2-9db7-8e59863759f6.mp4


---

**by [zluuba](https://github.com/zluuba)**
