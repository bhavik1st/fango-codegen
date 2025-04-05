#!/usr/bin/env python3
import os
import sys
import shutil
import argparse
from pathlib import Path

def create_directory(path):
    """Create directory if it doesn't exist."""
    os.makedirs(path, exist_ok=True)

def write_file(path, content):
    """Write content to a file."""
    with open(path, 'w') as f:
        f.write(content)

def create_project(project_name):
    """Create a new Fango project."""
    base_dir = Path(project_name)
    project_dir = base_dir / project_name
    
    # Create project structure
    create_directory(base_dir)
    create_directory(project_dir)
    
    # Create manage.py
    manage_py_content = '''#!/usr/bin/env python3
import uvicorn
from pathlib import Path
import sys

def main():
    """Run the development server."""
    uvicorn.run(
        "{}:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )

if __name__ == "__main__":
    main()
'''.format(project_name)
    
    write_file(base_dir / 'manage.py', manage_py_content)
    os.chmod(base_dir / 'manage.py', 0o755)
    
    # Create __init__.py
    write_file(project_dir / '__init__.py', '')
    
    # Create settings.py
    settings_content = '''from pathlib import Path

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-your-secret-key-here'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'fastapi',
]

MIDDLEWARE = [
    'fastapi.middleware.cors.CORSMiddleware',
]

ROOT_URLCONF = '{}.urls'

TEMPLATES = [
    {{
        'BACKEND': 'fastapi.templating.Jinja2Templates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
    }},
]

# Database
DATABASES = {{
    'default': {{
        'ENGINE': 'sqlite',
        'NAME': BASE_DIR / 'db.sqlite3',
    }}
}}
'''.format(project_name)
    
    write_file(project_dir / 'settings.py', settings_content)
    
    # Create urls.py
    urls_content = '''from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI(title="{}")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return {{"message": "Welcome to {}"}}
'''.format(project_name, project_name)
    
    write_file(project_dir / 'urls.py', urls_content)
    
    # Create wsgi.py
    wsgi_content = '''from {}.urls import app

# This is for production servers
application = app
'''.format(project_name)
    
    write_file(project_dir / 'wsgi.py', wsgi_content)
    
    # Create requirements.txt
    requirements_content = '''fastapi>=0.68.0
uvicorn>=0.15.0
jinja2>=3.0.1
python-multipart>=0.0.5
sqlalchemy>=1.4.23
'''
    
    write_file(base_dir / 'requirements.txt', requirements_content)
    
    print(f"Created project '{project_name}' successfully!")
    print(f"To get started:")
    print(f"  cd {project_name}")
    print(f"  pip install -r requirements.txt")
    print(f"  python manage.py runserver")

def create_app(app_name):
    """Create a new Fango app."""
    app_dir = Path(app_name)
    create_directory(app_dir)
    
    # Create __init__.py
    write_file(app_dir / '__init__.py', '')
    
    # Create admin.py
    admin_content = '''from fastapi import APIRouter

router = APIRouter()

# Add your admin routes here
'''
    
    write_file(app_dir / 'admin.py', admin_content)
    
    # Create apps.py
    apps_content = '''class AppConfig:
    name = '{}'
    verbose_name = '{}'
'''.format(app_name, app_name.title())
    
    write_file(app_dir / 'apps.py', apps_content)
    
    # Create models.py
    models_content = '''from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Add your models here
'''
    
    write_file(app_dir / 'models.py', models_content)
    
    # Create routes.py
    routes_content = '''from fastapi import APIRouter

router = APIRouter()

# Add your routes here
'''
    
    write_file(app_dir / 'routes.py', routes_content)
    
    # Create schemas.py
    schemas_content = '''from pydantic import BaseModel

# Add your Pydantic models here
'''
    
    write_file(app_dir / 'schemas.py', schemas_content)
    
    # Create views.py
    views_content = '''from fastapi import APIRouter

router = APIRouter()

# Add your view functions here
'''
    
    write_file(app_dir / 'views.py', views_content)
    
    print(f"Created app '{app_name}' successfully!")
    print(f"Don't forget to add '{app_name}' to INSTALLED_APPS in your project's settings.py")

def main():
    parser = argparse.ArgumentParser(description='Fango admin utility')
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # startproject command
    startproject_parser = subparsers.add_parser('startproject', help='Create a new Fango project')
    startproject_parser.add_argument('name', help='Project name')
    
    # startapp command
    startapp_parser = subparsers.add_parser('startapp', help='Create a new Fango app')
    startapp_parser.add_argument('name', help='App name')
    
    args = parser.parse_args()
    
    if args.command == 'startproject':
        create_project(args.name)
    elif args.command == 'startapp':
        create_app(args.name)
    else:
        parser.print_help()

if __name__ == '__main__':
    main() 