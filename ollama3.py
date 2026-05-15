from prompt3 import user_query
import subprocess
import re
import os


def get_response_userquery_from_ollama(user_input: str) -> str:

    prompt = user_query(user_input)

    process = subprocess.Popen(
        ["ollama", "run", "mistral"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding='utf-8',
        env={**os.environ, "TERM": "dumb"}
    )

    output, error = process.communicate(input=prompt)

    if process.returncode != 0:
        return "SELECT * FROM ocr_line_items"

    cleaned_query = output.strip()

    print("\n===== RAW SQL OUTPUT =====\n")
    print(cleaned_query)

    # Remove markdown
    cleaned_query = re.sub(r"```sql", "", cleaned_query)
    cleaned_query = re.sub(r"```", "", cleaned_query)

    # Remove ANSI escape sequences
    cleaned_query = re.sub(
        r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])',
        '',
        cleaned_query
    )

    # Remove terminal artifacts
    cleaned_query = re.sub(
        r'\[[0-9;]*[A-Za-z]',
        '',
        cleaned_query
    )

    cleaned_query = cleaned_query.strip()

    # Extract SQL only
    match = re.search(
        r"(SELECT|WITH).*",
        cleaned_query,
        re.IGNORECASE | re.DOTALL
    )

    if match:
        cleaned_query = match.group(0)

    cleaned_query = cleaned_query.strip()

    if not cleaned_query:
        return "SELECT * FROM ocr_line_items"

    return cleaned_query

"""description_text = "Pay to electricity board"
if __name__ == "__main__":
    category_list = get_response_category_from_ollama(user_input)
    print (category_list)"""