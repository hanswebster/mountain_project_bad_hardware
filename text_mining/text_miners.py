# functions to mine for certain words or phrases in text
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer

from .keywords import bad_bolt_adj_syns, bad_bolt_vb_syns, bad_bolt_explicits, bolt_stem_set

ps = PorterStemmer()
adj_vb_tags = ['ADJ', 'ADV', 'VERB']

def bolt_text_bad(text):
    if text and text.strip()[-1] not in '!.?':
        text += '.'
    text += " sample sentence." #nltk library improperly tags sentences without this for some reason
    tokenized_word = word_tokenize(text)
    word_with_pos = nltk.pos_tag(tokenized_word, tagset='universal')
    
    tokenized_sent = sent_tokenize(text)
    flag = []
    index = 0
    for sent in tokenized_sent:
        flagged = False
        length = len(word_tokenize(sent))
        next_index = index+length
        sent_pos = word_with_pos[index:next_index]
        
        for phrase in bad_bolt_explicits: # check for explicits first
            if phrase in sent:
                flag.append(sent) # += sent
                flagged = True
                continue
        if bolt_sent(sent_pos) and bolt_sent_bad(sent_pos) and not flagged:
            flag.append(sent) # += sent:

        index += length

    return flag


def bolt_sent_bad(sent):
    word_tokens = [word[0] for word in sent]
    sent_with_pos = sent
    stemmed_words = []
    
    for word in word_tokens:
        stemmed_words.append(ps.stem(word))

    close_adj_vb_list = []
    for pair in sent_with_pos: #TODO: replace this nested loop with better dictionary for hyphens later
        if pair[1] in adj_vb_tags:
            pair_words = pair[0].split('-')
            for word in pair_words:
                close_adj_vb_list.append(word)

    close_adj_vb_syns = set([]) #TODO: abstract this into function, then import
    for wd in close_adj_vb_list:
        syns = wordnet.synsets(wd)
        syn_words = set([syn.lemmas()[0].name() for syn in syns])
        close_adj_vb_syns = close_adj_vb_syns | syn_words
    return bool(bad_bolt_adj_syns & close_adj_vb_syns) or bool(bad_bolt_vb_syns & close_adj_vb_syns)


def bolt_sent(sent): 
    word_tokens = [word[0] for word in sent]
    stemmed_words = []
    for word in word_tokens:
        stemmed_words.append(ps.stem(word))
    sent_set = set(stemmed_words)
    return bool(bolt_stem_set & sent_set)


