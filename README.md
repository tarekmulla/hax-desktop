[![Snyk Security](https://github.com/tarekmulla/hax-desktop/actions/workflows/snyk-security.yml/badge.svg)](https://github.com/tarekmulla/hax-desktop/actions/workflows/snyk-security.yml) [![Python Linting](https://github.com/tarekmulla/hax-desktop/actions/workflows/liniting.yml/badge.svg)](https://github.com/tarekmulla/hax-desktop/actions/workflows/liniting.yml) [![Unit Tests](https://github.com/tarekmulla/hax-desktop/actions/workflows/test.yml/badge.svg)](https://github.com/tarekmulla/hax-desktop/actions/workflows/test.yml)

# HaX Desktop tool

HaX is an AI-powered Cybersecurity tool designed to detect website vulnerabilities. Its cloud connection enhances capabilities for advanced analytics and modeling.

<p align="center">
  <img src="/docs/images/logo.png" alt="design" width="40%"/>
</p>


## About the project

This tool is expertly designed for ethical hacking, using intelligent cyber attack simulations to identify successful outcomes. It uploads results to the cloud for advanced data analytics, refining models for future attacks.


## 🧰 Tech stack

The application uses the following technology and tools.
| Technology / Tool | Purpose |
| ----------- | ----------- |
| [Python](https://www.python.org/) |  Build the atcual application |
| [TKinter](https://docs.python.org/3/library/tkinter.html) | Python package (“Tk interface”) to build the GUI interface |
| [Github actions](https://github.com/features/actions) | Automation pipelines |
| [Snyk](https://snyk.io/) | Security check ([SAST](https://snyk.io/learn/application-security/static-application-security-testing/) analysis, and [SCA](https://snyk.io/series/open-source-security/software-composition-analysis-sca/) analysis) |
| [CodeQL](https://codeql.github.com/) | Discover vulnerabilities across the codebase |
| [Dependabot](https://github.com/dependabot) | Send alert when the repository is using a dependency with a known vulnerability |
| [flake8](https://flake8.pycqa.org/) | Python linting tool |
| [mypy](https://mypy-lang.org/) | Python static type checker |
| [isort](https://pycqa.github.io/isort/) | modules import organizer |
| [pylint](https://pylint.readthedocs.io/en/latest/) | Python static code analyser |

## How do I get set up?

Feel free to clone the repository and create your own version of the application. However, kindly note that the source code is licensed under the `GPL-3.0 license`. To learn more about the license and its terms, please refer to the complete license documentation available [here](./LICENSE).


### Deployment prerequisites

Before running the application, make sure to meet the following requirements:
_**Note**: Those steps are working for both macOS, and Linux_

- Download and install python latest version, [check here](https://www.python.org/downloads/).
- Install pip, [check here](https://pip.pypa.io/en/stable/installation/).
- Install TKinter `brew install python-tk` or `make install-tk`. _**Note**: You need to have brew installed_.
- Install poetry, [check here](https://python-poetry.org/docs/).
- Install all dependencies by running  `poetry install`, the command will create a virtual environment, to understand how poetry works please refer to this [documentation](https://python-poetry.org/docs/configuration).
- You can run pytest using command `poetry run pytest`
- To run the package you can use command `poetry run python haxdesktop/main.py`


## Who do I talk to?

You can contact us directly using one of the following:
* 🖥️ Website: [haxsec.com](https://www.haxsec.com/)
* ✉️ Support Email [support@haxsec.com](mailto:support@haxsec.com)
