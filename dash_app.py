from dash import Dash, html, dcc, Input, Output, State
from Data.data import load_data
from Model.model import load_trained_model
from Model.recommendation import user_recommendation, match_discount_product
import plotly.graph_objs as go
import pandas as pd

# Load and start the app
df = load_data('amazon.csv')
tokenizer, model = load_trained_model()
app = Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1('Amazon Product Recommendation System'),

    html.Div([
        # Categories
        html.Div([
            html.H3('Categories:'),
            html.Div(id='categories')
        ], style={'width': '20%', 'display': 'inline-block', 'vertical-align': 'top'}),

        # Main content
        html.Div([
            # Recommendations
            html.Div(id='recommendations'),

            # Search and Discount section
            html.Div([
                html.Div([
                    html.H3('Search for Discounts🔖 '),
                    dcc.Input(id='search-input', type='text', placeholder='Enter a keyword...'),
                    html.Button('Search', id='search-button', n_clicks=0)
                ], style={'textAlign': 'center', 'margin': '20px 0'}),

                html.Div([
                    html.Div(id='discount-info'),
                    dcc.Graph(id='discount-plot')
                ], id='discount-section')
            ])
        ], style={'width': '75%', 'display': 'inline-block'})
    ])
])

# Callback: Update categories
@app.callback(
    Output('categories', 'children'),
    Input('search-button', 'n_clicks')
)
def update_categories(n_clicks):
    main_categories = df['main_category'].unique()
    categories_html = []
    for main_category in main_categories:
        subcategories = df[df['main_category'] == main_category]['sub_category'].unique()
        categories_html.append(
            html.Details([
                html.Summary(main_category),  # Main category
                html.Ul([html.Li(sub) for sub in subcategories])  # Subcategory list
            ])
        )
    return categories_html

# recommendations
@app.callback(
    Output('recommendations', 'children'),
    Input('search-button', 'n_clicks')
)
def update_recommendations(n_clicks):
    top_products = user_recommendation(df)
    recommendations = html.Div([
        html.H3('Top Recommended Products🎉:'),
        html.Ul([html.Li(f'{row["product_name"]} - Rating: {row["rating"]:.1f}') for _, row in top_products.iterrows()])
    ])
    return recommendations

# discount information and graph
@app.callback(
    [Output('discount-info', 'children'),
     Output('discount-plot', 'figure'),
     Output('discount-section', 'style')],  # Show/Hide discount section
    [Input('search-button', 'n_clicks')],
    [State('search-input', 'value')]
)
def update_discount(n_clicks, query):
    if query:
        matched_product = match_discount_product(query, tokenizer, model, df)
        if matched_product is not None:
            image = matched_product.get('img_link', 'https://via.placeholder.com/150')
            discount_info = html.Div([
                html.H3(f'Matched Discounted Product: {matched_product["product_name"]}'),
                html.Img(
                    src=image,
                    className="product-image"),
                html.P(f'Discount: {matched_product["discount_percentage"]}%'),
                html.P(f'Price: {matched_product["discounted_price"]}'),
                html.A(
                    "🔘Buy Now",
                    href=matched_product['product_link'],
                    target='_blank',
                    className="buy-now-button"
                )
            ])
            # Line graph for price drop
            figure = go.Figure()
            figure.add_trace(go.Scatter(
                x=['Original Price', 'Discounted Price'],
                y=[matched_product['actual_price'], matched_product['discounted_price']],
                mode='lines+markers',
                name='Price Drop',
                marker=dict(color='orange'),
                line=dict(color='orange')
            ))
            figure.update_layout(
                title=f'Price Drop for {matched_product['sub_category']}',
                xaxis_title='Price Type',
                yaxis_title='Price (₹)',
                template='seaborn',
                yaxis=dict(autorange='reversed')
            )

            # Show the discount section
            return discount_info, figure, {'display': 'flex', 'flex-direction': 'row'}

    # If no match, hide discount section and reset outputs
    return 'Enter a keyword to search for discounted products!', go.Figure(), {'display': 'none'}

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)


