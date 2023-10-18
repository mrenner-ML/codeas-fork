DEFAULT_PROMPTS = {
    "generate_docstrings": {
        "action": "modify_code",
        "user_prompt": "Generate docstrings using numpy style.",
        "guidelines": ["clean_code"],
    },
    "guidelines": {
        "clean_code": """Use consistent and meaningful naming conventions for variables, functions, classes, and modules.
Don't repeat yourself. Reuse code through functions, classes, or libraries to minimize duplication.
Add comments to explain complex logic, but aim to write self-explanatory code.
"""
    },
}
