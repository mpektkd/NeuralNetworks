def preprocess(sentence, stem=False, lem=False):
    # rem_url=re.sub(r'http\S+', '',cleantext) ## MAYBE!
    # sentence=sentence.replace('{html}',"") 

    # Convert to String
    sentence=str(sentence)

    # Convert letters to lowercase 
    sentence = sentence.lower()

    # Remove Special Characters/Punctuations
    cleantext = re.sub(r'[^A-Za-z ]+', ' ', sentence)

    # Tokenize Corpus
    # This class applies, 
    # 1. Punctuation removing
    # 2. Tokenization
    tokenizer = RegexpTokenizer(r'\w+') 
    tokens = tokenizer.tokenize(cleantext)  

    # Remove StopWords
    filtered_words = [w for w in tokens if len(w) > 2 if not w in stopwords.words('english')]

    # Appply Stemming
    if stem:
      stemmer = PorterStemmer() 
      filtered_words=[stemmer.stem(w) for w in filtered_words]
    
    # Appply Lemmatization
    elif lem:
      lemmatizer = WordNetLemmatizer()
      filtered_words=[lemmatizer.lemmatize(w) for w in filtered_words]

    return " ".join(filtered_words)