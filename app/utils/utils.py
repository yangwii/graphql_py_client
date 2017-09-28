# -*- coding: utf-8 -*-

import json

from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport


def send(host, port, data):
    client = Client(
        retries=3,
        transport=RequestsHTTPTransport(url=host + ':' + port)
    )
    query = gql(data)
    response = client.execute(query)
    return json.dumps(response)
