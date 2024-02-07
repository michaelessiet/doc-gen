# README for OpenAI Wrapper and Documentation Generator

## Overview

This repository contains a Python script that serves as a wrapper for the OpenAI API, specifically designed to facilitate the generation of documentation for code snippets. The core functionality is built around the OpenAI Python client, allowing users to submit code to the API and receive an automatically generated documentation snippet in return.

## Features

- **API Wrapper**: Simplifies interaction with the OpenAI API by handling authentication and request formatting.
- **Documentation Generation**: Leverages the `text-embedding-3-large` model (or other specified models) to generate concise, relevant documentation for provided code snippets.

## Prerequisites

Before you can use this script, you need to have the following:

- An OpenAI API key. You can obtain one by signing up at [OpenAI's website](https://beta.openai.com/signup/).
- The `openai` Python package installed in your environment. Install it using pip if you haven't already:
  ```bash
  pip install openai
  ```

## Usage

### Setting Up

1. Clone this repository to your local machine.
2. Ensure that you have set the `OPENAI_API_KEY` environment variable:
    ```bash
    export OPENAI_API_KEY='your_api_key_here'
    ```

### Using the Script

The script `openai_wrapper.py` defines a class `OpenAI` and a function `generateDocumentation`. Here's how to use them:

1. **OpenAI Class**: This class is instantiated with your OpenAI API key (fetched from environment variables). It's used internally by the `generateDocumentation` function and generally doesn't need to be interacted with directly.

2. **generateDocumentation Function**:
    - **Purpose**: Generates documentation for a given piece of code.
    - **Parameters**:
      - `code`: A string containing the code for which you want to generate documentation.
      - `model`: (Optional) The model ID to use for the completion. Defaults to `"text-embedding-3-large"`.
    - **Returns**: A string containing the generated documentation.

    **Example Usage**:
    ```python
    code_snippet = '''
    def add(a, b):
        return a + b
    '''

    documentation = generateDocumentation(code_snippet)
    print(documentation)
    ```

## Notes

- The generated documentation's quality and relevance may vary based on the input code and the chosen model. It's recommended to review and possibly edit the generated text before using it in a formal context.
- Be mindful of the OpenAI usage limits and costs associated with your API key.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check the issues page if you want to contribute.

## License

Distributed under the MIT License. See `LICENSE` for more information.

---

Remember, this is a starting point for your README. Depending on your project's complexity and scope, you might need to provide more specific installation instructions, usage examples, or information on dependencies.

For generating documentation based on code snippets, you would typically want a model that's proficient in understanding and generating human language, and that has some capability or training in interpreting programming code. As of the last update, the following models from OpenAI might be suitable for this task:

1. **`code-davinci-002` or its successors**: This model is fine-tuned for understanding and generating code. It's capable of explaining code, generating code from descriptions, and even writing tests. It can handle a broad range of programming languages and tasks related to code, including documentation generation.

2. **`davinci` or its successors**: While not as specialized in code as the `code-davinci` models, the `davinci` models are the most capable in terms of general language understanding and generation, which makes them quite versatile. They can still understand and generate code to a reasonable degree.

3. **`text-davinci-003` or its successors**: This model combines the strengths of the `davinci` model with enhanced ability to understand and generate natural language text. It's a good choice if your primary goal is detailed, human-like text generation, and you still need a reasonable understanding of code.

When choosing a model, consider the following:

- **Specificity to Programming Languages**: If your code snippets are in a specific language, check if the model has been trained or has shown proficiency in that language.
- **Balance Between Code and Natural Language**: Decide whether your priority is understanding code or generating natural, human-like text. Some models are better at one than the other.
- **Cost and Performance**: More capable models may also come with higher costs and slower response times. Balance the need for advanced capabilities with your budget and performance requirements.

For the task described, I would recommend starting with the `code-davinci-002` model or its successors, as they are optimized for understanding and generating code, which is central to generating accurate and useful documentation for code snippets. If you find that the model's natural language generation needs improvement for your use case, or if the code aspects are less complex, you might consider `text-davinci-003` or similar models. Always test with your specific use cases to find the best fit.
