import os

from fabric.api import local
from fabric.context_managers import lcd

PROJECT_REPO = 'git@github.com:alexxispn/django_polls.git'
PROJECT_NAME = 'django_polls'
PROJECT_PATH = f'/home/winvi/workspace/python/{PROJECT_NAME}'
PYTHON_VENV = f'{PROJECT_PATH}/.venv/bin/python3.11'
PIP_VENV = f'{PROJECT_PATH}/.venv/bin/pip'


def git_clone():
    print('Cloning project')
    if os.path.exists(PROJECT_PATH):
        print('Project already exists - skipping clone')
        return
    local(f'git clone {PROJECT_REPO} {PROJECT_PATH}')


def create_env():
    print('Creating virtual environment')
    with lcd(PROJECT_PATH):
        local('python3 -m venv .venv')


def install_requirements():
    print('Installing requirements')
    with lcd(PROJECT_PATH):
        local(f'{PIP_VENV} install -r requirements.txt')


def run_migration():
    print('Running migrations')
    with lcd(PROJECT_PATH):
        local(f'{PYTHON_VENV} manage.py migrate')


def load_data():
    print('Loading data')
    with lcd(PROJECT_PATH):
        local(f'{PYTHON_VENV} manage.py loaddata fixtures/polls_data.json')


def runserver():
    print('Running server')
    with lcd(PROJECT_PATH):
        local(f'{PYTHON_VENV} manage.py runserver')


def deploy():
    git_clone()
    create_env()
    install_requirements()
    run_migration()
    load_data()
    runserver()
