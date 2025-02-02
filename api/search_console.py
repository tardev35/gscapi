from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def fetch_search_analytics(creds, site_url, start_date, end_date):
    """
    Fetch search analytics data from Google Search Console API.
    """
    try:
        service = build('searchconsole', 'v1', credentials=creds)
        request = {
            'startDate': start_date,
            'endDate': end_date,
            'dimensions': ['query', 'page', 'country', 'device'],
            'rowLimit': 20
        }
        response = service.searchanalytics().query(siteUrl=site_url, body=request).execute()
        return response
    except HttpError as error:
        print(f"An error occurred: {error}")
        print(error.content)  # Print the full error response
        return None