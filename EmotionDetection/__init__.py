"""
EmotionDetection Package

This package provides emotion detection functionality using Watson NLP API
with fallback simulation for demo purposes.
"""

from .emotion_detection import emotion_detector

__version__ = "1.0.0"
__author__ = "Your Name"
__all__ = ["emotion_detector"]