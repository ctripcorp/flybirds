# -*- coding: utf-8 -*-
"""
project cli
"""
from typing import List, Optional

import typer

import flybirds.utils.flybirds_log as log
from flybirds.cli.create_project import create_demo
from flybirds.cli.parse_args import parse_args, default_report_path
from flybirds.core.launch_cycle.run_manage import run_script

app = typer.Typer(
    help='Welcome to flybirds. Type "--help" for more information.',
    no_args_is_help=True,
)


@app.command("run")
def runner(
        feature_path: str = typer.Option(
            "features",
            "--path",
            "-P",
            help="Feature path that needs " "to be executed",
        ),
        tag: str = typer.Option(
            None,
            "-T",
            "--tag",
            help="Run scenarios with a specific tag. "
                 "Multiple scenarios are separated by "
                 "commas(,). "
                 "e.g. flybirds run --tag tag1,-tag2,tag4",
        ),
        report_format: str = typer.Option(
            "--format=json", "--format", "-F", help="Result format."
        ),
        report_path: str = typer.Option(
            default_report_path,
            "-R",
            "--report",
            help="The path to generate the report.",
        ),
        define: Optional[List[str]] = typer.Option(
            None,
            "-D",
            "--define",
            help="User-defined parameters. e.g. --define screenShotDir=cmVwb.",
        ),
        rerun: bool = typer.Option(
            True,
            "--rerun/--no-rerun",
            help="Whether the failed scenario needs to be rerun",
        ),
        es: str = typer.Option(
            None, "--es", help="APP boot environment parameters"
        ),
        to_html: bool = typer.Option(
            True, "--html/--no-html", help="Whether to generate HTML report"
        ),
        run_at: str = typer.Option(
            "local", "--run-at", help="Run environment, extended parameters"
        )
):
    """
    Run the project.
    """
    # process args
    run_args = parse_args(
        feature_path, tag, report_format, report_path, define, rerun, es,
        to_html, run_at
    )
    log.info("============last run_args: {}".format(str(run_args)))
    run_script(run_args)


@app.command("create")
def create_project():
    """
    Generate project example
    """
    create_demo()


if __name__ == "__main__":
    app()
