import pytest


@pytest.fixture(autouse=True)
def use_tmp_media_root(tmpdir, settings):
    """Stores files created during tests in a temporary directory."""
    settings.MEDIA_ROOT = tmpdir / "media"
