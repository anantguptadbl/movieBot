# Imports
import os,json
from flask import Flask
from flask import Flask,render_template,request
import numpy as np
import sys,site

# Add other Libraries
from elasticsearch import Elasticsearch

# Start the Elastic Search conncetion
es = Elasticsearch([{'host': '172.16.139.218', 'port': 9200}])

# Uncomment for AWS
site.addsitedir('/home/ubuntu/.local/lib/python2.7/site-packages')
sys.path.insert(0, "/var/www/html/flaskapp")


# Initial level flask configuration
print "the file path is " + os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.dirname(os.path.abspath(__file__)) + '/static'
print "The template dir is " + template_dir
app = Flask(__name__,static_folder=template_dir,template_folder=template_dir)

# Read the BreakOut Model
#breakOutModel = load_model('breakOut_model')

#app = Flask(__name__)

#@app.route('/')
#def hello_world():
#  return 'Hello from Flask!'

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/getMovies', methods=["GET","POST"])
def getMovieSearchResults():
    print(request)
    searchText=request.args.get('searchString')
    results=es.search(index="movies", body={"query": {"match": {'Title':searchText}}})
    movieNames=[x['_source']['Title'] for x in results['hits']['hits']]
    return(json.dumps({"searchResults":movieNames}))

@app.route('/getSummarizedResults', methods=["GET","POST"])
def getSummarizedResults():
    print(request)
    searchString=request.args.get('searchString')
    linksData=summarizer.getLinksForSearchString(searchString)
    fullData=summarizer.getDataFromLinks(linksData[0])
    redundantData=summarizer.getDataFromLinks(linksData[1])
    return(json.dumps({"text":fullData,"impNouns":potentialWords,"placeDict":placeDict}))

if __name__ == '__main__':
    app.run(host='172.16.139.218',port=5000,debug=False)

