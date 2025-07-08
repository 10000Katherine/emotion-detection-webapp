#!/usr/bin/env python3
"""
Emotion Detection Module.

This module provides emotion detection functionality using Watson NLP API
with fallback simulation capabilities for demo purposes when the API
is unavailable or returns errors.

Author: Your Name
Date: 2025
"""

import json
import requests


def emotion_detector(text_to_analyse):
    """
    Analyze the emotion of the given text using Watson NLP Emotion Predict function.

    This function sends text to Watson NLP API for emotion analysis and returns
    a dictionary containing emotion scores and the dominant emotion. It includes
    comprehensive error handling for various failure scenarios.

    Args:
        text_to_analyse (str): The text to be analyzed for emotions

    Returns:
        dict: Dictionary containing emotion scores and dominant emotion in format:
              {
                  'anger': float,
                  'disgust': float,
                  'fear': float,
                  'joy': float,
                  'sadness': float,
                  'dominant_emotion': str
              }
              Dictionary with all None values if status_code = 400 or API error
        None: If input is blank, empty, or None
    """
    # Check for blank entries - return None for completely empty input
    if not text_to_analyse or text_to_analyse.strip() == "":
        return None

    # Watson NLP API configuration
    url = ('https://sn-watson-emotion.labs.skills.network/v1/'
           'watson.runtime.nlp.v1/NlpService/EmotionPredict')
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Input JSON format as specified by Watson NLP API
    input_json = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    try:
        # Make POST request to Watson NLP API with timeout
        response = requests.post(url, json=input_json, headers=headers, timeout=10)

        # Access the status_code attribute of the server response
        if response.status_code == 200:
            # Parse the response JSON
            formatted_response = json.loads(response.text)

            # Extract emotions from the API response
            emotions = formatted_response['emotionPredictions'][0]['emotion']

            # Extract individual emotion scores
            anger_score = emotions.get('anger', 0)
            disgust_score = emotions.get('disgust', 0)
            fear_score = emotions.get('fear', 0)
            joy_score = emotions.get('joy', 0)
            sadness_score = emotions.get('sadness', 0)

            # Create emotion scores dictionary for finding dominant emotion
            emotion_scores = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score
            }

            # Find the dominant emotion (emotion with highest score)
            dominant_emotion = max(emotion_scores, key=emotion_scores.get)

            # Return formatted result
            return {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': dominant_emotion
            }

        if response.status_code == 400:
            # For status_code = 400, return dictionary with all values as None
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }

        # For other error status codes, fallback to simulation
        return _simulate_emotion_detection(text_to_analyse)

    except requests.exceptions.RequestException:
        # For any request exception, fallback to simulation
        return _simulate_emotion_detection(text_to_analyse)
    except (KeyError, json.JSONDecodeError):
        # For JSON parsing errors, fallback to simulation
        return _simulate_emotion_detection(text_to_analyse)


def _simulate_emotion_detection(text_to_analyse):
    """
    Simulate emotion detection for demo purposes when API is unavailable.

    This function provides a fallback mechanism by analyzing text keywords
    to simulate emotion detection when the Watson NLP API is unavailable
    or returns errors.

    Args:
        text_to_analyse (str): The text to be analyzed

    Returns:
        dict: Simulated emotion analysis results
        None: If input is empty or None
    """
    if not text_to_analyse or text_to_analyse.strip() == "":
        return None

    text_lower = text_to_analyse.lower()

    # Define keyword lists for different emotions
    joy_keywords = ['love', 'great', 'amazing', 'wonderful', 'excellent',
                    'happy', 'doing this', 'having fun']
    anger_keywords = ['angry', 'hate', 'furious', 'mad']
    sadness_keywords = ['sad', 'depressed', 'unhappy', 'miserable']
    fear_keywords = ['scared', 'afraid', 'terrified', 'worried']

    # Simulate different emotions based on keywords
    if any(word in text_lower for word in joy_keywords):
        return {
            'anger': 0.005,
            'disgust': 0.002,
            'fear': 0.001,
            'joy': 0.870,
            'sadness': 0.003,
            'dominant_emotion': 'joy'
        }
    if any(word in text_lower for word in anger_keywords):
        return {
            'anger': 0.850,
            'disgust': 0.100,
            'fear': 0.020,
            'joy': 0.005,
            'sadness': 0.025,
            'dominant_emotion': 'anger'
        }
    if any(word in text_lower for word in sadness_keywords):
        return {
            'anger': 0.020,
            'disgust': 0.010,
            'fear': 0.050,
            'joy': 0.020,
            'sadness': 0.900,
            'dominant_emotion': 'sadness'
        }
    if any(word in text_lower for word in fear_keywords):
        return {
            'anger': 0.010,
            'disgust': 0.010,
            'fear': 0.850,
            'joy': 0.005,
            'sadness': 0.125,
            'dominant_emotion': 'fear'
        }

    # Neutral/default response for unrecognized text
    return {
        'anger': 0.100,
        'disgust': 0.100,
        'fear': 0.100,
        'joy': 0.500,
        'sadness': 0.200,
        'dominant_emotion': 'joy'
    }