import nox


@nox.session
def lint(session):
    """Checks for linting errors with ruff."""
    session.install("-r", "requirements.txt")
    session.run("ruff", "check")


@nox.session
def formatting(session):
    """Checks that code is correctly formatted using ruff."""
    session.install("-r", "requirements.txt")
    session.run("ruff", "format", "--check")
