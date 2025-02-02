from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

# Load data from CSV
def load_data():
    if not os.path.exists('search_analytics.csv'):
        raise FileNotFoundError("The file 'search_analytics.csv' does not exist. Please run main.py to generate it.")
    
    df = pd.read_csv('search_analytics.csv')
    return df

# Home route
@app.route('/')
def dashboard():
    try:
        # Load data
        data = load_data()
        
        # Convert DataFrame to a list of dictionaries for rendering in the template
        records = data.to_dict(orient='records')
        
        # Calculate total clicks and impressions
        total_clicks = data['Clicks'].sum()
        total_impressions = data['Impressions'].sum()
        
        # Calculate average CTR and position
        average_ctr = (total_clicks / total_impressions) * 100 if total_impressions > 0 else 0
        average_position = data['Position'].mean()
        
        # Prepare data for charts
        chart_data = {
            'queries': data['Query'].tolist(),
            'clicks': data['Clicks'].tolist(),
            'impressions': data['Impressions'].tolist(),
            'ctr': data['CTR'].tolist(),
            'position': data['Position'].tolist(),
            'total_clicks': total_clicks,
            'total_impressions': total_impressions,
            'average_ctr': average_ctr,
            'average_position': average_position
        }
        
        # Render the dashboard template
        return render_template('dashboard.html', records=records, chart_data=chart_data)
    except FileNotFoundError as e:
        return str(e), 404

if __name__ == '__main__':
    app.run(debug=True)