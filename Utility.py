import sys
import docx2txt

print(sys.path)

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


hi = readWord("static/assets/text/beskrivelse.docx")

print(hi)