import json

JSON_SCHEMA = {
    "Invoice_No": "The unique invoice identifier",

    "Issue_Date": "The invoice date in MM/DD/YYYY format",

    "billed_to": "Customer or company name",

    "Description": [
        {
            "text": "Service or product description",
            "amount": "Numeric amount for this item"
        }
    ],

    "Grand_total": "Final invoice total amount"
}

def Data_conversion(extracted_text: str) -> str:

    return f"""
Return ONLY valid JSON.

STRICT SCHEMA:

{{
  "Invoice_No": "string",
  "Issue_Date": "string",
  "billed_to": "string",
  "Description": [
    {{
      "text": "string",
      "amount": 0
    }}
  ],
  "Grand_total": 0
}}

RULES:
- Do NOT add extra keys
- Do NOT add tax_details
- Do NOT add quantity
- Do NOT add address
- Do NOT add gst
- Do NOT add explanations
- Do NOT add markdown
- Do NOT add comments
- billed_to must ALWAYS be string
- Description items must ONLY contain:
    - text
    - amount

OCR TEXT:
{extracted_text}
"""