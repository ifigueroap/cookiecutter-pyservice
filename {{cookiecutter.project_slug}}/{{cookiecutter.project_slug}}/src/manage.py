import logging

import typer

from settings import settings

app = typer.Typer()
logger = logging.getLogger(__name__)
state = {"verbose": False}


def log_verbose(s):
    """Print string s if verbose is True."""
    if state["verbose"]:
        typer.echo(s)


@app.callback()
def main(verbose: bool = typer.Option(False, "--verbose", "-v")):
    """Typer app entry point."""
    if verbose:
        typer.echo("Verbose activated")
        state["verbose"] = True


@app.command()
def hello():
    """Say hello!."""
    typer.echo("Hello!")
    typer.echo(settings)


if __name__ == "__main__":
    app()
