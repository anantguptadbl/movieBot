#/usr/bin/python

# SHELL COMMANDS LIST
#curl -X GET 'http://172.16.139.218:9200'

import requests
res = requests.get('http://172.16.139.218:9200')
print(res.content)

from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': '172.16.139.218', 'port': 9200}])

# Add Data
#es.index(index='movies', doc_type='movie', id=0, body={'name':'lcentral1','release':'2019-01-02'})

# Query Data
print(es.get(index='movies', doc_type='movie', id=0))

# Search Data
print(es.search(index="movies", body={"query": {"match": {'name':'lcentral1'}}}))
