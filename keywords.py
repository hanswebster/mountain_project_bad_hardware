from nltk.corpus import wordnet
from nltk.stem import PorterStemmer


ps = PorterStemmer()
bolt_words = ['bolted', 'bolts', 'hardware', 'hangers', 'anchor', 'ring', 'carabiners', 'biners', 'chains', 'station', 'draws', 'perma-draws', 'piton', 'perma', 'permas', 'link', 'quick-link' ]
bolt_stems = []
for word in bolt_words:
    bolt_stems.append(ps.stem(word))
bolt_stem_set = set(bolt_stems)


bad_bolt_explicits = ['star-drive', 'stardrive', 'button-head', 'buttonhead', 'button head', 'quarter-in', 'quarterin', 'quarter in', '1/4 in', '1/4in', '1/4"']
bad_bolt_verbs = ['replace', 'repair', 'fix', 'maintain']
bad_bolt_vb_syns = set([])
for vb in bad_bolt_verbs:
    syns = wordnet.synsets(vb)
    syn_words = set([syn.lemmas()[0].name() for syn in syns])
    bad_bolt_vb_syns = bad_bolt_vb_syns | syn_words

bad_bolt_adjs = ['old', 'bad', 'rusted', 'inadequate', 'spin', 'spinning', 'loose', 'broken', 'unsafe', 'nail', 'damaged', 'chopped', 'missing', 'worn']
bad_bolt_adj_syns = set([])
for adj in bad_bolt_adjs:
    syns = wordnet.synsets(adj)
    syn_words = set([syn.lemmas()[0].name() for syn in syns])
    bad_bolt_adj_syns = bad_bolt_adj_syns | syn_words
