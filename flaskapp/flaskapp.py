# Imports
import os,json
from flask import Flask
from flask import Flask,render_template,request
import numpy as np
import keras
from sklearn import preprocessing
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout
from keras.models import load_model
import sys,site

# Add other Libraries

# Uncomment for AWS
site.addsitedir('/home/ubuntu/.local/lib/python2.7/site-packages')
sys.path.insert(0, "/var/www/html/flaskapp")
#from mockup.app import app as application 
keras.backend.clear_session()


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

@app.route('/getDataBreakOut', methods=["GET","POST"])
def getXYDataBreakOut():
	print(request.args.get('paddleData'));
	print(request.args.get('BallData'));
	
	

@app.route('/getSummarizedResults', methods=["GET","POST"])
def getSummarizedResults():
	print(request)
	searchString=request.args.get('searchString')
	linksData=summarizer.getLinksForSearchString(searchString)
	fullData=summarizer.getDataFromLinks(linksData[0])
	redundantData=summarizer.getDataFromLinks(linksData[1])
	#fullData=summarizer.getDataFromLinks(linksData[0])
	#print("the fullData is {}".format(fullData))
	normalNouns=summarizer.getAllNouns(fullData)
	redundantNouns=summarizer.getAllNouns(redundantData)
	potentialWords=[x for x in normalNouns if x not in redundantNouns]
	placeDict=dict((x,summarizer.getosmDetails(x)) for x in potentialWords)
	#print("impNouns are {}".format(impNouns))
	return(json.dumps({"text":fullData,"impNouns":potentialWords,"placeDict":placeDict}))

if __name__ == '__main__':
  app.run(host='172.16.139.218',port=5000,debug=False)

