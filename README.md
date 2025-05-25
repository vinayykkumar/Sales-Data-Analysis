📊 SaaS and Subscription-Based Data Analysis
Overview
This project focuses on analyzing data from a SaaS (Software as a Service) and subscription-based business model. It aims to extract actionable insights regarding customer behavior, revenue trends, churn patterns, and overall business performance through advanced analytics, machine learning (ML), and deep learning (DL) techniques.

📁 Project Structure
kotlin
Copy
Edit
├── data/
│   └── saas_subscriptions.csv
├── notebooks/
│   └── eda_analysis.ipynb
│   └── churn_prediction_model.ipynb
├── app/
│   └── streamlit_app.py
├── models/
│   └── churn_model.pkl
│   └── dl_model.h5
├── README.md
└── requirements.txt
🔍 Objectives
Perform in-depth EDA to understand customer and subscription behavior.

Track key SaaS KPIs such as MRR, ARR, Churn Rate, LTV, and CAC.

Build predictive models to identify potential churn using:

XGBoost

Deep Learning (Neural Networks)

Deploy an interactive analytics dashboard using Streamlit.

🔧 Technologies Used
Python

Pandas, NumPy – Data analysis and manipulation

Matplotlib, Seaborn, Plotly – Visualization

Scikit-learn, XGBoost – Machine learning

TensorFlow/Keras – Deep learning model development

Streamlit – Web app interface

🔬 Features
📈 SaaS Dashboard to track revenue trends and user metrics

🔍 Exploratory data analysis (EDA) with interactive plots

🤖 Churn prediction using:

Logistic Regression

XGBoost

Deep Learning

📊 Cohort and retention analysis

🖥️ Streamlit dashboard for interactive exploration

🚀 How to Run
Clone the Repository

bash
Copy
Edit
git clone https://github.com/yourusername/saas-subscription-analytics.git
cd saas-subscription-analytics
Install Dependencies

bash
Copy
Edit
pip install -r requirements.txt
Launch the App

bash
Copy
Edit
streamlit run app/streamlit_app.py
📌 Key Insights
Churn rate is higher for monthly subscribers vs annual.

Customers with low product engagement are more likely to cancel.

XGBoost and deep learning models significantly improved churn prediction accuracy (~88–90%).

👨‍💻 Team
This project was completed by a team of 4 members.

Roles included:

Data Cleaning & Preprocessing

Feature Engineering

Machine Learning & Deep Learning Modeling

Streamlit Dashboard Development

🔮 Future Enhancements
Integrate real-time billing APIs (e.g., Stripe, Chargebee).

Implement model retraining and monitoring pipeline.

Deploy with cloud platforms like AWS or GCP for scalability.

📄 License
This project is for academic and educational use only.
