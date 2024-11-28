import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from Model.model import generate_embedding
import pandas as pd

def user_recommendation(df, top_n=10):
    # rating weight
    df['rating_weight'] = df['rating'] * df['rating_count']
    unique = df.sort_values(by='rating_weight', ascending=False).drop_duplicates(subset=['product_name'])
    categories = unique['category'].unique()
    one_per_category = max(1, top_n // len(categories))

    # Select top products from each category
    recommended_products = [
        unique[unique['category'] == category].head(one_per_category)
        for category in categories
    ]
    final_recommendations = pd.concat(recommended_products).head(top_n)
    return final_recommendations[['product_name', 'rating']]

def match_discount_product(query, tokenizer, model, df):
    discounted_products = df[df['discount_percentage'] > 0].copy()
    if discounted_products.empty:
        return None

    # Generate embeddings for all discounted products
    discounted_products['embedding'] = discounted_products['product_name'].apply(
        lambda x: generate_embedding(x, tokenizer, model) if isinstance(x, str) else np.zeros(10)
    )
    query = generate_embedding(query, tokenizer, model)
    # Compute cosine similarity
    embeddings = np.vstack(discounted_products['embedding'].to_numpy())  # Ensure consistent type
    similarities = cosine_similarity([query], embeddings).flatten()
    # Find the best match
    best_match = np.argmax(similarities)
    return discounted_products.iloc[best_match]

