from machinetranslation import translator
from flask import Flask, render_template, request, url_for, redirect
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    responseText = translator.english_to_french(textToTranslate)
    return responseText

@app.route("/frenchToEnglish", methods=['GET'])
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    responseText = translator.french_to_english(textToTranslate)
    return responseText


@app.route("/")
def renderIndexPage():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(port=8080, debug=True)
