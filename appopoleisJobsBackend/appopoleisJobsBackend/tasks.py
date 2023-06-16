import http.client
from celery import shared_task

@shared_task
def fetch_jobs_from_api():
    host = 'jooble.org'
    key = 'd460d215-7760-414a-a190-1fce90b3595a'
    keywords = ['it', 'sales', 'marketing']  # List of keywords
    locations = ['india']  # List of locations

    for keyword in keywords:
        for location in locations:
            connection = http.client.HTTPSConnection(host)
            headers = {"Content-type": "application/json"}
            body = f'{{ "keywords": "{keyword}", "location": "{location}" }}'
            connection.request('POST', '/api/' + key, body, headers)
            response = connection.getresponse()
            data = response.read()
            # Process the retrieved jobs for each keyword and location
            # and update your Django models with the relevant job information
            # ...
