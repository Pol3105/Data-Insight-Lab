# Data-Insight-Lab 📊

> **Interactive Data Analytics Dashboard built with Python and Streamlit.** Features exploratory data analysis (EDA), dynamic visualizations, and KPI tracking using Pandas.

---

## 🚀 About This Project (My Data Journey)

Welcome to my portfolio! **This is my very first project in the field of Data Analytics.** It represents the starting point of my journey into data science. My goal was to move beyond static spreadsheets and build a **live, interactive tool** that consumes real-time financial data. While this is just the beginning, it demonstrates my ability to integrate APIs, handle data frames, and create user-friendly interfaces.

**Stay tuned:** I will be constantly adding more complex projects to this repository as I master SQL, Machine Learning, and deeper statistical analysis.

---

## 🛠️ How I Built It (Step-by-Step)

This project was built using an iterative process to ensure robustness and usability:

### 1. Environment Setup
I set up a cloud-based development environment using **GitHub Codespaces**, ensuring a clean and reproducible workspace with Python.

### 2. Data Extraction (ETL)
Instead of using static CSV files, I implemented a connection to the **Yahoo Finance API** (`yfinance`). This allows the dashboard to pull stock market data in real-time, making the tool useful for current market analysis.

### 3. Data Processing with Pandas
I used `pandas` to structure the raw JSON data into DataFrames, handling dates and cleaning missing values to prepare the dataset for visualization.

### 4. Interactive Visualization
I chose **Plotly** over static libraries (like Matplotlib) to create interactive Candlestick charts. This allows users to zoom, pan, and hover over specific data points to see open/close prices.

### 5. User Interface (UI/UX)
Using **Streamlit**, I built a sidebar for user inputs. I implemented:
* **Dropdown menus** for quick selection of popular assets (Apple, Bitcoin, etc.).
* **Input validation** and error handling (Try/Except blocks) to prevent the app from crashing if an invalid ticker is entered.

---

## 💻 Tech Stack

* **Language:** Python 3.10+
* **Web Framework:** Streamlit
* **Data Manipulation:** Pandas
* **Data Visualization:** Plotly Graph Objects
* **API:** yfinance

---

## ⚙️ How to Run Locally

If you want to clone this repository and run the dashboard on your machine:

1.  **Clone the repo:**
    ```bash
    git clone [https://github.com/TU_USUARIO/Data-Insight-Lab.git](https://github.com/TU_USUARIO/Data-Insight-Lab.git)
    cd Data-Insight-Lab
    ```

2.  **Install dependencies:**
    ```bash
    pip install streamlit pandas yfinance plotly
    ```

3.  **Run the app:**
    ```bash
    streamlit run app.py
    ```

---

*Created with ❤️ by Pablo Rejon Camacho*