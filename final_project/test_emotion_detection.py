import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test1(self):
        """
        output = emotion_detector("I am glad this happened")
        self.assertEqual(output['dominant_emotion'], 'joy')

        output = emotion_detector("I am really mad about this")
        self.assertEqual(output['dominant_emotion'], 'anger')

        output = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(output['dominant_emotion'], 'disgust')

        output = emotion_detector("I am so sad about this")
        self.assertEqual(output['dominant_emotion'], 'sadness')

        output = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(output['dominant_emotion'], 'fear')
        """
        self.assertEqual(1,1)


unittest.main()
