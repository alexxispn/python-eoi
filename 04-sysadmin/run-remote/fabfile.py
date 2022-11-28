from fabric.api import run, cd, env
from fabric.contrib.files import exists

PROJECT_REPO = 'https://github.com/alexxispn/django_polls.git'
PROJECT_NAME = 'django_polls'
PROJECT_PATH = f'/home/alexis/workspace/python/{PROJECT_NAME}'
PYTHON_VENV = f'{PROJECT_PATH}/.venv/bin/python3'
PIP_VENV = f'{PROJECT_PATH}/.venv/bin/pip'

env.hosts = ['3.15.38.15', '18.217.241.86']
env.user = 'alexis'


def git_clone():
    print('Cloning project')
    if exists(PROJECT_PATH):
        print('Project already exists - skipping clone')
        return
    run(f'git clone {PROJECT_REPO} {PROJECT_PATH}')


def create_env():
    print('Creating virtual environment')
    with cd(PROJECT_PATH):
        run('python3 -m venv .venv')


def install_requirements():
    print('Installing requirements')
    with cd(PROJECT_PATH):
        run(f'{PIP_VENV} install -r requirements.txt')


def run_migration():
    print('Running migrations')
    with cd(PROJECT_PATH):
        run(f'{PYTHON_VENV} manage.py migrate')


def load_data():
    print('Loading data')
    with cd(PROJECT_PATH):
        run(f'{PYTHON_VENV} manage.py loaddata fixtures/polls_data.json')


def runserver():
    print('Running server')
    with cd(PROJECT_PATH):
        run(f'{PYTHON_VENV} manage.py runserver')


def deploy():
    git_clone()
    create_env()
    install_requirements()
    run_migration()
    load_data()
    runserver()
