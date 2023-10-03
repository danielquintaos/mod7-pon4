
# Mall Customer Spending Score Predictor

This project provides a simple interface for predicting a mall customer's spending score based on their gender, age, and annual income. The prediction is powered by a machine learning model trained on a dataset of mall customers.

## Features

- **Simple User Interface**: Using Streamlit, users can easily input their details and get a predicted spending score.
- **Trained Model**: The backend uses a machine learning model trained on a dataset of mall customers, ensuring accurate predictions.

## Dataset Columns

The dataset consists of the following columns:

- `CustomerID`: Unique ID assigned to each customer.
- `Gender`: Gender of the customer.
- `Age`: Age of the customer.
- `Annual Income (k$)`: Annual income of the customer in thousands of dollars.
- `Spending Score (1-100)`: Score assigned by the mall based on customer behavior and spending nature.

The project focuses on predicting the `Spending Score (1-100)` based on the other features.

## Installation & Setup

1. **Clone the Repository**:
   ```
   git clone https://github.com/danielquintaos/mod7-pon4.git
   cd mall-customer-predictor
   ```

2. **Install Required Libraries**:
   ```
   pip install streamlit pandas scikit-learn
   ```

3. **Run the Streamlit App**:
   ```
   streamlit run predictor_app.py
   ```

4. Access the app in your browser via the provided link, typically `http://localhost:8501`.

## Usage

1. Open the Streamlit app in your browser.
2. Select your gender from the dropdown.
3. Input your age and annual income.
4. Click on "Predict Spending Score" to get the predicted score.

## Future Enhancements

- Improve prediction accuracy by incorporating more features.
- Add capability to handle batch predictions.
- Implement data visualization to provide insights on spending patterns.
