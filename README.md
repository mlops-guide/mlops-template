# mlops-template
🍪 Cookiecutter template for MLOps Project based on the MLOps Guide

Example proejct: https://github.com/MLOPsStudyGroup/dvc-gitactions

This template can be used to develop a project based on the MLOps guide: https://mlopsstudygroup.github.io/mlops-guide/


## Ideal  Stack
- Data Versioning: DVC
- Machine Learning Pipeline: DVC Pipeline (preprocess, train, evaluate)
- CI/CD: Unit testing with Pytest, pre-commit and Github Actions
- CML: Continuous Machine Learning and Github Actions
- Deploy on release: Github Actions and IBM Watson
- Monitoring: IBM OpenScale
- Infrastructure-as-a-code: Terraform script

## Installing

### Install cookiecutter
Cookiecutter is a CLI tool used to create projects based on templates. It supports Windows, Linux and MacOS officially. The instalation process is listed on their documentation: https://cookiecutter.readthedocs.io/en/1.7.2/installation.html

### Use Template
This is runs cookiecutter and creates a project based on this template and the response from questions asked on the CLI, such as: ```author```,```project_name```,```open_source_license``` and others.
```
cookiecutter https://github.com/MLOPsStudyGroup/mlops-template.git
```
