def extract_topic_keywords(df, column, nr_topics):
    """
    Extract topic and keywords from a text column using BERTopic.

    Parameters:
    - df: DataFrame containing the data
    - column: name of the column with the text
    - nr_topics: maximum number of topics (optional)

    Returns:
    - topic_keywords: dictionary {topic_id: [keyword1, keyword2, ...]}
    - df with 'Topic_ID' column
    - model topic_model
    """
    from bertopic import BERTopic

        # 2. Preprocessing of text column
    df[column] = df[column].astype(str)
    df[column] = df[column].apply(clean_for_bert)

    docs = df[column].astype(str).tolist()
    
    topic_model = BERTopic(nr_topics=nr_topics, calculate_probabilities=True, verbose=True)
    topics, _ = topic_model.fit_transform(docs)

    # Map topics to keywords
    topic_keywords = {}
    for topic_id in set(topics):
        if topic_id == -1:
            continue  # skip outliers
        topic_data = topic_model.get_topic(topic_id)
        if topic_data and hasattr(topic_data, "__iter__"):
            topic_keywords[topic_id] = [word for word, _ in topic_data]
        else:
            topic_keywords[topic_id] = []

    df["Topic_ID"] = topics

    return topic_keywords, df, topic_model