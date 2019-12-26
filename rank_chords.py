import codecs
import json

def read_file(filepath):
	master_dict = dict()
	master_tups = list()
		
	with open(filepath) as f:
		for line in f:
			line_list = line.rstrip().strip('\r').split(' ')
			master_dict[line_list[0]] = {'notes':line_list[1:]}
			master_tups.append(tuple((line_list[0], line_list[1:])))
	for key, value in master_dict.items():
		d = dict()
		for i in master_tups:
			cnt = 0
			if i[0] == key:
				pass
			else:
				for l in i[1]:
					if l in value['notes']:
						cnt += 1
			if cnt not in [0,1,2]:  
				if cnt not in d:
					d[cnt] = [i[0]]
				elif cnt in d:
					if i[0] in d[cnt]:
						pass
					else:
						d[cnt].append(i[0])
		master_dict[key]['matches'] = d
	
	print(json.dumps(master_dict, indent=4))

if __name__ == "__main__":
	file = 'all_chords.txt'
	read_file(file)
