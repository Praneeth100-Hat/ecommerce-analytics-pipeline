<h1 align="center">🛒 Ecommerce Analytics Pipeline</h1>

<p align="center">
  <a href="https://github.com/Praneeth100-Hat/ecommerce-analytics-pipeline/stargazers">
    <img alt="Stars" src="https://img.shields.io/github/stars/Praneeth100-Hat/ecommerce-analytics-pipeline?style=flat&color=ffcc00" />
  </a>
  <a href="https://github.com/Praneeth100-Hat/ecommerce-analytics-pipeline/issues">
    <img alt="Issues" src="https://img.shields.io/github/issues/Praneeth100-Hat/ecommerce-analytics-pipeline?style=flat" />
  </a>
  <img alt="Python" src="https://img.shields.io/badge/Python-3.10%2B-blue" />
  <img alt="License" src="https://img.shields.io/badge/License-MIT-green" />
</p>

> **Quickstart**
> ```bash
> git clone https://github.com/Praneeth100-Hat/ecommerce-analytics-pipeline.git
> cd ecommerce-analytics-pipeline
> python -m venv venv
> # Windows
> venv\Scripts\activate
> # macOS/Linux: source venv/bin/activate
> pip install -r requirements.txt
> python src/extract.py && python src/transform.py && python src/load.py
> ```

## 📊 Results (click to view)
- **Monthly Sales** → [`reports/monthly_sales.csv`](reports/monthly_sales.csv)
- **Top Products** → [`reports/top_products.csv`](reports/top_products.csv)
- **Revenue by Country** → [`reports/country_revenue.csv`](reports/country_revenue.csv)
- **Top Customers** → [`reports/top_customers.csv`](reports/top_customers.csv)


import os
os.makedirs("../reports/figures", exist_ok=True)
plt.savefig("../reports/figures/monthly_sales.png", bbox_inches="tight", dpi=160)


## 📈 Visuals
<p align="center">
  <img src="reports/figures/monthly_sales.png" width="720" alt="Monthly Sales Trend"/>
</p>
## 📂 Project Structure
ecommerce-analytics-pipeline/
├─ data/
├─ notebooks/
├─ reports/
│  ├─ monthly_sales.csv
│  ├─ top_products.csv
│  ├─ country_revenue.csv
│  └─ top_customers.csv
├─ src/
│  ├─ extract.py
│  ├─ transform.py
│  └─ load.py
├─ ecommerce.db
├─ requirements.txt
└─ README.md
**Jump to code:**  
[`src/extract.py`](src/extract.py) • [`src/transform.py`](src/transform.py) • [`src/load.py`](src/load.py) •
[`notebooks/analytics.ipynb`](notebooks/analytics.ipynb)
## 🧪 Sample SQL (SQLite)
```sql
-- Total revenue per month
SELECT strftime('%Y-%m', InvoiceDate) AS month,
       ROUND(SUM(Quantity * UnitPrice), 2) AS revenue
FROM fact_sales
GROUP BY month
ORDER BY month;

---

## 7) Add a **Roadmap** checklist (shows ambition)

```markdown
## 🗺️ Roadmap
- [x] Build ETL (extract → transform → load)
- [x] Generate top-line reports (sales, products, countries, customers)
- [ ] Add cohort analysis & retention curves
- [ ] Add dashboard (Streamlit) and host on free tier
# Python
__pycache__/
*.pyc

# Jupyter
.ipynb_checkpoints/

# Environments
venv/

# OS
.DS_Store
Thumbs.db
## 👤 Author
Praneeth Kamjula

If you found this useful, please ⭐ the repo — it helps!

