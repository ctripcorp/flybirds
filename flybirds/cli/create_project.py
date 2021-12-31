# -*- coding: utf-8 -*-
"""
This module is used to create cli project.
"""
import os
import platform
import shutil

import typer

import flybirds.template as template


def create_demo():
    """
    Create project cli demo
    """
    typer.secho(
        "Welcome to flybirds cli. Please enter any information to continue.",
        fg=typer.colors.MAGENTA,
    )
    project_name = typer.prompt("Please input your project name>>")
    test_platform = typer.prompt(
        "Please input your test platform?(Android/IOS)"
    )
    device_id = "127.0.0.1:8200"
    package_name = "ctrip.android.view"
    web_driver_agent = "com.fd.test.WebDriverAgentLib.xctrunner"
    if test_platform is not None and test_platform.strip().lower() == 'ios':
        package_name = "com.ctrip.inner.wireless"

        is_bundle = typer.confirm(
            "Do you want to configure your webDriverAgent now?"
            "(this step can be skipped)")
        if is_bundle:
            web_driver_agent = typer.prompt("Please input your Bundle ID of"
                                            " webDriverAgent?")
        else:
            typer.secho(
                "You can configure your  Bundle ID of webDriverAgent later in"
                " the project's"
                " flybirds_config.json file.", fg=typer.colors.YELLOW)

    connect_device = typer.confirm(
        "Do you want to configure your deviceId now?"
        "(this step can be skipped)")
    if connect_device:
        device_id = typer.prompt("Please input your deviceId?")
    else:
        typer.secho("You can configure your deviceId later in the project's"
                    " flybirds_config.json file.", fg=typer.colors.YELLOW)

    if_package = typer.confirm(
        "Do you want to configure your packageName now?"
        "(this step can be skipped)")
    if if_package:
        package_name = typer.prompt(
            "Please input your packageName?(You can use"
            " the ADB command to view your package name"
            ", such as: adb shell pm list packages |"
            " findstr 'trip')"
        )
    else:
        typer.secho("You can configure your packageName later in the project's"
                    " flybirds_config.json file.", fg=typer.colors.YELLOW)

    try:
        typer.echo(f"Cloning into '{project_name}'...")
        total = 600
        with typer.progressbar(length=total, label="Processing") as progress:
            demo_path = copy_from_template(progress, project_name,
                                           test_platform, device_id,
                                           package_name, web_driver_agent)
        typer.secho(
            f"Done it! Create Project {project_name} has success!\n"
            f"You can find it at: {demo_path}",
            fg=typer.colors.MAGENTA,
        )
    except Exception:
        typer.secho(
            f"Error!! create project {project_name} has error",
            fg=typer.colors.MAGENTA,
            err=True,
        )


def copy_from_template(progress, project_name, test_platform, device_id=None,
                       package_name=None, web_driver_agent=None):
    """
    Generate project files from template
    """
    # Serialization path
    src_file_path = template.__file__
    src_path = os.path.normpath(src_file_path[0: src_file_path.rfind(os.sep)])
    target_path = os.path.normpath(
        os.path.join(os.path.normpath(os.getcwd()), project_name)
    )

    if os.path.isdir(target_path):
        # target_path is existed
        shutil.rmtree(target_path)
    shutil.copytree(src_path, target_path)
    progress.update(100)

    # delete file
    os.remove(os.path.normpath(os.path.join(target_path, "__init__.py")))
    progress.update(100)

    # modify platform
    if test_platform is not None:
        replace_file_content(
            os.path.join(target_path, "config/flybirds_config.json"),
            "platform",
            test_platform,
        )
    progress.update(100)

    # modify deviceId
    if device_id is not None:
        replace_file_content(
            os.path.join(target_path, "config/flybirds_config.json"),
            "deviceId",
            device_id,
        )
    progress.update(100)

    # modify packageName
    if package_name is not None:
        replace_file_content(
            os.path.join(target_path, "config/flybirds_config.json"),
            "packageName",
            package_name,
        )
    progress.update(100)

    # modify webDriverAgent
    if web_driver_agent is not None:
        replace_file_content(
            os.path.join(target_path, "config/flybirds_config.json"),
            "webDriverAgent",
            web_driver_agent,
        )
    progress.update(100)
    return target_path


def get_files_from_dir(dir):
    """
    Recursively get all files from the directory
    """
    files = []
    for main_dir, dirs, file_name_list in os.walk(dir):
        for file in file_name_list:
            file_path = os.path.join(main_dir, file)
            files.append(file_path)
    return files


def replace_file_content(file_path, key, value):
    """
    replace file content
    """
    new_file = ""
    with open(file_path, "r", encoding="utf-8") as f:
        new_file = f.read()
    new_file = new_file.replace(f"%{{{{{key}}}}}", f"{value}")
    # write file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_file)


def run_project(progress, target_path):
    """
    install packages
    """
    target_venv_path = os.path.normpath(
        os.path.join(target_path, activate_venv())
    )

    os.system(
        f"cd {target_path} && virtualenv venv && {target_venv_path} "
        f"&& pip install -r requirements.txt"
    )
    progress.update(100)


def activate_venv():
    """
    Activate venv
    :return:
    """
    sys_str = platform.system()
    if sys_str == "Windows":
        return "./venv/Scripts/activate"
    else:
        return "source venv/bin/activate"
