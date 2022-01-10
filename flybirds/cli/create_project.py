# -*- coding: utf-8 -*-
"""
This module is used to create cli project.
"""
import os
import platform
import shutil

import typer

import flybirds.template as template
import flybirds.utils.flybirds_log as log
from flybirds.utils.file_helper import get_files_from_dir, \
    get_paths_from_dir, \
    replace_file_content, update
from flybirds.utils.pkg_helper import find_package_base_path


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
        total = 700
        with typer.progressbar(length=total, label="Processing") as progress:
            demo_path = copy_from_template(progress, project_name,
                                           test_platform, device_id,
                                           package_name, web_driver_agent)
        typer.secho(
            f"Done it! Create Project {project_name} has success!\n"
            f"You can find it at: {demo_path}",
            fg=typer.colors.MAGENTA,
        )
    except Exception as e:
        typer.secho(
            f"Error!! create project {project_name} has error, errMsg: {e}",
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

    try:
        # process extend pkg
        add_extend_pkg(target_path)
    except Exception as e:
        log.error(f"[create_project][add_extend_pkg] has error, msg: {e}")

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


def add_extend_pkg(demo_path):
    """
    Add expansion pack
    """
    pkg_query = "-flybirds-plugin"
    pkg_list = find_package_base_path(pkg_query)
    if pkg_list is None or len(pkg_list) <= 0:
        log.info("[create_project][add_extend_pkg] has no extend packs need to"
                 "be added.")
        return

    copy_extend_files(pkg_list, demo_path)


def copy_extend_files(pkg_list, demo_pro_path):
    """
    Add extend features and config files
    """
    if demo_pro_path is None:
        return

    for pkg in pkg_list:
        # features src path
        extend_path = os.path.normpath(
            os.path.join(pkg.get("path"), pkg.get("name"), 'template'))

        if extend_path is None or not os.path.exists(extend_path):
            log.info(
                "[create_project][copy_extend_files]extend_path is none or not"
                "existed.")
            continue

        feat_path = os.path.join(os.path.normpath(extend_path), 'features')
        config_path = os.path.join(os.path.normpath(extend_path), 'config')

        # add extend features
        if feat_path is not None and os.path.exists(feat_path):
            feat_files = get_files_from_dir(feat_path)

            # features target path
            demo_an_paths = get_paths_from_dir(demo_pro_path, 'android')
            demo_ios_paths = get_paths_from_dir(demo_pro_path, 'ios')

            for an_path in demo_an_paths:
                for file in feat_files:
                    shutil.copy(file, an_path)

            for ios_path in demo_ios_paths:
                for file in feat_files:
                    shutil.copy(file, ios_path)

        # add extend config
        if config_path is not None and os.path.exists(config_path):
            # config target path
            demo_config_path = os.path.join(os.path.normpath(demo_pro_path),
                                            'config')
            if os.path.isdir(demo_config_path):
                # target_path is existed
                shutil.rmtree(demo_config_path)
            shutil.copytree(config_path, demo_config_path)


def write_import_steps(pkg_list, demo_pro_path, site_path):
    """
    Write the steps that needs to be imported
    """
    if site_path is None:
        return

    import_str = ''
    # str that need to be imported
    for pkg in pkg_list:
        step_path = os.path.normpath(
            os.path.join(pkg.get("path"), pkg.get("name"), 'dsl', 'step'))

        if step_path is None or not os.path.exists(step_path):
            log.info(
                "[create_project][write_import_steps] extend_step path is none"
                "or not existed.")
            continue

        step_files = os.listdir(step_path)
        pkg_import_str = ''
        if step_files is not None and len(step_files) > 0:
            pkg_import_str = f'from {pkg.get("name")}.dsl.step import'
        for file in step_files:
            stem, suffix = os.path.splitext(file)
            if '__init__' == stem or '__pycache__' == stem:
                continue
            pkg_import_str += " " + stem + ","

        import_str += pkg_import_str.strip(',') + "\n"

    # write the extension steps that need to be imported into the file
    steps_file = os.path.join(os.path.normpath(demo_pro_path),
                              'features/steps/steps.py')
    update(steps_file, import_str)
