# Fango Framework

A Django-inspired framework built with FastAPI

## Installation

```bash
pip install -e .
```

## Usage

Create new project:
```bash
python fango-admin.py startproject myproject
```

Create new app:
```bash
cd myproject
python fango-admin.py startapp myapp
```

## Project Structure

New projects contain:
```
myproject/
├── asgi.py
├── settings.py
├── urls.py
└── apps/
    └── __init__.py
```

## Running the Server

```bash
uvicorn myproject.asgi:app --reload
```

## Testing

1. Verify project creation:
```bash
python fango-admin.py startproject testproject
ls testproject
```

2. Verify app creation:
```bash
cd testproject
python fango-admin.py startapp testapp
ls apps/testapp
```

3. Verify server starts:
```bash
uvicorn testproject.asgi:app --port 8001
```