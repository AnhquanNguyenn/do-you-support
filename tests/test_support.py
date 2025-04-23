import pytest
from unittest.mock import patch, MagicMock
from pathlib import Path
from src.support import generate_pros_and_cons_html


@pytest.fixture
def temp_output_file():
    output_file = Path("./.temp/do-you-support-eyad.html")
    output_file.parent.mkdir(parents=True, exist_ok=True)
    yield output_file
    if output_file.exists():
        output_file.unlink()


@patch("src.support.random.sample")
@patch("src.support.webbrowser.open")
@patch("src.support.PROS", new=["Pro 1", "Pro 2", "Pro 3"])
@patch("src.support.CONS", new=["Con 1", "Con 2", "Con 3"])
def test_generate_pros_and_cons_html(
    mock_webbrowser_open: MagicMock,
    mock_random_sample: MagicMock,
    temp_output_file: Path,
) -> None:
    mock_random_sample.side_effect = lambda x, k: x[:k]
    generate_pros_and_cons_html(number_of_samples=2)

    assert temp_output_file.exists(), "Output HTML file was not created."
    content = temp_output_file.read_text(encoding="utf-8")
    assert "<li>Pro 1</li>" in content
    assert "<li>Pro 2</li>" in content
    assert "<li>Con 1</li>" in content
    assert "<li>Con 2</li>" in content
    mock_webbrowser_open.assert_called_once_with(temp_output_file.resolve().as_uri())
