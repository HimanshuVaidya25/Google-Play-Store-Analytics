# 📊 Google Play Store Data Analytics Dashboard

## 📌 Project Overview

This project is an interactive data analytics dashboard built using **Python, Pandas, Matplotlib, Plotly, and Streamlit**.  
The dashboard analyzes the Google Play Store dataset and implements six advanced analytical tasks with business logic filters and time-based visualization control.

The dashboard displays different visualizations based on specific filtering conditions and predefined time windows (IST).

---

## 🗂 Dataset Used

- Dataset: Google Play Store Dataset  
- File: `playstore_data.csv`
- Key Features Used:
  - App
  - Category
  - Rating
  - Reviews
  - Size
  - Installs
  - Type
  - Price
  - Content Rating
  - Last Updated
  - Android Version

---

## 🛠 Tools & Technologies

- Python 3.10
- Pandas
- NumPy
- Matplotlib
- Plotly
- Streamlit
- Pytz (Timezone handling)
- Git & GitHub

---

## 📈 Implemented Tasks

### 🔹 Task 1 – Grouped Bar Chart
- Compared average rating and total reviews
- Top 10 categories by installs
- Filters:
  - Avg rating ≥ 4.0
  - Size ≥ 10 MB
  - Last Updated in January
- Visible only between **3 PM – 5 PM IST**

---

### 🔹 Task 2 – Dual Axis Chart
- Compared average installs and revenue (Free vs Paid)
- Filters:
  - Installs > 10,000
  - Revenue > $10,000
  - Android version > 4.0
  - Size > 15 MB
  - Content Rating = Everyone
  - App name ≤ 30 characters
- Visible only between **1 PM – 2 PM IST**

---

### 🔹 Task 3 – Interactive Choropleth Map
- Global installs visualization (Plotly)
- Top 5 categories only
- Categories not starting with A, C, G, S
- Highlighted installs > 1 Million
- Visible only between **6 PM – 8 PM IST**

---

### 🔹 Task 4 – Stacked Area Chart
- Cumulative installs over time
- Filters:
  - Rating ≥ 4.2
  - No numbers in app name
  - Category starts with T or P
  - Reviews > 1000
  - Size between 20MB – 80MB
- Visible only between **4 PM – 6 PM IST**

---

### 🔹 Task 5 – Bubble Chart
- Relationship between Size and Rating
- Bubble size represents installs
- Filters:
  - Rating > 3.5
  - Reviews > 500
  - Installs > 50k
  - App name not containing 'S'
- Game category highlighted in Pink
- Visible only between **5 PM – 7 PM IST**

---

### 🔹 Task 6 – Time Series Line Chart
- Trend of installs over time
- Category starting with E, C, B
- Reviews > 500
- App name not starting with x, y, z
- Growth period highlighted
- Visible only between **6 PM – 9 PM IST**

---

## ⏰ Time-Based Visualization Control

Each task is displayed only within its assigned IST time window.  
Outside the allowed time range, a warning message is shown instead of the graph.

This ensures compliance with internship requirements.

---

## 🚀 How to Run the Project

### 1️⃣ Clone Repository
```bash
git clone https://github.com/YOUR_USERNAME/Google-Play-Store-Analytics.git
cd Google-Play-Store-Analytics

