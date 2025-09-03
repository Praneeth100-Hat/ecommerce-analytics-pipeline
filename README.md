# 🛒 Ecommerce Analytics Pipeline  
End-to-end ETL + analytics project using Python, Pandas, SQLite, and Jupyter. Extracts raw ecommerce sales data, cleans/transforms it, loads it into SQLite, and delivers reports & visualizations.  

---

## 🚀 Features
- Extracts raw ecommerce sales data from CSV  
- Cleans and transforms messy data  
- Loads into SQLite database for storage and querying  
- Generates reports (monthly sales, top products, revenue by country, etc.)  
- Provides analysis & visualizations in Jupyter  

---

## 🛠 Tech Stack
- **Python** (Pandas, NumPy)  
- **SQLite** (with SQLAlchemy for queries)  
- **Matplotlib & Seaborn** for visualizations  
- **Jupyter Notebooks** for analysis  

---

## 📂 Project Structure
- **data/** – raw, staging, and cleaned CSVs  
- **src/** – ETL scripts (`extract.py`, `transform.py`, `load.py`)  
- **notebooks/** – analysis notebook (`analytics.ipynb`)  
- **reports/** – generated CSVs (monthly sales, top products, etc.)  
- **ecommerce.db** – SQLite database created by `load.py`  
- **requirements.txt** – Python dependencies  

---

## ▶️ How to Run
1. Clone the repository  
   ```bash
   git clone https://github.com/Praneeth100-Hat/ecommerce-analytics-pipeline.git
   cd ecommerce-analytics-pipeline
