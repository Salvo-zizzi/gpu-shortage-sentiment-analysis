def HG_sentiment(df, column):
    """
    Calculate the sentiment of news articles using a Hugging Face model (distilBERT with 2 classes).
    Returns the dataframe with Sentiment, Score.
    """
    from transformers import pipeline

    # Convert to string
    df[column] = df[column].astype(str)

    # Initialize the pipeline
    sentiment_pipeline = pipeline(
        "sentiment-analysis", 
        model="distilbert-base-uncased-finetuned-sst-2-english"
    )

    # Apply the pipeline once for each text
    results = sentiment_pipeline(df[column].tolist(), truncation=True, max_length=512, batch_size=8) # truncate if too long

    results_df = pd.DataFrame(results)
    df['Sentiment'] = results_df['label'].str.lower()
    df['Score'] = results_df['score'].round(4)

    return df