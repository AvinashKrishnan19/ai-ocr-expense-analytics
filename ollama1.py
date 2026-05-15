from prompt import Data_conversion
import subprocess
import re
import json
import os


def get_json_from_prompt(raw_invoice_text:str) -> str:
    prompt = Data_conversion(raw_invoice_text)

    #Execute Ollama subprocess
    # using llama3 is recommended
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
        raise RuntimeError(f'Ollama Failed: {error}')
    
    #clean the llm Output
    cleaned_output = output.strip()

    print("\n===== RAW LLM OUTPUT =====\n")
    print(cleaned_output)

    # Remove markdown if exists
    cleaned_output = re.sub(r"```json", "", cleaned_output)
    cleaned_output = re.sub(r"```", "", cleaned_output)

    cleaned_output = cleaned_output.strip()
     


    try:

        # Remove ANSI escape sequences
        cleaned_output = re.sub(
            r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])',
            '',
            cleaned_output
        )

        # Remove terminal artifacts
        cleaned_output = re.sub(
            r'\[[0-9;]*[A-Za-z]',
            '',
            cleaned_output
        )

        # Extract JSON only
        start = cleaned_output.find("{")
        end = cleaned_output.rfind("}") + 1

        cleaned_output = cleaned_output[start:end]

        # Remove control characters
        cleaned_output = re.sub(
            r'[\x00-\x1F\x7F]',
            '',
            cleaned_output
        )

        # Normalize spaces
        cleaned_output = re.sub(r'\s+', ' ', cleaned_output)

        cleaned_output = cleaned_output.strip()

        result = json.loads(cleaned_output)

        return result

    except Exception as e:

        print(f"\nJSON Parse Error: {e}")

        print("\nCLEANED OUTPUT:\n")
        print(cleaned_output)

        return None


if __name__ == "__main__":

    SAMPLE_INVOICE_TEXT ="""
        Invoice No: 52451
        Isuue Date: 12/25/2025
        Description: Product shipment, consulting fee
        Amount: 500.00
        Grand Total: $500.00
        """
    result_dict=get_json_from_prompt(SAMPLE_INVOICE_TEXT)
    print("\n===== FINAL JSON =====\n")
    print(result_dict)
