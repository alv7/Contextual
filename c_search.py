
import glob
import mmap

def search_file_contents(file_name, keyword):
	keyword = str.encode(keyword)
	with open(file_name, 'rb', 0) as file:
		try:
			with mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
				if s.find(keyword) != -1:
					return True
		except ValueError:
			pass	
	return False


def search_file(file_name, keyword):
	# if keyword is in title or contents
	if keyword in file_name or search_file_contents(file_name, keyword):
		return True
	else:
		return False

def search_folder(keyword):
	all_names = glob.glob('*.txt')
	filtered_names = []
	for name in all_names:
		if search_file(name, keyword):
			filtered_names.append(name)
	return filtered_names

res = search_folder(' ')
print(len(res), res)

