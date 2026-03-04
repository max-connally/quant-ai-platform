import random

def get_sentiment():

    score = random.uniform(-1,1)

    if score > 0.3:
        return "Positive"

    if score < -0.3:
        return "Negative"

    return "Neutral"
