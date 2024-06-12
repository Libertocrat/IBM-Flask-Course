"""
Flask server for the Sentiment Detector app
"""

from flask import Flask
from flask import render_template, make_response, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    """
    Renders the home page
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def detect_emotion():
    """
    Performs sentiment analysis on the input text sent through the "textToAnalyze" query parameter.
    Returns the emotion predictions for a given text
    """
    # Parse text to analyze
    input_text = request.args.get("textToAnalyze")
    emotion_output = emotion_detector(input_text)

    if emotion_output is None:
        res = make_response("<strong>An error has ocurred. Please try again!</strong>")
    elif emotion_output['dominant_emotion'] is not None:

        # Format response message
        output_msg = f"""
        For the given statement, the system response is 'anger': {emotion_output['anger']}, 'disgust': {emotion_output['disgust']}, 
        'fear': {emotion_output['fear']}, 'joy': {emotion_output['joy']} and 'sadness': {emotion_output['sadness']}.
         The dominant emotion is <strong>{emotion_output['dominant_emotion']}</strong>
        """
        res = make_response(output_msg)
    else:
        res = make_response("<strong>Invalid text! Please try again!</strong>")

    return res

app.run(host="localhost", port=5000)

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
