from nltk.corpus import wordnet

bolt_words = ['bolt', 'hardware', 'hanger', 'anchor', 'ring', 'carabiner', 'biner', 'chain', 'station', 'draw', 'perma-draw', ]

bad_bolt_adjs = ['old', 'bad', 'rusted', 'inadequate', 'spinning', 'loose', 'broken', 'star-drive', 'button-head', 'quarter-inch', 'unsafe', 'nail', 'damaged']
bad_bolt_verbs = ['replace', 'repair', 'fix', 'maintain']
bad_bolt_adj_syns = set([])
for adj in bad_bolt_adjs:
    syns = wordnet.synsets(adj)
    syn_words = set([syn.lemmas()[0].name() for syn in syns])
    bad_bolt_adj_syns = bad_bolt_adj_syns | syn_words
