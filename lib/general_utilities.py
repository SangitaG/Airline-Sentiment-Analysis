import pickle
import re
from tqdm import tqdm

# clean text.
def cleaner(text):
    '''
    cleans html tags and newline character from text.
    '''
    TAG_RE = re.compile(r'<[^>]+>')
    text = TAG_RE.sub('', text)
    text = re.sub('\n', '', text)
                  
    return(text)

def clean_text(page_lst):
    '''
    method called to clean text from a list of documents.
    '''
    for page in tqdm(page_lst):
        page['text'] = cleaner(page['text'])
    
    return(page_lst)

def pickle_obj(filename, objname):
    '''
    method called to pickle object.
    '''
    filehandler = open(filename,"wb")
    pickle.dump(objname,filehandler)

def read_pickle_obj(filename):
    '''
    method called to read pickled object.
    '''
    file = open(filename,'rb')
    object_content = pickle.load(file)
    return(object_content)