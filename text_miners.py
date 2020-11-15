# functions to mine for certain words or phrases in text
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer

from keywords import bad_bolt_adj_syns, bad_bolt_explicits

ps = PorterStemmer()
adj_tags = ['JJ', 'JJR', 'JJS']

def bolt_text_bad(text):
    for phrase in bad_bolt_explicits: # check for explicits first
        if phrase in text:
            return True

    tokenized_sent = sent_tokenize(text)
    #print(tokenized_sent)
    result = False
    for sent in tokenized_sent:
        result = result or bolt_sent_bad(sent)
    return result



def bolt_sent_bad(sent): #TODO: add logging here
    word_tokens = nltk.word_tokenize(sent)
    sent_with_pos = nltk.pos_tag(word_tokens)
    stemmed_words = []
    
    for word in word_tokens:
        stemmed_words.append(ps.stem(word))

    close_adj_list = []
    for pair in sent_with_pos: #TODO: replace this nested loop with better dictionary for hyphens later
        if pair[1] in adj_tags:
            pair_words = pair[0].split('-')
            for word in pair_words:
                close_adj_list.append(word)

    close_adj_syns = set([]) # abstract this into function, then import
    for adj in close_adj_list:
        syns = wordnet.synsets(adj)
        syn_words = set([syn.lemmas()[0].name() for syn in syns])
        close_adj_syns = close_adj_syns | syn_words

    return bool(bad_bolt_adj_syns & close_adj_syns)



text = 'There is a star-drive bolt'
print(bolt_text_bad(text))