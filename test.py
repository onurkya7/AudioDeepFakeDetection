import os
import librosa
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

def runtest(example_file_path):
    loaded_model = joblib.load("models/random_forest_model.joblib")

    def extract_features(file_path):
        try:
            audio, sample_rate = librosa.load(file_path, res_type='kaiser_fast') 
            mfccs = np.mean(librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40).T, axis=0)
            return mfccs
        except Exception as e:
            print("Error encountered while parsing file:", file_path)
            return None

    example_features = extract_features(example_file_path)
    if example_features is not None:
        prediction = loaded_model.predict([example_features])
        class_label = "Real" if prediction[0] == 1 else "Fake"
        return f"{class_label} Audio File"
    else:
        return "Error extracting features from the example file."
    

    
