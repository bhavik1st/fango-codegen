#!/usr/bin/env python
import argparse
import os
from pathlib import Path

TEMPLATES = {
    'project': {
        'structure': [
            'settings.py',
            'urls.py',
            'asgi.py',
            'apps/__init__.py'
        ],
        'content': {
            'asgi.py': """from fastapi import FastAPI
from .settings import settings

app = FastAPI(title=settings.PROJECT_NAME)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)""",
            'settings.py': """class Settings:
    PROJECT_NAME = '{{project_name}}'
    HOST = '0.0.0.0'
    PORT = 8000

settings = Settings()"""
        }
    },
    'app': {
        'structure': [
            '__init__.py',
            'models.py',
            'views.py',
            'routes.py'
        ],
        'content': {
            'routes.py': """from fastapi import APIRouter

router = APIRouter(prefix='/{{app_name}}')

# Add your routes here"""
        }
    }
}

def create_project(name):
    project_dir = Path(name)
    project_dir.mkdir(exist_ok=True)
    
    for file in TEMPLATES['project']['structure']:
        path = project_dir / file
        path.parent.mkdir(parents=True, exist_ok=True)
        
        if file in TEMPLATES['project']['content']:
            content = TEMPLATES['project']['content'][file].replace(
                '{{project_name}}', name
            )
            path.write_text(content)
        else:
            path.touch()
    
    print(f'Created project {name}')


def create_app(name):
    app_dir = Path('apps') / name
    app_dir.mkdir(parents=True, exist_ok=True)
    
    for file in TEMPLATES['app']['structure']:
        path = app_dir / file
        
        if file in TEMPLATES['app']['content']:
            content = TEMPLATES['app']['content'][file].replace(
                '{{app_name}}', name
            )
            path.write_text(content)
        else:
            path.touch()
    
    print(f'Created app {name}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fango administration utility')
    subparsers = parser.add_subparsers(dest='command')

    # Startproject command
    startproject = subparsers.add_parser('startproject', help='Create new project')
    startproject.add_argument('name', help='Project name')

    # Startapp command
    startapp = subparsers.add_parser('startapp', help='Create new app')
    startapp.add_argument('name', help='App name')

    args = parser.parse_args()

    if args.command == 'startproject':
        create_project(args.name)
    elif args.command == 'startapp':
        create_app(args.name)
    else:
        parser.print_help()