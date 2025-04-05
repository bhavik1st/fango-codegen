#!/usr/bin/env python3

import os
import sys
import argparse
from pathlib import Path

def create_file(path, content=''):
    """Create a file with given content."""
    with open(path, 'w') as f:
        f.write(content)

def create_directory(path):
    """Create a directory if it doesn't exist."""
    os.makedirs(path, exist_ok=True)

def create_init_file(path):
    """Create an empty __init__.py file."""
    create_file(os.path.join(path, '__init__.py'))

def create_project(project_name):
    """Create a new Fango project."""
    # Create project directory
    create_directory(project_name)
    
    # Create project package directory
    package_dir = os.path.join(project_name, project_name)
    create_directory(package_dir)
    
    # Create __init__.py
    create_init_file(package_dir)
    
    # Create settings.py
    settings_content = '''from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Fango App"
    DEBUG: bool = True
    
settings = Settings()
'''
    create_file(os.path.join(package_dir, 'settings.py'), settings_content)
    
    # Create urls.py
    urls_content = '''from fastapi import APIRouter

router = APIRouter()

# Add your routes here
'''
    create_file(os.path.join(package_dir, 'urls.py'), urls_content)
    
    # Create asgi.py
    asgi_content = '''from fastapi import FastAPI
from .settings import settings

app = FastAPI(title=settings.APP_NAME, debug=settings.DEBUG)

# Import and include your route handlers here
'''
    create_file(os.path.join(package_dir, 'asgi.py'), asgi_content)
    
    # Create manage.py
    manage_content = '''#!/usr/bin/env python3
import uvicorn

if __name__ == "__main__":
    uvicorn.run("{}:app".format(__package__ + ".asgi"), host="127.0.0.1", port=8000, reload=True)
'''
    create_file(os.path.join(project_name, 'manage.py'), manage_content)
    os.chmod(os.path.join(project_name, 'manage.py'), 0o755)

def create_app(app_name):
    """Create a new Fango app."""
    # Create app directory
    create_directory(app_name)
    
    # Create __init__.py
    create_init_file(app_name)
    
    # Create models.py
    models_content = '''from pydantic import BaseModel

# Define your models here
'''
    create_file(os.path.join(app_name, 'models.py'), models_content)
    
    # Create views.py
    views_content = '''from fastapi import APIRouter

router = APIRouter()

# Define your views here
'''
    create_file(os.path.join(app_name, 'views.py'), views_content)
    
    # Create routes.py
    routes_content = '''from fastapi import APIRouter
from . import views

router = APIRouter()

# Include your view routes here
'''
    create_file(os.path.join(app_name, 'routes.py'), routes_content)

def main():
    parser = argparse.ArgumentParser(description='Fango management utility')
    parser.add_argument('command', choices=['startproject', 'startapp'], help='Command to execute')
    parser.add_argument('name', help='Name of the project or app')
    
    args = parser.parse_args()
    
    if args.command == 'startproject':
        create_project(args.name)
        print(f'Created project {args.name}')
    elif args.command == 'startapp':
        create_app(args.name)
        print(f'Created app {args.name}')

if __name__ == '__main__':
    main()