import sys
from docx2txt import docx2txt
import nexmo


#print(sys.path)

# This reader read an html template to a string
def myReader(path): 
  fname = path
  html_file = open(fname, 'r', encoding='utf-8')
  source_code = html_file.read()
  source_code = source_code.rstrip('\n')
  print(source_code)
  return (source_code)


def readWord(path):
  my_string = docx2txt.process(path)
  return my_string


class Client:
    def sendSms(text):
        client = nexmo.Client(key='76e45d59', secret='U4OZwIimNkIUBqtB')
        client.send_message({
            'from': 'Vonage APIs',
            'to': '4553577221',
            'text': text,
        })




