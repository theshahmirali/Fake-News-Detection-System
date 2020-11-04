def build_comment_dictionary(df, comment_scores):
    count = 0
    # Building Sentiment Analyser.
    from nltk import tokenize
    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    analyser = SentimentIntensityAnalyzer()
    
    for value in df.itertuples():
        post_id = value[6]
        comment = value[3]
        if post_id in comment_scores:
            sentiment_score = analyser.polarity_scores(comment)["compound"]
            new_score = comment_scores[post_id][0] + sentiment_score
            new_count = comment_scores[post_id][1] + 1
            comment_scores[post_id] = [new_score, new_count]
            count += 1
            
def post_sentiment(post):
    from nltk import tokenize
    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    analyser = SentimentIntensityAnalyzer()
    sentiment_score = analyser.polarity_scores(post)["compound"]
    return sentiment_score
