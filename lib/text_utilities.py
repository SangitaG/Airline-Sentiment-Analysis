
def tokenize(text):
    '''
    split string of text into list f words.
    '''
    
    return(text.split())

def cleaner(text):
    '''
    clean tweets.
    '''
    
    # convert text to lowercase.
    text = text.lower()
    # remove www.* or https?://* to URL
    text = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','',text)
    # remove @username to AT_USER
    text = re.sub('@[^\s]+','',text)
    # remove additional white spaces
    text = re.sub('[\s]+', ' ', text)
    # Replace #word with word
    text = re.sub(r'#([^\s]+)', r'\1', text)
    # remove some punctuation symbols.
    text= ''.join(ch for ch in text if ch not in exclude_punctuation)
    # clean
    text = re.sub('&#39;','',text).lower()
    # trim
    text = text.strip('\'"')
    # trim any leading or trailing white spaces.
    text = text.strip()

    return(text)

def remove_stopwords(text):
    '''
    remove english stop words
    '''
    word_lst = tokenize(text)
    out = [word.strip() for word in word_lst if word not in stop_words]   
    
    text = ' '.join(out)
    return(text)

def stemming(text):
    '''
    eliminate plurals and redundancy of words (ie thank, thanks)
    '''
    ps = PorterStemmer()
    text = tokenize(text)
    text = ' '.join(ps.stem(word) for word in text)
    return(text)

def declump_emojis(text):
    em_txt = text        
    for i in text:
        if (i in emoji.UNICODE_EMOJI):
            print(i)
            em_txt = em_txt.replace(i,' '+i+' ')
        
    return(em_txt)

def process_doc(text):
    
    rem_stop = " ".join([i for i in text.lower().split() if i not in stop])
    rem_punc= ''.join(ch for ch in rem_stop if ch not in exclude)
    text = " ".join(lemma.lemmatize(word) for word in rem_punc.split())
    
    return(text)


