categories =[
    "food", "logistics", "drinks", "travel", "grocery expense", "utilities", "Other" 
]

def build_category_prompt(description_text:str) -> str:
    category_list = ",".join(categories)
    return f"""
You are an intelligent expense classification AI.

Your task is to analyze the bill or invoice description and classify it into ONLY ONE category.

Available Categories:
{category_list}

Rules:
- Return only one category name
- Do not explain anything
- If no category matches, return "Other"

Bill Description:
{description_text}
"""





