#/usr/bin/python

# INSTALLATIONS
# pip install elasticsearch
# pip install elasticsearch_dsl

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
#print(es.get(index='movies', doc_type='movie', id=0))

# Search Data
#print(es.search(index="movies", body={"query": {"match": {'Title':'beanstalk'}}}))

# Read the movie Data and add it
import pandas as pd
data=pd.read_csv('/home/ubuntu/anant/projects/movie/movieBot/data/wiki_movie_plots_deduped.csv.tar.gz')

def addDataToCollection(idVal,JSONVal):
	es.index(index='movies', doc_type='movie', id=idVal, body=JSONVal)

colValues=['Title','Origin/Ethnicity','Director','Cast','Genre','Wiki Page','Plot']
for i,row in data[colValues].iterrows():
	addDataToCollection(i,row.to_json())

