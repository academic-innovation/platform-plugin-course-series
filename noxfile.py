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


@nox.session
def migrations(session):
    """Checks that all expected migrations are present."""
    session.install("-r", "requirements.txt")
    session.run("python", "manage.py", "makemigrations", "--dry-run", "--check")


@nox.session
def test(session):
    """Runs tests with pytest."""
    session.install("-r", "requirements.txt")
    session.run("pytest")
