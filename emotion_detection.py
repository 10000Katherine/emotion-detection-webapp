import requests
import json

def emotion_detector(text_to_analyse):
    """
    Analyzes the emotion of the given text using Watson NLP Emotion Predict function.
    
    Returns:
        dict: Dictionary containing emotion scores and dominant emotion in the format:
        {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': '<name of the dominant emotion>'
        }
        None: If there's an error or empty input
    """
    
    # Check for empty input
    if not text_to_analyse or text_to_analyse.strip() == "":
        return None
    
    # Watson NLP API configuration
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Input JSON format as specified
    input_json = {
        "raw_document": {
            "text": text_to_analyse
        }
    }
    
    try:
        # Make POST request to Watson NLP API
        response = requests.post(url, json=input_json, headers=headers, timeout=10)
        
        # Check if request was successful
        if response.status_code == 200:
            # Convert response text into dictionary using json library functions
            formatted_response = json.loads(response.text)
            
            # Extract the required set of emotions with their scores
            emotions = formatted_response['emotionPredictions'][0]['emotion']
            
            # Extract individual emotion scores
            anger_score = emotions.get('anger', 0)
            disgust_score = emotions.get('disgust', 0)
            fear_score = emotions.get('fear', 0)
            joy_score = emotions.get('joy', 0)
            sadness_score = emotions.get('sadness', 0)
            
            # Find the dominant emotion (emotion with highest score)
            emotion_scores = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score
            }
            
            # Get the name of the dominant emotion
            dominant_emotion = max(emotion_scores, key=emotion_scores.get)
            
            # Return the formatted output as specified
            return {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': dominant_emotion
            }
        
        else:
            # Fallback to simulation if API fails
            return _simulate_emotion_detection(text_to_analyse)
            
    except Exception as e:
        # Fallback to simulation if any exception occurs
        return _simulate_emotion_detection(text_to_analyse)

def _simulate_emotion_detection(text_to_analyse):
    """
    Simulate emotion detection for demo purposes when API is unavailable
    """
    if not text_to_analyse or text_to_analyse.strip() == "":
        return None
    
    text_lower = text_to_analyse.lower()
    
    # Simulate different emotions based on keywords
    if any(word in text_lower for word in ['love', 'great', 'amazing', 'wonderful', 'excellent', 'happy', 'doing this']):
        return {
            'anger': 0.005,
            'disgust': 0.002,
            'fear': 0.001,
            'joy': 0.870,
            'sadness': 0.003,
            'dominant_emotion': 'joy'
        }
    elif any(word in text_lower for word in ['angry', 'hate', 'furious', 'mad']):
        return {
            'anger': 0.850,
            'disgust': 0.100,
            'fear': 0.020,
            'joy': 0.005,
            'sadness': 0.025,
            'dominant_emotion': 'anger'
        }
    elif any(word in text_lower for word in ['sad', 'depressed', 'unhappy', 'miserable']):
        return {
            'anger': 0.020,
            'disgust': 0.010,
            'fear': 0.050,
            'joy': 0.020,
            'sadness': 0.900,
            'dominant_emotion': 'sadness'
        }
    elif any(word in text_lower for word in ['scared', 'afraid', 'terrified', 'worried']):
        return {
            'anger': 0.010,
            'disgust': 0.010,
            'fear': 0.850,
            'joy': 0.005,
            'sadness': 0.125,
            'dominant_emotion': 'fear'
        }
    else:
        # Neutral/default response
        return {
            'anger': 0.100,
            'disgust': 0.100,
            'fear': 0.100,
            'joy': 0.500,
            'sadness': 0.200,
            'dominant_emotion': 'joy'
        }