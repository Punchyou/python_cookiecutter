# Python 3.10 Project Cookiecutter

This is a Cookiecutter template for creating a Python 3.10 project with Docker support.

## Table of Contents

  - [Python 3.10 Project Cookiecutter](#python-310-project-cookiecutter)
  - [Table of Contents](#table-of-contents)
  - [Project Structure](#project-structure)
  - [Prerequisites](#prerequisites)
  - [Create a New Project](#create-a-new-project)
  - [Contributing](#contributing)
  - [License](#license)

## Project Structure

```
.
└── {{ cookiecutter.project_slug }}
    ├── Dockerfile
    ├── Dockerfile_test
    ├── README.md
    ├── __init__.py
    ├── cookiecutter.json
    ├── docker-compose.yml
    ├── requirements.txt
    ├── src
    │   ├── __init__.py
    │   └── app.py
    └── tests
        ├── __init__.py
        └── test_app.py
```

- **Dockerfile**: Defines the Docker image for the application.
- **Dockerfile_test**: Defines the Docker image for running tests.
- **README.md**: Project documentation.
- **__init__.py**: Marks the directory as a Python package.
- **cookiecutter.json**: Defines the template variables for Cookiecutter.
- **docker-compose.yml**: Docker Compose configuration file.
- **requirements.txt**: Python dependencies.
- **src/**: Source code directory.
  - **__init__.py**: Marks the directory as a Python package.
  - **app.py**: Main application script.
- **tests/**: Unit tests directory.
  - **__init__.py**: Marks the directory as a Python package.
  - **test_app.py**: Unit tests for the application.



## Prerequisites

- [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/installation.html)

## Create a New Project

1. Install Cookiecutter if you haven't already:

    ```
    pip install cookiecutter
    ```

2. Generate a new project using this template:

    ```
    cookiecutter https://github.com/Punchyou/python_cookiecutter
    ```

3. Follow the prompts to customize your project.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.