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

#print(sys.path)

myTemplate = myReader
readDocument = readWord

app.config['JSON_ADD_STATUS'] = True
app.config['JSON_DATETIME_FORMAT'] = '%d/%m/%Y %H:%M:%S'
#dapd
@app.route('/')
def hello_world():
  description = readDocument('static/assets/text/description.docx')
  job = readDocument('static/assets/text/job.docx')
  education = readDocument('static/assets/text/education.docx')
  return render_template('index.html', description=description, job=job, education=education)

@app.route('/about')
def aboutPage():
  return render_template('about.html')

@app.route('/project')
def projectPage():
  IMDB = readDocument('static/assets/text/IMDB.docx')
  TD = readDocument('static/assets/text/TowerDefence.docx')
  CodeLearn = readDocument('static/assets/text/codeLearningGame.docx')
  Portfolio = readDocument('static/assets/text/portfolio.docx')
  MineSweeper = readDocument('static/assets/text/mineSweeper.docx')
  Maze = readDocument('static/assets/text/maze.docx')
  Chicago = readDocument('static/assets/text/Chicago.docx')
  Pokemon = readDocument('static/assets/text/pokemon.docx')
  Database = readDocument('static/assets/text/database.docx')
  return render_template('/new/proj.html',
                         IMDB=IMDB,
                         TD=TD,
                         CodeLearn=CodeLearn,
                         Portfolio=Portfolio,
                         MineSweeper=MineSweeper,
                         Maze=Maze,
                         Chicago=Chicago,
                         Pokemon=Pokemon,
                         Database=Database)



if __name__ == '__main__':
  app.run(debug=True)




