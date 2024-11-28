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

## Model
This system utilizes **Hugging Face Transformers** for embedding generation and **cosine similarity** for matching user queries to relevant products. The recommendation algorithm considers:
- **Rating weight**: A combination of product ratings and rating counts.
- **Category diversity**: Ensuring recommendations are varied and balanced.

The model is optimized for:
- Matching user queries to the most relevant discounted products.
- Selecting diverse and top-rated products from various categories.

### Libraries and Frameworks
- **Hugging Face Transformers**: NLP embeddings for product matching.
- **NumPy**: Efficient numerical operations.
- **scikit-learn**: Cosine similarity for matching embeddings.
- **Dash**: Frontend framework for an interactive UI.

---
### Features
- `product_id`: Unique ID for each product
- `product_name`: Name of the product
- `category`: Category of the product
- `discounted_price`: Discounted price of the product
- `actual_price`: Original price of the product
- `discount_percentage`: Percentage of discount offered
- `rating`: Product rating
- `rating_count`: Number of users who rated the product
- `about_product`: Description of the product

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

