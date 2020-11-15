from nltk.corpus import wordnet

bolt_words = ['bolt', 'hardware', 'hanger', 'anchor', 'ring', 'carabiner', 'biner', 'chain', 'station', 'draw', 'perma-draw', 'piton', 'perma', 'link', 'quick-link' ]

bad_bolt_adjs = ['old', 'bad', 'rusted', 'inadequate', 'spinning', 'loose', 'broken', 'unsafe', 'nail', 'damaged', 'chopped', 'missing', 'worn']
bad_bolt_explicits = ['star-drive', 'stardrive', 'button-head', 'buttonhead', 'button head', 'quarter-in', 'quarterin', 'quarter in', '1/4 in', '1/4in', '1/4"']
bad_bolt_verbs = ['replace', 'repair', 'fix', 'maintain']
bad_bolt_adj_syns = set([])
for adj in bad_bolt_adjs:
    syns = wordnet.synsets(adj)
    syn_words = set([syn.lemmas()[0].name() for syn in syns])
    bad_bolt_adj_syns = bad_bolt_adj_syns | syn_words
