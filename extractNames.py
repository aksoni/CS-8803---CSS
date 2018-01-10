import nltk

#outputFile = open('outputHTML.txt', 'w')
#with open('outputText.txt', 'r') as handle:
 #   for line in handle:
  #      line = line.lstrip(' ')
   #     if line and line[0].isalpha() and not line.startswith('o [') and not line.startswith('Headlines'):
    #        outputFile.write(line)
			
			
with open('2016scraped-traintest18KeywordOutput2.txt', 'r', encoding="utf8") as f:
    sample = f.read()

#keywords = ["kill", "kills", "killing", "killings", "killed", "shot", "shots", "shoot", "shoots", "shooting", "murder", "murders", "murdered"]

#print("sample", sample)
sentences = nltk.sent_tokenize(sample)
#for sent in sentences:
    #print("NEW SENTENCE", sent)
tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
#print("tagged", tagged_sentences)
chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=False)

def extract_entity_names(t):
    entity_names = []

    if hasattr(t, 'label') and t.label:
       # print("label", t.label())
        if t.label() == 'PERSON':
            entity_names.append(' '.join([child[0] for child in t]))
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))

    return entity_names

entity_names = []
for tree in chunked_sentences:
    # Print results per sentence
   # print(extract_entity_names(tree))
   #print("tree", tree)
    entity_names.extend(extract_entity_names(tree))

# Print all entity names
#print entity_names

# Print unique entity names
#print(set(entity_names))
entity_names = set(entity_names)
outputFile = open('2016scraped-traintest18NameOutput.txt', 'w', encoding='utf-8')
for name in entity_names:
    print("outputting", name)
    outputFile.write(name)
    outputFile.write('\n')
