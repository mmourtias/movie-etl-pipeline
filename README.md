# 🎬 Movie ETL Pipeline (TMDB API)

An end-to-end **ETL (Extract – Transform – Load)** data engineering project using the **TMDB API**, **Python**, and **SQLite**.

The pipeline collects movie data from an external API, cleans and normalizes it, loads it into a relational database, and performs analytical queries whose results are also **visualized into charts** for better insight.

---

## 📌 Project Overview

This project simulates a real-world data engineering workflow with clear separation of responsibilities across ETL stages.

It demonstrates how to:
- Extract data from a REST API
- Transform raw JSON responses into a clean, structured format
- Load processed data into a relational database
- Analyze stored data using SQL and Python
- Visualize analytical query results into meaningful charts

---

## 🧱 Architecture

TMDB API  
↓  
collect.py → data/raw/  
↓  
transform.py → data/processed/  
↓  
load.py → SQLite (movies.db)  
↓  
analysis.py → SQL-based insights  
↓  
visualize.py → charts & reports (PNG)

---

## 🛠️ Tech Stack

- Python 3
- Requests (API communication)
- SQLite (local relational database)
- SQL (data analysis)
- python-dotenv (environment variables)
- Logging (pipeline observability)
- Matplotlib (data visualization)
- VS Code + SQLite Explorer (database inspection)

---

## 📂 Project Structure

```text

movie_etl_api/
├── etl/
│   ├── collect.py        # Extract data from TMDB API
│   ├── transform.py      # Clean & normalize raw data
│   ├── load.py           # Load data into SQLite
│   ├── analysis.py       # Query & analyze stored data
│   └── visualize.py      # Visualize SQL query results
│
├── data/
│   ├── raw/              # Raw API responses (JSON)
│   └── processed/        # Cleaned movie data
│
├── database/
│   ├── movies.db         # SQLite database
│   ├── init.sql          # Database schema
│   └── queries.sql       # Analytical SQL queries
│
├── reports/
│   ├── top_popular_movies.png
│   └── top_rated_movies.png
│
├── requirements.txt
├── .env                  # API credentials (not committed)
└── README.md

```
---

## ⚙️ Setup Instructions

1. Clone the repository  
2. Create and activate a virtual environment  
3. Install dependencies using: pip install -r requirements.txt  
4. Create a .env file in the project root containing: TMDB_API_KEY=your_api_key_here  

---

## ▶️ Running the Pipeline

Run each step in order from the project root using the following commands:

python etl/collect.py  
python etl/transform.py  
python etl/load.py  
python etl/analysis.py  
python etl/visualize.py  

If all steps complete successfully, the ETL pipeline has executed end-to-end and produced both data and visual reports.

---

## 🔍 Data Validation

- Raw data is stored in data/raw/
- Processed data is stored in data/processed/
- Loaded data is stored in database/movies.db
- Tables and records can be inspected via SQLite Explorer
- SQL analysis queries are defined in database/queries.sql
- Visualization outputs are saved in the reports/ directory

---

## 📊 Example Analyses & Visualizations

- Total number of movies stored
- Top 10 most popular movies (visualized as bar chart)
- Top-rated movies with a minimum vote threshold (visualized as bar chart)

Each visualization is generated directly from the corresponding SQL query results.

---

## ✅ Project Status

The ETL pipeline is complete and fully functional.

Potential future improvements include:
- API pagination and incremental loads
- Workflow orchestration (Airflow / Prefect)
- Data quality checks
- Interactive dashboards
- Containerization with Docker

---

## 🧠 Key Takeaway

This project focuses on understanding **data flow and structure**, not memorization.  
Each ETL and analysis step is isolated, testable, and verifiable, closely reflecting real-world data engineering and analytics workflows.

---

## 👤 Author

Built as a hands-on data engineering learning project using real-world tools and workflows.
