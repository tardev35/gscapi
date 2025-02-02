import csv


def save_to_csv(data, filename='search_analytics.csv'):
    """
    Save search analytics data to a CSV file.
    """
    rows = data.get('rows', [])
    if not rows:
        print("No data found.")
        return
    
    # Define CSV headers
    headers = ['Query', 'Page', 'Country', 'Device', 'Clicks', 'Impressions', 'CTR', 'Position']
    
    # Write data to CSV
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        for row in rows:
            keys = row.get('keys', [])
            writer.writerow(
                keys + [row.get('clicks'), 
                row.get('impressions'), 
                row.get('ctr'), 
                row.get('position')]
            )
            
    print(f"Data saved to {filename}")