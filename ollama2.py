from prompt2 import build_category_prompt
import subprocess
import re 
import os

def get_category_from_ollama(description_text:str) -> str:
    prompt =build_category_prompt(description_text)


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
        return "uncategorized llm error"
    
    cleaned_category = re.sub(r'["\\]', '', output.strip()).strip()

    lines = cleaned_category.split('\n')
    final_category = lines[0].strip()

    if not final_category:
        return "Uncategorized - empty Response"
    
    return final_category 

description_text = "Pay to electricity board"
if __name__ == "__main__":
    category_list = get_category_from_ollama(description_text)
    print (category_list)


