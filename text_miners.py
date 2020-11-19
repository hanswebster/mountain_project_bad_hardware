# functions to mine for certain words or phrases in text
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer

from keywords import bad_bolt_adj_syns,bad_bolt_vb_syns, bad_bolt_explicits, bolt_stem_set

ps = PorterStemmer()
adj_vb_tags = ['ADJ', 'ADV', 'VERB']

def bolt_text_bad(text):
    for phrase in bad_bolt_explicits: # check for explicits first
        if phrase in text:
            #print("found explicit")
            return True

    return has_bolts_and_trigger_words(text)

def has_bolts_and_trigger_words(text):
    text = text + ". sample sentence"
    tokenized_word = word_tokenize(text)
    word_with_pos = nltk.pos_tag(tokenized_word, tagset='universal')
    
    tokenized_sent = sent_tokenize(text)
    sentence_lengths = [len(word_tokenize(sentence)) for sentence in tokenized_sent]
    
    #print(tokenized_sent)
    result = False
    index = 0
    for length in sentence_lengths:
        next_index = index+length
        sent = word_with_pos[index:next_index]
        #print(bolt_sent(sent))
        result = result or (bolt_sent(sent) and bolt_sent_bad(sent))
        index += length

        if result:
            break
    return result



def bolt_sent_bad(sent): #TODO: add logging here
    word_tokens = [word[0] for word in sent]
    sent_with_pos = sent
    #print(sent_with_pos)
    stemmed_words = []
    
    for word in word_tokens:
        stemmed_words.append(ps.stem(word))

    close_adj_list = []
    for pair in sent_with_pos: #TODO: replace this nested loop with better dictionary for hyphens later
        if pair[1] in adj_vb_tags:
            pair_words = pair[0].split('-')
            for word in pair_words:
                close_adj_list.append(word)
    #print(close_adj_list)

    close_adj_syns = set([]) # abstract this into function, then import
    for adj in close_adj_list:
        syns = wordnet.synsets(adj)
        syn_words = set([syn.lemmas()[0].name() for syn in syns])
        close_adj_syns = close_adj_syns | syn_words
    #print(close_adj_syns)
    #print(bad_bolt_adj_syns)
    return bool(bad_bolt_adj_syns & close_adj_syns) or bool(bad_bolt_vb_syns & close_adj_syns)


def bolt_sent(sent): # list[tuple[str, str]]) -> bool: #TODO: add logging here
    word_tokens = [word[0] for word in sent]
    stemmed_words = []
    for word in word_tokens:
        stemmed_words.append(ps.stem(word))
    sent_set = set(stemmed_words)
    #print('bolt sent set: ')
    #print(sent_set)
    return bool(bolt_stem_set & sent_set)



#text = 'There is a bad crimp. The bolt spins. '
#print(bolt_text_bad(text))