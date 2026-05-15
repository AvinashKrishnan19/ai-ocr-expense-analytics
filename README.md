# AI-Powered OCR Invoice Intelligence & Expense Analytics Platform

## Overview

This project is an end-to-end AI-powered OCR Invoice Intelligence System that extracts invoice data from images, converts unstructured OCR text into structured JSON using Large Language Models (LLMs), categorizes expenses automatically, stores the extracted information in SQLite, and provides an interactive Streamlit analytics dashboard with natural language SQL querying.

The platform combines Computer Vision, OCR, LLMs, databases, and dashboard analytics into a single intelligent expense management workflow.

---

# Features

## OCR-Based Invoice Extraction

* Extracts text from invoice and bill images using Tesseract OCR.
* Supports multiple invoice image formats.
* Handles noisy and scanned invoices.

## Image Preprocessing

* Grayscale conversion
* Gaussian blur noise reduction
* Thresholding and image cleaning using OpenCV
* Improved OCR accuracy for noisy invoices

## AI-Powered Invoice Parsing

* Uses Ollama + Mistral LLM for structured invoice extraction.
* Converts raw OCR text into valid JSON.
* Extracts:

  * Invoice Number
  * Invoice Date
  * Customer Name
  * Product Descriptions
  * Amounts
  * Grand Total

## Automated Expense Categorization

* Uses AI-based categorization for expense classification.
* Categories include:

  * Food
  * Grocery Expense
  * Logistics
  * Travel
  * Utilities
  * Drinks
  * Other

## SQLite Database Integration

* Stores structured invoice data into SQLite.
* Supports multiple invoice processing.
* Structured storage for analytics and querying.

## Streamlit Analytics Dashboard

* Interactive expense dashboard
* Dynamic filtering
* Invoice filtering
* Category-wise filtering
* Responsive expense table display

## AI-Powered Natural Language SQL Chatbot

Users can ask questions in natural language such as:

* Show all food category bills
* What is the total expense?
* Show expenses greater than 200
* Which invoice has the highest expense?

The system converts natural language into SQLite queries using LLMs.

---

# Project Architecture

```text
Invoice Image
      ↓
Image Preprocessing (OpenCV)
      ↓
OCR Text Extraction (Tesseract OCR)
      ↓
LLM JSON Structuring (Ollama + Mistral)
      ↓
Expense Categorization
      ↓
SQLite Database Storage
      ↓
Streamlit Analytics Dashboard
      ↓
Natural Language SQL Chatbot
```

---

# Tech Stack

| Technology    | Purpose                              |
| ------------- | ------------------------------------ |
| Python        | Backend Development                  |
| OpenCV        | Image Processing                     |
| Tesseract OCR | Text Extraction                      |
| Ollama        | Local LLM Runtime                    |
| Mistral LLM   | Invoice Structuring & SQL Generation |
| SQLite        | Database Storage                     |
| Pandas        | Data Processing                      |
| Streamlit     | Dashboard UI                         |
| Regex         | Data Cleaning                        |

---

# Folder Structure

```text
OCR Project/
│
├── inputocrimage/
├── outputocrimage/
├── extracted_text.txt
├── Image_cleaning.py
├── ocr_processor.py
├── parser.py
├── ollama1.py
├── ollama2.py
├── ollama3.py
├── prompt.py
├── prompt2.py
├── prompt3.py
├── data_insertion.py
├── table_creation.py
├── frontend.py
├── frontend2.py
├── ocr_master_table.db
├── requirements.txt
└── README.md
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/your-username/ai-ocr-expense-analytics.git
cd ai-ocr-expense-analytics
```

---

## 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Install Tesseract OCR

Download and install:

[https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)

Update Tesseract path inside:

```python
pytesseract.pytesseract.tesseract_cmd = r"YOUR_TESSERACT_PATH"
```

---

## 4. Install Ollama

Download Ollama:

[https://ollama.com/](https://ollama.com/)

Pull Mistral model:

```bash
ollama pull mistral
```

---

# Running the Project

## Step 1 — Image Cleaning

```bash
python Image_cleaning.py
```

---

## Step 2 — OCR Text Extraction

```bash
python ocr_processor.py
```

---

## Step 3 — Invoice Parsing

```bash
python parser.py
```

---

## Step 4 — Create Database Table

```bash
python table_creation.py
```

---

## Step 5 — Insert Data into SQLite

```bash
python data_insertion.py
```

---

## Step 6 — Launch Streamlit Dashboard

```bash
streamlit run frontend2.py
```

---

# Sample Natural Language Queries

```text
Show all food category bills

What is the total expense?

Show expenses greater than 200

Which invoice has the maximum total?

Show all grocery expenses
```

---

# Database Schema

| Column       | Description                 |
| ------------ | --------------------------- |
| Invoice_No   | Unique invoice ID           |
| line_item_id | Serial number for each item |
| Issue_Date   | Invoice date                |
| billed_to    | Customer name               |
| billed_by    | Vendor name                 |
| Description  | Product/service description |
| Category     | Expense category            |
| Amount       | Expense amount              |
| Grand_Total  | Total invoice amount        |
| source_file  | Source invoice image        |

---

# Key Learning Outcomes

This project demonstrates:

* OCR pipeline development
* Computer Vision preprocessing
* LLM integration using Ollama
* JSON data structuring
* AI-based expense classification
* SQLite database integration
* Streamlit dashboard development
* Natural Language to SQL conversion
* End-to-end AI workflow engineering

---

# Future Improvements

* PDF invoice support
* Multi-page invoice processing
* Multi-language OCR
* Cloud deployment
* Authentication system
* Expense analytics charts
* Export to Excel/PDF
* RAG-based invoice search
* Docker deployment
* REST API integration

---

# Screenshots

Add project screenshots here:

```text
screenshots/dashboard
screenshots/chatbot.png
screenshots/ocr_output.png
```

---

# Author

Avinash Krishnan

AI/ML Developer | OCR & LLM Automation

---

# License

This project is for educational and portfolio purposes.
