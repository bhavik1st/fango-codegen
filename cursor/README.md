# Fango Framework

Fango is a modern Python web framework inspired by Django, built on top of FastAPI. It provides a powerful and developer-friendly way to build web applications with a familiar Django-like structure and commands.

## Features

- FastAPI-powered backend for high performance
- Django-inspired project structure and commands
- Built-in admin interface
- Easy project and app scaffolding
- Modern async support
- Type hints and validation out of the box

## Installation

```bash
pip install fango
```

## Quick Start

1. Create a new Fango project:
```bash
fango-admin startproject myproject
cd myproject
```

2. Create a new app:
```bash
fango-admin startapp myapp
```

3. Run the development server:
```bash
python manage.py runserver
```

## Project Structure

After creating a new project, you'll get the following structure:

```
myproject/
├── manage.py
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── requirements.txt
```

When you create a new app, it will generate:

```
myapp/
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── routes.py
├── schemas.py
└── views.py
```

## Development

To contribute to Fango:

1. Clone the repository
2. Install development dependencies:
```bash
pip install -r requirements-dev.txt
```

3. Run tests:
```bash
pytest
```

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 