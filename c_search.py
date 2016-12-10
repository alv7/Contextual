
import glob
import mmap
import ntpath

NOTES_PATH = 'notes'

def search_file_contents(file_name, keyword):
	keyword = keyword.lower()
	with open(file_name, 'r') as fl:
		for line in fl:
			if keyword in line.lower():
				return True
	return False

def search_file(file_name, keyword):
	# if keyword is in title or contents
	if keyword.upper() in file_name.upper() or search_file_contents(file_name, keyword):
		return True
	else:
		return False

def file_name_from_path(path):
	head, tail = ntpath.split(path)
	return tail or ntpath.basename(head)

def search_folder(keyword):
	types = (NOTES_PATH + '/' +'*.txt' , NOTES_PATH + '/' +'*.md')
	all_names = []
	for t in types:
		all_names.extend(glob.glob(t))
	filtered_names = []
	for name in all_names:
		if search_file(name, keyword):
			name = file_name_from_path(name)
			filtered_names.append(name)
	return filtered_names
