# doc-gen

This project provides a set of tools aimed at simplifying the documentation generation process for Python codebases by leveraging OpenAI's GPT models. It encapsulates the functionality to read and process directories and files, and generates documentation automatically using selected GPT models based on the content of the code or entire directories.

## Structure and Key Components

The project comprises several Python modules and configuration files:

- `pyproject.toml`: Configuration file for managing the project, its dependencies, and packaging information using Poetry.
- `README.md` & `test.md`: Markdown files providing an overview of the project, its usage, and documentation guidelines.
- `main.py`: The executable script that uses command-line options to either document a single file or an entire directory.
- `file_reader.py`: Contains functions for reading and compiling the contents of files and directories.
- `generator.py`: Interfaces with OpenAI's API to generate documentation based on provided code using GPT models.
- `README.generator.py.md`: Detailed documentation for the automatic documentation generation script.

### Dependencies
The project relies on several external libraries, notably:
- `requests` for making HTTP requests.
- `openai` for interacting with OpenAI's API.
- Other necessary libraries for running async operations, managing environment variables, and parsing data (`anyio`, `httpx`, `pydantic`, etc.).

The `pyproject.toml` file includes all dependencies, and the `poetry.lock` file locks the project to specific versions of these dependencies to ensure consistency.

## Getting Started

### Prerequisites

Ensure you have Python 3.12 or higher installed on your system. Additionally, you'll need Poetry for dependency management.

1. Clone this repository to your local machine.
2. Navigate to the project directory in the terminal.
3. Run `poetry install` to install all dependencies.

### Configuration

Before you can use the project, you'll need to obtain an OpenAI API key. Set this key as an environment variable named `OPENAI_API_KEY`:

```bash
export OPENAI_API_KEY='your_api_key_here'
```

### Usage

`main.py` is the primary entry point of the application. It offers options to document either a single Python file or all Python files within a directory.

#### To document a single file:

```bash
python main.py -d /path/to/your_file.py
```

This command generates a `README.your_file.py.md` file in the same directory as the input file, containing the generated documentation.

#### To document an entire directory:

```bash
python main.py -d /path/to/your_directory
```

This will scan the input directory, compile the Python files it contains into a single string, and generate a `README.md` file in the same directory with the documentation for the entire directory.

#### Build to single binary

```bash
./scripts/build.sh
```

This will create a single binary file named `main.bin`.

## Contributing

Contributions to this project are welcome. Please refer to the latter sections of `README.md` for guidelines on contributing, reporting issues, and submitting pull requests.

## Licensing

The project is available under the MIT License, which allows for a wide range of uses. Please see the `LICENSE` file for full license text.
