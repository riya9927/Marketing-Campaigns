# 📊 Marketing Data Analysis

## 📌 Project Overview
This project aims to analyze marketing data to uncover insights related to customer income, spending habits, and demographic factors. The dataset is processed, cleaned, and visualized using Python libraries such as Pandas, Seaborn, and Matplotlib.

## 🚀 Features
- **Data Cleaning & Preprocessing:**
  - Converted `Income` column to numeric format by removing `$` and `,`.
  - Handled missing values in `Income` by grouping based on `Education` & `Marital_Status`.
  - Converted `Dt_Customer` to datetime format.
  - Created new features like `Total_Children`, `Age`, and `Total_Spending`.
- **Exploratory Data Analysis (EDA):**
  - Boxplots of key numeric features (`Income`, `Age`, `Total_Spending`).
  - Histograms to visualize feature distributions.
- **Visualization:**
  - Used `Seaborn` and `Matplotlib` to generate insightful graphs.

## 📂 Dataset
The dataset used in this analysis is **marketing_data.csv**, which contains:
- Customer demographic details (Age, Education, Marital Status, etc.).
- Spending behavior (Expenditures on Wines, Meat, Fish, etc.).
- Customer acquisition details (`Dt_Customer`).

## 🛠️ Tech Stack
- **Programming Language:** Python 🐍
- **Libraries Used:**
  - Pandas 📊
  - NumPy 🔢
  - Matplotlib 📉
  - Seaborn 🎨

## 📜 Installation
To set up the project locally, follow these steps:

1. **Clone the repository**
   ```sh
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

3. **Run the analysis**
   ```sh
   python analysis.py
   ```

## 📈 Usage
- Run `analysis.py` to perform data preprocessing and visualization.
- Modify `marketing_data.csv` to analyze new datasets.

## 📌 To-Do
- [ ] Implement advanced visualizations 📊
- [ ] Perform feature engineering for predictive modeling 🔍
- [ ] Train ML models for customer segmentation 🤖

## 🤝 Contributing
Contributions are welcome! Feel free to fork the repo and submit a pull request. 🚀

## 📄 License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---
🔗 **Let's Connect:** [LinkedIn](https://www.linkedin.com/in/your-profile) | [GitHub](https://github.com/your-username)

