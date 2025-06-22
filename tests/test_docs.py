import pathlib
import pytest

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]

README = REPO_ROOT / 'README.md'
INDEX_HTML = REPO_ROOT / 'index.html'

@pytest.mark.parametrize('path', [README, INDEX_HTML])
def test_file_exists_and_not_empty(path):
    assert path.exists(), f"{path} should exist"
    content = path.read_text().strip()
    assert content, f"{path} should not be empty"
