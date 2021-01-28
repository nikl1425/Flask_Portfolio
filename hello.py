from flask import Flask, jsonify
from flask import render_template
from Utility import myReader, readWord
from datetime import datetime
import sys

descriptionDoc = 'static/assets/text/description.docx'
educationDoc = 'static/assets/text/education.docx'
jobDoc = 'static/assets/text/job.docx'


#sys.path.append('/Users/niklashjort/Desktop/Projects/Flask_Portfolio-master/venv/lib/python3.9/site-packages/flask_cors/')
app = Flask(__name__)

print(sys.path)

myTemplate = myReader
readDocument = readWord

app.config['JSON_ADD_STATUS'] = True
app.config['JSON_DATETIME_FORMAT'] = '%d/%m/%Y %H:%M:%S'
#dapd
@app.route('/')
def hello_world():
  description = readDocument('')
  print(description)
  return render_template('home.html', description=description)

@app.route('/about')
def aboutPage():
  return render_template('about.html')

@app.route('/project')
def projectPage():
  return render_template('project.html')


if __name__ == '__main__':
  app.run(port=8080, debug=True)




