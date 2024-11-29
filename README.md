# Amazon_Recommendation_System

## Overview
The **Amazon Recommendation System** is a web-based application that provides personalized product recommendations based on user input and product data. It integrates product information such as categories, discounts, and pricing trends to enhance the shopping experience.

This system was built using **Dash**, **Plotly**, and other Python libraries to deliver an interactive and user-friendly interface.

---

## Features
- **Category-Based Navigation**: Browse products by category and subcategory.
- **Top Recommendations**: Displays the most relevant products based on popularity and ratings.
- **Discount Search**: Search for products with discounts and visualize price trends.
- **Interactive Charts**: Plot price comparisons and discount trends for better decision-making.
- **Responsive Design**: Optimized for both desktop and mobile screens.

---

## Setup Instructions

### Prerequisites
Ensure you have the following installed on your system:
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
    source .venv/bin/activate  # For macOS/Linux
    .venv\Scripts\activate     # For Windows
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
- Use the **categories panel** to explore products by their categories and subcategories.
- Enter a keyword in the **search bar** to find discounted products.
- View detailed product recommendations with interactive visualizations.

---

## Dataset
The project uses the **Amazon Sales Dataset** from Kaggle. This dataset includes details of 1K+ Amazon products, including their ratings, reviews, and other product-specific information.

### Usage
If you'd like to use the same dataset, you can access it in two ways:

1. **Download Manually**  
   Visit the [Kaggle dataset page](https://www.kaggle.com/datasets/karkavelrajaj/amazon-sales-dataset/data), download the dataset as a ZIP file, and extract it to your local directory.

2. **Using Kaggle API**  
   To automate the process with the Kaggle API:
   ```python
   import kagglehub
   
   # Download the dataset
   path = kagglehub.dataset_download("karkavelraja/amazon-sales-dataset")
   print("Path to dataset files:", path)

---

## Model
This system leverages the **all-MiniLM-L6-v2** model from [Hugging Face](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2), a sentence-transformer model designed for semantic similarity tasks. The model maps sentences and paragraphs to a **384-dimensional dense vector space**, making it ideal for clustering, semantic search, and matching user queries to product names.

### Key Features of the Model:
- **Efficient Embedding Generation**: Converts product names and user queries into meaningful embeddings.
- **Lightweight and Fast**: With **22.7M parameters**, the model is optimized for speed and accuracy.
- **Cosine Similarity**: Used to compute the relevance between user queries and product names.

### How the System Works:
This system utilizes **Hugging Face Transformers** for embedding generation and **cosine similarity** for matching user queries to relevant products. The recommendation algorithm is designed with the following considerations:
- **Rating Weight**: A combination of product ratings and rating counts to prioritize highly-rated and popular products.
- **Category Diversity**: Ensures recommendations are varied and balanced across different product categories.

### Optimizations:
- **Query Matching**: Matches user queries to the most relevant discounted products using embeddings and cosine similarity.
- **Diverse Recommendations**: Selects top-rated products from various categories to provide a balanced set of recommendations.

### Libraries and Frameworks:
The system is built using the following tools:
- **Hugging Face Transformers**: Provides state-of-the-art NLP embeddings for product matching.
- **NumPy**: Enables efficient numerical operations, including handling embeddings.
- **scikit-learn**: Powers cosine similarity calculations for matching embeddings.
- **Dash**: A powerful frontend framework used to create an interactive and user-friendly UI.

### Installation
To use the model, ensure the following library is installed:
```bash
pip install -U sentence-transformers
---
## Technologies Used
- **Dash**: For building the interactive web application
- **Plotly**: For creating visualizations
- **Pandas**: For data manipulation
- **scikit-learn**: For recommendation algorithms
---

## License
This project is licensed under the **AGPL-3.0 License**. See the [LICENSE](./LICENSE) file for details.

---


## Author
Developed by **Zoe Zhuang**  
For any queries or issues, please contact [Zoe Zhuang](mailto:zz3256@columbia.edu).

