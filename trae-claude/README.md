# Fango Framework

Fango is a modern Python web framework inspired by Django, built on top of FastAPI. It combines Django's elegant project structure and scaffolding with FastAPI's high performance and modern features.

## Features

- Django-like project structure
- Command-line tool (fango-admin) for project scaffolding
- FastAPI-based core for high performance
- Easy-to-use app creation and management

## Installation

```bash
# Coming soon: Will be available via pip
pip install fango
```

## Quick Start

1. Create a new project:
```bash
python fango-admin.py startproject myproject
```

2. Navigate to your project:
```bash
cd myproject
```

3. Create a new app:
```bash
python fango-admin.py startapp myapp
```

## Project Structure

After creating a project and an app, your directory structure will look like this:

```
myproject/
├── manage.py
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── asgi.py
└── myapp/
    ├── __init__.py
    ├── models.py
    ├── views.py
    └── routes.py
```

## Development

To contribute to Fango:

1. Clone the repository
2. Create a virtual environment
3. Install development dependencies
4. Run tests

## Testing

To test the fango-admin tool:

1. Clone this repository
2. Run the following commands:
```bash
# Test project creation
python fango-admin.py startproject testproject

# Test app creation
cd testproject
python fango-admin.py startapp testapp
```

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.