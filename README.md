# Amazon Recommendation System

## Overview
The **Amazon Recommendation System** is a web-based application that delivers personalized product recommendations based on user input and product data. It integrates product categories, discounts, and pricing trends to enhance the shopping experience. The system is built using **Dash**, **Plotly**, and other Python libraries to provide an interactive and user-friendly interface.

---

## Features
- **Category-Based Navigation**: Browse products by category and subcategory.
- **Top Recommendations**: Displays the most relevant products based on ratings and popularity.
- **Discount Search**: Find discounted products and visualize pricing trends.
- **Interactive Charts**: Compare prices and discount trends with graphical insights.
- **Responsive Design**: Optimized for both desktop and mobile devices.

---

## Setup Instructions

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- pip (Python package manager)
- Git

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/Zihui-Z/Amazon_Recommendation_System.git
    cd Amazon_Recommendation_System
    ```

2. Set up a virtual environment:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # macOS/Linux
    .venv\Scripts\activate     # Windows
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    python dash_app.py
    ```

5. Open your browser and navigate to `http://127.0.0.1:8050`.

---

## Usage
- Use the **categories panel** to explore products by categories and subcategories.
- Enter a keyword in the **search bar** to find discounted products.
- View interactive visualizations for detailed product insights.

---

## Dataset
The project uses the **Amazon Sales Dataset** from Kaggle, which includes:
- Product names
- Categories
- Ratings
- Discount percentages
- Prices (original and discounted)

### Accessing the Dataset
1. **Manual Download**: Visit the [Kaggle dataset page](https://www.kaggle.com/datasets/karkavelrajaj/amazon-sales-dataset/data) and download the dataset as a ZIP file.
2. **Using Kaggle API**:
    ```python
    import kagglehub

    # Download the dataset
    path = kagglehub.dataset_download("karkavelrajaj/amazon-sales-dataset")
    print("Path to dataset files:", path)
    ```

---

## Model
This system uses the **all-MiniLM-L6-v2** model from [Hugging Face](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2). It maps product names and queries to a **384-dimensional dense vector space** for tasks like clustering, semantic search, and recommendation.

### Key Features:
- **Efficient Embedding Generation**: Converts product names and user queries into meaningful embeddings.
- **Lightweight and Fast**: Optimized for speed and accuracy with only **22.7M parameters**.
- **Cosine Similarity**: Computes the relevance between user queries and product names.

### System Optimizations:
- **Query Matching**: Matches user queries to the most relevant discounted products.
- **Diverse Recommendations**: Provides balanced recommendations across categories based on ratings and popularity.

---

## Libraries and Frameworks
- **Hugging Face Transformers**: NLP embeddings for product matching.
- **NumPy**: Efficient numerical operations for embeddings.
- **scikit-learn**: Cosine similarity for matching embeddings.
- **Dash**: Interactive web application framework.
- **Plotly**: For creating engaging visualizations.

---

## License
This project is licensed under the **AGPL-3.0 License**. See the [LICENSE](./LICENSE) file for details.

---

## Author
Developed by **Zihui Zhuang**  
For queries or issues, contact [Zihui Zhuang](mailto:zz3256@columbia.edu).


