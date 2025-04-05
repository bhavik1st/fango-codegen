# Fango Framework

Fango is a lightweight Python framework inspired by Django, built on top of FastAPI. It provides scaffolding tools to create projects and apps with ease.

## Features
- Create a new Fango project using `fango-admin.py`.
- Create apps within a project with pre-defined folder structures and boilerplate code.

## Installation
1. Ensure Python 3.7+ is installed.
2. Install FastAPI and Uvicorn:
   ```bash
   pip install fastapi uvicorn
   ```

## Usage

### Create a New Project
Run the following command to create a new project:
```bash
python fango-admin.py startproject <project_name>
```
This will generate a folder structure similar to:
```
<project_name>/
    manage.py
    <project_name>/
        __init__.py
        settings/
            __init__.py
        templates/
        static/
    apps/
    tests/
```

### Create a New App
Run the following command inside the project directory:
```bash
python fango-admin.py startapp <app_name>
```
This will generate a folder structure similar to:
```
apps/
    <app_name>/
        __init__.py
        models.py
        views.py
        urls.py
        migrations/
        templates/<app_name>/
        static/<app_name>/
```

### Running the Project
1. Navigate to the project directory.
2. Run the project using:
   ```bash
   python manage.py
   ```
3. Open your browser and visit `http://127.0.0.1:8000`.

## Testing
- Verify the project structure is created correctly.
- Add routes in `views.py` and include them in `urls.py`.
- Start the server and test the endpoints.

Enjoy building with Fango!
