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
    replace_file_content, update, update_json_data
from flybirds.utils.pkg_helper import find_package_base_path


def create_demo():
    """
    Create project cli demo
    """
    typer.secho(
        "Welcome to flybirds cli. Please enter any information to continue.",
        fg=typer.colors.MAGENTA,
    )
    user_dict = {
        'device_id': "127.0.0.1:8200",
        'package_name': "ctrip.android.view",
        'web_driver_agent': "com.fd.test.WebDriverAgentLib.xctrunner",
        'headless': True,
        'browser_type': ['chromium']
    }
    project_name = typer.prompt("Please input your project name>>")
    user_dict['project_name'] = project_name
    platform_start = "Please input your test platform? "
    platform_ending = typer.style("(Android/IOS/Web)", fg=typer.colors.CYAN,
                                  bold=True)
    p_message = platform_start + platform_ending
    test_platform = typer.prompt(p_message)
    if test_platform is None or test_platform.strip().lower() not in [
        'android', 'ios', 'web']:
        test_platform = 'android'
    test_platform = test_platform.strip().lower()
    user_dict['test_platform'] = test_platform

    if test_platform in ['android', 'ios']:
        if test_platform == 'ios':
            user_dict['package_name'] = "com.ctrip.inner.wireless"
            is_bundle = typer.confirm(
                "Do you want to configure your webDriverAgent now?"
                "(this step can be skipped)")
            if is_bundle:
                web_driver_agent = typer.prompt(
                    "Please input your Bundle ID of"
                    " webDriverAgent?")
                user_dict['web_driver_agent'] = web_driver_agent
            else:
                typer.secho(
                    "You can configure your  Bundle ID of webDriverAgent later"
                    " in the project's"
                    " flybirds_config.json file.", fg=typer.colors.YELLOW)
        connect_device = typer.confirm(
            "Do you want to configure your deviceId now?"
            "(this step can be skipped)")
        if connect_device:
            device_id = typer.prompt("Please input your deviceId?")
            user_dict['device_id'] = device_id
        else:
            typer.secho(
                "You can configure your deviceId later in the project's"
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
            user_dict['package_name'] = package_name
        else:
            typer.secho(
                "You can configure your packageName later in the project's"
                " flybirds_config.json file.", fg=typer.colors.YELLOW)
    if test_platform == 'web':
        message_start = "Please enter the number represented by the " \
                        "browserType you want to test? Multiple browsers " \
                        "are separated by commas(,)."
        ending = typer.style("(1:chromium  2:firefox  3:webkit)",
                             fg=typer.colors.CYAN, bold=True)
        message = message_start + ending
        out_index = typer.prompt(message)
        index_arr = out_index.strip().split(',')
        browser_dict = {
            '1': "chromium",
            '2': "firefox",
            '3': "webkit"
        }
        browser_types = []
        [browser_types.append(browser_dict.get(i)) for i in index_arr if
         i in browser_dict.keys()]
        # add default value
        if len(browser_types) < 1:
            browser_types.append('chromium')
        user_dict['browser_type'] = browser_types
        headless = typer.confirm(
            "Do you want to launch browser in headless mode?")
        user_dict['headless'] = headless
    try:
        typer.echo(f"Cloning into '{project_name}'...")
        total = 900
        with typer.progressbar(length=total, label="Processing") as progress:
            demo_path = copy_from_template(progress, user_dict)
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


def create_mini():
    """
    Create mini project cli
    """
    user_dict = {}

    try:
        typer.echo(f"Cloning into ...")
        total = 900
        with typer.progressbar(length=total, label="Processing") as progress:
            demo_path = copy_from_template(progress, user_dict, os.path.normpath(os.getcwd()))
            compare_path = os.path.join(demo_path, "compareData")
            feat_files = get_files_from_dir(compare_path)

            config_ele = os.path.join(demo_path, "config/ele_locator.json")
            feat_files.append(config_ele)

            config_schema = os.path.join(demo_path, "config/schema_url.json")
            feat_files.append(config_schema)

            config_flybirds = os.path.join(demo_path, "config/flybirds_config.json")
            feat_files.append(config_flybirds)

            interface_path = os.path.join(demo_path, "interfaceIgnoreConfig/test.json")
            feat_files.append(interface_path)

            mock_path = os.path.join(demo_path, "mockCaseData/mock_test.json")
            feat_files.append(mock_path)

            for file in feat_files:
                os.remove(file)

            feature_path = os.path.join(demo_path, "features/test")
            shutil.rmtree(feature_path)

        typer.secho(
            f"Done it! Create Project has success!\n"
            f"You can find it at: {demo_path}",
            fg=typer.colors.MAGENTA,
        )
    except Exception as e:
        typer.secho(
            f"Error!! create project has error, errMsg: {e}",
            fg=typer.colors.MAGENTA,
            err=True,
        )


def copy_from_template(progress, user_dict, target=None):
    """
    Generate project files from template
    """
    # Serialization path
    src_file_path = template.__file__
    src_path = os.path.normpath(src_file_path[0: src_file_path.rfind(os.sep)])
    if target is None:
        target_path = os.path.normpath(
            os.path.join(os.path.normpath(os.getcwd()),
                         user_dict.get('project_name'))
        )
        if os.path.isdir(target_path):
            # target_path is existed
            shutil.rmtree(target_path)
    else:
        target_path = target

    shutil.copytree(src_path, target_path, dirs_exist_ok=True)
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
    test_platform = user_dict.get('test_platform')
    if test_platform is not None:
        replace_file_content(
            os.path.join(target_path, "config/flybirds_config.json"),
            "platform",
            test_platform,
        )
    progress.update(100)

    # modify deviceId
    device_id = user_dict.get('device_id')
    if device_id is not None:
        replace_file_content(
            os.path.join(target_path, "config/flybirds_config.json"),
            "deviceId",
            device_id,
        )
    progress.update(100)

    # modify packageName
    package_name = user_dict.get('package_name')
    if package_name is not None:
        replace_file_content(
            os.path.join(target_path, "config/flybirds_config.json"),
            "packageName",
            package_name,
        )
    progress.update(100)

    # modify webDriverAgent
    web_driver_agent = user_dict.get('web_driver_agent')
    if web_driver_agent is not None:
        replace_file_content(
            os.path.join(target_path, "config/flybirds_config.json"),
            "webDriverAgent",
            web_driver_agent,
        )
    progress.update(100)

    # modify browserType
    browser_type = user_dict.get('browser_type')
    if browser_type is not None:
        update_json_data(
            os.path.join(target_path, "config/flybirds_config.json"),
            "web_info.browserType",
            browser_type,
        )
    progress.update(100)

    # modify headless
    headless = user_dict.get('headless')
    if headless is not None:
        update_json_data(
            os.path.join(target_path, "config/flybirds_config.json"),
            "web_info.headless",
            headless,
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
        custom_handle_path = os.path.join(os.path.normpath(extend_path),
                                          'pscript', "custom_handle")
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

        # add extend custom operation
        if custom_handle_path is not None and os.path.exists(
                custom_handle_path):
            # config target path
            demo_custom_handle_path = os.path.join(
                os.path.normpath(demo_pro_path),
                'pscript', "custom_handle")
            if os.path.isdir(demo_custom_handle_path):
                # target_path is existed
                shutil.rmtree(demo_custom_handle_path)
            shutil.copytree(custom_handle_path, demo_custom_handle_path)


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
