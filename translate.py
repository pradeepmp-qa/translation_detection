from flask import Flask, render_template, request
from textblob import TextBlob



# initialse the application
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('form.html')

@app.route('/submit' , methods = ["POST"])
def form_data():
   language = request.form.get('language_to_translate')
   valid_text = request.form.get('input_text')
   blob = TextBlob(valid_text)
   out = blob.translate(to = language)
   # Language detection:
   initial_blob = TextBlob(valid_text)
   detect_blob = initial_blob.detect_language()

   return render_template('predict.html' , data = f' {out}',detected_data = f'original statement was in {detect_blob}')
#    return render_template('predict.html' , sentence_data = f'Number of sentences are {sentence_length}')
if __name__ == '__main__':
    app.run(debug = True)

