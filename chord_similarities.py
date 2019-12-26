import difflib
import operator
import json


def read_file(filepath):
	tups = list()

	with open(filepath) as f:
	    for line in f:
	        line_list = line.rstrip().strip('\r').split(' ')
	        tups.append(tuple((line_list[0], line_list[1:])))
	return tups

def similarity_rank(input_chord, output_tups):
	ratio_ranks = dict()
	for tup in output_tups:
	    rat=difflib.SequenceMatcher(None,input_chord,tup[1]).ratio()
	    if rat not in ratio_ranks:
	        ratio_ranks[rat] = [tup]
	    else:
	        ratio_ranks[rat].append(tup)
	sorted_rank = sorted(ratio_ranks.items(), key=operator.itemgetter(0),reverse=True)
	for x in enumerate(sorted_rank):
	    print('Rank {} - {:.1%}'.format((x[0]+1), x[1][0]))
	    for match in x[1][1]:
		    print('\t{}'.format(match))
		    
if __name__ == "__main__":
	filepath = 'all_chords.txt'
	output_tups = read_file(filepath)
	input_chord = raw_input('Chords: ')
	input_chord = input_chord.split(' ')
	similarity_rank(input_chord, output_tups)