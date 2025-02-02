from auth.google_auth import authenticate_google
from api.search_console import fetch_search_analytics
from utils.file_utils import save_to_csv
import json

def main():
    # Authenticate
    creds = authenticate_google()

    site_url = 'sc-domain:devhub.in.th'
    
    # Define date range (format: 'YYYY-MM-DD')
    start_date = '2024-01-01'
    end_date = '2024-12-31'
    
    # Fetch data
    data = fetch_search_analytics(creds, site_url, start_date, end_date)
    
    # Print and save the results
    if data:
        print(json.dumps(data, indent=2))
        save_to_csv(data)
    else:
        print("No data returned from the API.")

if __name__ == '__main__':
    main()