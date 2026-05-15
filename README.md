# 📊 Data Loading Project

📌 **Description**

This project demonstrates how to load and explore data files using Python (Pandas).
It supports multiple file formats including CSV, JSON, Excel, and Parquet.

## 📁 Project Structure
```text
project/
│
├── raw_data/
│   ├── student_coffee_crisis.csv
│   ├── student_coffee_crisis.json
│   ├── student_coffee_crisis.xlsx
│   └── student_coffee_crisis.parquet
│
├── load_data.py
├── requirements.txt
└── README.md
```

## ⚙️ Features
* **Load different data formats using Pandas**
* **Preview dataset using .head()**
* **Check dataset structure using .info()**
* **Work with Parquet files using pyarrow**

## 🚀 How to Run

1. **Install dependencies**
```bash
pip install -r requirements.txt
```
2. **Run the script**
```bash
python load_data.py
```
## 📦 Requirements
**pandas**
**openpyxl**
**pyarrow**

**To generate requirements file:**
```bash
pip freeze > requirements.txt
```

## 🧠 What This Project Shows
Basic data loading in Python
Handling multiple file formats
Simple data exploration using Pandas

## ⭐ Notes

Make sure the **raw_data** folder exists and contains all dataset files before running the script.