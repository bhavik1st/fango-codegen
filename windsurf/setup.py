from setuptools import setup, find_packages

setup(
    name="fango",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "fastapi>=0.95.0",
        "uvicorn>=0.21.0",
        "pydantic>=1.10.7",
        "sqlalchemy>=2.0.9",
        "alembic>=1.10.3",
        "jinja2>=3.1.2",
    ],
    entry_points={
        "console_scripts": [
            "fango-admin=fango_admin:main",
        ],
    },
    author="Fango Team",
    author_email="example@example.com",
    description="A Django-inspired web framework built on FastAPI",
    keywords="web, framework, fastapi, django",
    url="https://github.com/yourusername/fango",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
)
