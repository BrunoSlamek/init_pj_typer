import typer
import os

app = typer.Typer()


def create_django_project(path: str, project_name: str, app_name: str):
    os.system(f'\
        cmd /c "cd {path} & \
            django-admin startproject {project_name} . & \
                django-admin startapp {app_name} & \
                    cd {app_name} & \
                         type nul > serializers.py & \
                            mkdir api & \
                                cd api & \
                                    type nul > __ini__.py & \
                                        type nul > api.py"')


if __name__ == "__main__":
    typer.run(create_django_project)