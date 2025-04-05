import os
import sys

def create_project(project_name):
    """Creates a new Fango project with the specified name."""
    os.makedirs(f"{project_name}/{project_name}/settings", exist_ok=True)
    os.makedirs(f"{project_name}/{project_name}/templates", exist_ok=True)
    os.makedirs(f"{project_name}/{project_name}/static", exist_ok=True)
    os.makedirs(f"{project_name}/apps", exist_ok=True)
    os.makedirs(f"{project_name}/tests", exist_ok=True)

    with open(f"{project_name}/manage.py", "w") as f:
        f.write(
            'from fastapi import FastAPI\n\n'
            'app = FastAPI()\n\n'
            'if __name__ == "__main__":\n'
            '    import uvicorn\n'
            '    uvicorn.run(app, host="127.0.0.1", port=8000)\n'
        )

    with open(f"{project_name}/{project_name}/__init__.py", "w") as f:
        f.write("# __init__.py: Initialize the project module\n")

    with open(f"{project_name}/{project_name}/settings/__init__.py", "w") as f:
        f.write("# settings/__init__.py: Project settings package\n")

    print(f"Project '{project_name}' created successfully.")

def create_app(app_name):
    """Creates a new Fango app with the specified name."""
    if not os.path.exists("apps"):
        print("Error: 'apps' directory not found. Run this command inside a Fango project.")
        return

    app_path = f"apps/{app_name}"
    os.makedirs(f"{app_path}/migrations", exist_ok=True)
    os.makedirs(f"{app_path}/templates/{app_name}", exist_ok=True)
    os.makedirs(f"{app_path}/static/{app_name}", exist_ok=True)

    with open(f"{app_path}/__init__.py", "w") as f:
        f.write("# __init__.py: Initialize the app module\n")

    with open(f"{app_path}/models.py", "w") as f:
        f.write("# models.py: Define app models\n")

    with open(f"{app_path}/views.py", "w") as f:
        f.write(
            'from fastapi import APIRouter\n\n'
            'router = APIRouter()\n\n'
            '@router.get("/")\n'
            'async def read_root():\n'
            '    return {"message": "Hello from the app!"}\n'
        )

    with open(f"{app_path}/urls.py", "w") as f:
        f.write(
            'from .views import router\n\n'
            'def include_router(app):\n'
            '    app.include_router(router, prefix="/{app_name}")\n'
        )

    print(f"App '{app_name}' created successfully.")

def main():
    if len(sys.argv) < 3:
        print("Usage: python fango-admin.py <command> <name>")
        print("Commands:")
        print("  startproject <project_name>  Create a new Fango project")
        print("  startapp <app_name>          Create a new Fango app")
        return

    command, name = sys.argv[1], sys.argv[2]
    if command == "startproject":
        create_project(name)
    elif command == "startapp":
        create_app(name)
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
