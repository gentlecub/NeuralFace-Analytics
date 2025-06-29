# 🚗 CarSales Analytics: Intelligent Vehicle Sales Insights

_Understand and Visualize Car Sales Trends with Python & Data Science Tools_

**CarSales Analytics** is a Python-powered desktop application designed to explore, analyze, and visualize car sales data from the years **2022 and 2023**. Built with **Pandas** and **Matplotlib**, this project delivers meaningful insights into sales performance, dealership rankings, best-selling car models, and more—making it an essential tool for data-driven decision-making in the automotive industry.

---

## ✨ Key Features

- 📈 **Daily Sales Analysis**  
  Identify day-by-day sales trends and seasonal behavior patterns.

- 🏆 **Top 5 Dealerships by Sales**  
  Discover which dealerships had the highest number of car sales.

- 🚘 **Top 10 Car Companies**  
  Highlight the manufacturers with the largest market share.

- 📊 **Monthly Car Sales Summary**  
  Visualize how car sales evolve month-by-month across two years.

- 🌟 **Top 10 Best-Selling Models**  
  Identify the most popular vehicles based on sales volume.

- 📉 **Company Growth Over Time**  
  Analyze how each manufacturer's sales evolved over time.

- 🔒 **Role-Based Access**  
  Admins can manage users, while standard users access data and reports.

---

## 🧠 How It Works

The application follows these key steps:

1. 🔐 **Login System**  
   Users authenticate through a login screen. Role-based access determines available features.

2. 📂 **Data Import**  
   Car sales data is loaded from CSV files and stored in a **MySQL** database (`MySql/` folder).

3. 🧹 **Data Cleaning & Processing**  
   Leveraging **Pandas**, the data is cleaned, validated, and transformed for analysis.

4. 📊 **Data Visualization**  
   Charts and graphs are generated with **Matplotlib** to facilitate insight discovery.

5. 🧾 **User Interface**  
   A simple, menu-driven console UI allows users to explore data visually or in table format.

---

## 🛠️ Technologies Used

- **Programming Language:** Python 3  
- **Data Handling:** Pandas  
- **Visualization:** Matplotlib (Pyplot)  
- **Database:** MySQL  
- **Authentication:** Role-based login system  
- **Execution:** `main.py` is the entry point  

---

## 📁 Project Structure
```
📁 CarSalesApp/
├── MySql/ # Database schema and SQL scripts
├── data/ # Raw CSV data files
├── modules/ # Application logic (login, analysis, UI)
├── charts/ # Chart generation utilities
├── main.py # Entry point of the application
└── README.md
```
---


---

## 🧭 How to Run

### 📦 1. Clone the repository

```bash
git clone https://github.com/your-username/CarSalesApp.git
cd CarSalesApp

---

💽 2. Import MySQL Schema
Use your preferred MySQL client (like phpMyAdmin or MySQL Workbench) to import the SQL schema from the MySql/ folder.

----

🚀 3. Run the application
bash
Copiar
Editar
python main.py

---

🔑 Login
Use a valid username and password from the MySQL database. Admin and user roles determine feature access.

| Role  | Features                                                           |
| ----- | ------------------------------------------------------------------ |
| User  | View charts, analytics, and tabular sales reports                  |
| Admin | Full access: manage users, edit/delete data, and view all insights |

---
