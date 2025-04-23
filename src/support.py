import random
import webbrowser
from pathlib import Path

from InquirerPy import inquirer
from loguru import logger as log

from utilities.pros_cons import PROS, CONS


def generate_pros_and_cons_html(number_of_samples: int) -> None:
    """
    Generates an HTML file displaying a list of pros and cons and opens it in the default web browser.

    This function reads an HTML template file, dynamically populates it with a specified number of
    randomly selected pros and cons, and writes the rendered HTML to an output file. The output file
    is then opened in the default web browser.

    Args:
        number_of_samples (int): The number of pros and cons to include in the generated HTML.

    Raises:
        FileNotFoundError: If the HTML template file is not found.
        ValueError: If `number_of_samples` is greater than the available number of pros or cons.

    Returns:
        None
    """
    selected_pros = random.sample(PROS, k=number_of_samples)
    selected_cons = random.sample(CONS, k=number_of_samples)

    script_dir = Path(__file__).parent.resolve()
    template_path = script_dir / "web_elements/do-you-support-eyad.html"
    html_template = template_path.read_text(encoding="utf-8")

    pros_list = "".join(f"<li>{pro}</li>" for pro in selected_pros)
    cons_list = "".join(f"<li>{con}</li>" for con in selected_cons)
    rendered_html = html_template.replace("{{PROS_LIST}}", pros_list).replace(
        "{{CONS_LIST}}", cons_list
    )

    output_file = Path("./.temp/do-you-support-eyad.html")
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(rendered_html, encoding="utf-8")
    log.info(f"HTML file generated: {output_file.resolve()}")

    webbrowser.open(output_file.resolve().as_uri())


if __name__ == "__main__":
    log.warning("Do you support ya boi Eyad?")
    number_of_pros_and_cons = int(
        inquirer.number(
            message="How many pros and cons do you want to generate?",
            min_allowed=1,
            max_allowed=100,
            long_instruction="BRUH I couldn't leverage an api due to storage of an api key. So I had to generate a "
            "random list locally, leave me alone, just choose a number between 1 and 100",
        ).execute()
    )
    generate_pros_and_cons_html(number_of_samples=number_of_pros_and_cons)
