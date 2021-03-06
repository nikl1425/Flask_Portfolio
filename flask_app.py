from flask import Flask, request, render_template
from Utility import myReader, readWord, Client
import nexmo

descriptionDoc = 'static/assets/text/description.docx'
educationDoc = 'static/assets/text/education.docx'
jobDoc = 'static/assets/text/job.docx'

client = Client

# sys.path.append('/Users/niklashjort/Desktop/Projects/Flask_Portfolio-master/venv/lib/python3.9/site-packages/flask_cors/')
app = Flask(__name__)

# print(sys.path)

myTemplate = myReader
readDocument = readWord

app.config['JSON_ADD_STATUS'] = True
app.config['JSON_DATETIME_FORMAT'] = '%d/%m/%Y %H:%M:%S'


# dapd
@app.route('/')
def hello_world():
    description = readDocument('static/assets/text/description.docx')
    job = readDocument('static/assets/text/job.docx')
    education = readDocument('static/assets/text/education.docx')
    return render_template('index.html', description=description, job=job, education=education)


@app.route('/Contact', methods=['GET', 'POST'])
def aboutPage():
    if request.method == 'POST':
        name = request.form['name']
        number = request.form['number']
        email = request.form['email']
        message = request.form['message']
        message = ("name: " + name + "number: " + number + " email: " + email + " message: " + message)
        client.sendSms(message)
    return render_template('/new/contact.html')


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
    Snake = readDocument('static/assets/text/snake.docx')
    Hangman = readDocument('static/assets/text/Hangman.docx')
    Tetris = readDocument('static/assets/text/Tetris.docx')
    Weather = readDocument('static/assets/text/Weather.docx')
    return render_template('/new/proj.html',
                           IMDB=IMDB,
                           TD=TD,
                           CodeLearn=CodeLearn,
                           Portfolio=Portfolio,
                           MineSweeper=MineSweeper,
                           Maze=Maze,
                           Chicago=Chicago,
                           Pokemon=Pokemon,
                           Database=Database,
                           Snake=Snake,
                           Hangman=Hangman,
                           Tetris=Tetris,
                           Weather=Weather)


if __name__ == '__main__':
    app.run(debug=True)
