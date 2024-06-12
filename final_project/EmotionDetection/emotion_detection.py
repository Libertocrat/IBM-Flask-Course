import requests

def emotion_detector(text_to_analyze):

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": { "text": text_to_analyze } }

    # Send text to the WatsonX API for emotion predict
    res = requests.post(url, headers = headers, json = payload)

    # Format response body as json
    res_json = res.json()
    # Extract emotion scores
    emotions = res_json['emotionPredictions'][0]['emotion']

    # Identify dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    # Format output emotion json
    output = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }

    return(output)
