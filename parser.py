import os
import json
from ollama1 import get_json_from_prompt
from ollama2 import get_category_from_ollama

OCR_OUTPUT_FILE = "extracted_text.txt"

def parse_multiple_invoice():
    print("parsing started")

    if not os.path.exists(OCR_OUTPUT_FILE):
        print("file doesnot exists")
        return[]
    
    with open(OCR_OUTPUT_FILE, "r", encoding='utf-8') as f:
        master_text = f.read()

    bill_section = master_text.split("--Text from")[1:]
    total_bills= len(bill_section)
    print(f"total bills to be processed {total_bills}")

    all_structured_list =[]

    for section in bill_section:
        try:
            lines = section.strip().splitlines()

            filename = lines[0].replace("--", "").strip()

            bill_text = "\n".join(lines[1:])
            print(f"processing {filename}")

            #agent1 execution
            structured_data_dict = get_json_from_prompt(bill_text)


            if structured_data_dict:
                description_list = structured_data_dict.get("Description", [])
                enriched_description = []
                for item in description_list:
                    service_name = item.get("text", "").strip()
                    amt = item.get("amount")
                    print(f"  > Categorizing: {service_name}")
                    category_label = get_category_from_ollama(service_name)
                
                    enriched_item ={
                        "service_description": service_name,
                        "Amount": amt,
                        "category": category_label
                    }
                    enriched_description.append(enriched_item)

                structured_data_dict['Description'] = enriched_description
                structured_data_dict['source_file'] = filename

                all_structured_list.append(structured_data_dict)

            else:
                print(f"error in {filename}")

        except Exception as e:
            print(f"errr as {e}")

    return all_structured_list


if __name__ == "__main__":
    final_extracted_data = parse_multiple_invoice()
    print("\n final list of bills generated")
    print(json.dumps(final_extracted_data, indent=4))




            