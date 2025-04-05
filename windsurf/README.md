# Fango Framework

Fango is a modern Python web framework inspired by Django but built on top of FastAPI. It combines the developer-friendly structure of Django with the high performance and modern features of FastAPI.

## Features

- **Django-like Project Structure**: Familiar organization for Django developers
- **FastAPI Core**: High performance, easy async support, and automatic OpenAPI documentation
- **Scaffolding Tools**: Easy project and app creation with `fango-admin`

## Installation

```bash
pip install -e .
```

## Quick Start

### Create a new project

```bash
fango-admin create-project myproject
```

This will create a new project with the following structure:

```
myproject/
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── asgi.py
└── manage.py
```

### Create a new app

```bash
cd myproject
fango-admin create-app myapp
```

This will create a new app with the following structure:

```
myapp/
├── __init__.py
├── models.py
├── views.py
├── schemas.py
└── urls.py
```

### Run the development server

```bash
python manage.py runserver
```

## Testing the Scaffolding Tool

To test the `fango-admin` tool without installing the package:

```bash
# Clone the repository
git clone https://github.com/yourusername/fango.git
cd fango

# Run the fango-admin script directly
python fango_admin.py create-project testproject
cd testproject
python ../fango_admin.py create-app testapp

# Or make it executable and run it
chmod +x fango_admin.py
./fango_admin.py create-project testproject
```

## License

MIT
