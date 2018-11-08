#!/usr/bin/env python3

import json
import logging
from urllib.parse import urljoin
import click
import requests


logging.basicConfig(level=logging.DEBUG)

class HTTPBearerAuthentication(requests.auth.AuthBase):
    def __init__(self, token):
        self._token = token

    def __call__(self, r):
        r.headers['Authorization'] = 'Bearer {token}'.format(token=self._token)
        return r

@click.command()
@click.option('--api-key', help='API key of the target grafana', required=True, prompt=True)
@click.option('--grafana-url', help='base url of the target grafana', required=True)
def backup(api_key, grafana_url):
    session = requests.Session()
    session.auth = HTTPBearerAuthentication(api_key)


    response = session.get(urljoin(grafana_url, '/api/search'))

    if not response.ok:
        click.secho("Request failed: {}".format(response), fg='red')
        click.echo('Response: {}'.format(response.json()))
        return 1

    data = response.json()
    dashboards = [ entry for entry in data if entry['type'] == 'dash-db' ]

    for dashboard in dashboards:
        dashboard_data = session.get(urljoin(grafana_url, '/api/dashboards/{uri}'.format(uri=dashboard['uri']))).json()
        filename = '{slug}.json'.format(slug=dashboard_data['meta']['slug'])
        with open(filename, 'w') as fh:
            json.dump(dashboard_data, fh, indent=4, sort_keys=True)

if __name__ == "__main__":
    backup()
