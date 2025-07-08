#!/usr/bin/env python3
"""
Flask Server for Emotion Detection Application.

This module deploys the emotion detection functionality as a web service
using Flask framework. It provides endpoints for emotion analysis and
serves a web interface for user interaction.

Author: Your Name
Date: 2025
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

# Initialize Flask application
app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Handle emotion detection requests.

    This route expects a 'textToAnalyze' parameter in the request
    and returns formatted emotion analysis results with proper
    error handling for blank entries and API failures.

    Returns:
        str: Formatted emotion analysis results or error message
    """
    # Get the text to analyze from request parameters
    text_to_analyze = request.args.get('textToAnalyze')

    # Check if text is provided and not empty
    if not text_to_analyze or text_to_analyze.strip() == "":
        return "Invalid text! Please try again!"

    # Call the emotion detector function
    response = emotion_detector(text_to_analyze)

    # Check if the response is None (blank entry case)
    if response is None:
        return "Invalid text! Please try again!"

    # Extract emotion scores from response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Error handling: check if dominant_emotion is None (API error case)
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Format the response as requested by client specifications
    formatted_response = (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and "
        f"'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    )

    return formatted_response


@app.route("/")
def render_index_page():
    """
    Render the main index page.

    This route serves the main HTML interface for the emotion
    detection application.

    Returns:
        str: Rendered HTML template
    """
    return render_template('index.html')


if __name__ == "__main__":
    # Run the Flask application on localhost:5000 with debug mode
    app.run(host="0.0.0.0", port=5000, debug=True)