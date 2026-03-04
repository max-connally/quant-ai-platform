from transformers import pipeline

sentiment_model = pipeline("sentiment-analysis")

def analyze_sentiment(news_list):

    scores = []

    for headline in news_list:

        result = sentiment_model(headline)[0]

        if result["label"] == "POSITIVE":
            scores.append(result["score"])
        else:
            scores.append(-result["score"])

    if len(scores) == 0:
        return 0

    return sum(scores) / len(scores)
