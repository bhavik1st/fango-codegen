#!/usr/bin/env python
import argparse
import os
import shutil
import sys

def create_project(project_name):
    """Creates a new Fango project directory structure."""
    try:
        os.makedirs(project_name, exist_ok=False)
    except FileExistsError:
        print(f"Error: Project '{project_name}' already exists.")
        return

    project_path = os.path.join(os.getcwd(), project_name)

    # Create project files
    with open(os.path.join(project_path, "main.py"), "w") as f:
        f.write(
            """from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello from Fango!"}
"""
        )

    with open(os.path.join(project_path, "requirements.txt"), "w") as f:
        f.write("fastapi\nuvicorn")

    # Create settings file
    with open(os.path.join(project_path, "settings.py"), "w") as f:
        f.write(
            """# Fango project settings
# You can add your settings here
"""
        )

    # Create apps directory
    os.makedirs(os.path.join(project_path, "apps"))

    print(f"Project '{project_name}' created successfully.")
    print(f"Navigate to '{project_name}' and run 'uvicorn main:app --reload' to start the server.")


def create_app(project_path, app_name):
    """Creates a new Fango app directory structure within a project."""
    app_path = os.path.join(project_path, "apps", app_name)

    try:
        os.makedirs(app_path, exist_ok=False)
    except FileExistsError:
        print(f"Error: App '{app_name}' already exists.")
        return
    except FileNotFoundError:
        print(f"Error: Project not found. Please run this command inside a Fango project directory.")
        return

    # Create app files
    with open(os.path.join(app_path, "models.py"), "w") as f:
        f.write("# Fango app models")

    with open(os.path.join(app_path, "schemas.py"), "w") as f:
        f.write("# Fango app schemas")

    with open(os.path.join(app_path, "routers.py"), "w") as f:
        f.write(
            """from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def app_root():
    return {"message": "Hello from app!"}
"""
        )

    with open(os.path.join(app_path, "__init__.py"), "w") as f:
        f.write("")

    print(f"App '{app_name}' created successfully in project '{os.path.basename(project_path)}'.")


def main():
    """Parses command-line arguments and executes the appropriate command."""
    parser = argparse.ArgumentParser(description="Fango Admin CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Create project command
    create_project_parser = subparsers.add_parser("createproject", help="Create a new Fango project")
    create_project_parser.add_argument("project_name", help="Name of the project")

    # Create app command
    create_app_parser = subparsers.add_parser("createapp", help="Create a new Fango app")
    create_app_parser.add_argument("app_name", help="Name of the app")

    args = parser.parse_args()

    if args.command == "createproject":
        create_project(args.project_name)
    elif args.command == "createapp":
        project_path = os.getcwd()
        create_app(project_path, args.app_name)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
