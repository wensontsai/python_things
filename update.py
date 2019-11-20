import os
import glob
import json


# Get root paths.
curr_root = os.getcwd()
print(curr_root)

# Can define path further.
path = curr_root

# Update dict.
updates = {
	"office.medical.0.price": "$$$$$$",
	"office.parking.style": "$$$$$$",
	"office.medical.3.sq-ft": "$$$$$$"
}

def try_as_int(string):
	try:
		return int(string)
	except ValueError:
		return string


# Helper func to traverse nested JSON
def update_param(json_input, lookup_key, update_value):

	# break up lookup_key
	key_list = [try_as_int(key) for key in lookup_key.split(".")]
	node = json_input

	try:
		for key in key_list[:-1]:
			if isinstance(key, int):
				node = node[key]
			else:
				node = node.get(key)

		# Traverse until end, and update last key with new value.
		node.update({key_list[-1]: update_value})

		# if isinstance(json_input, dict):
		# 	for k, v in json_input.items():
		# 		if k == lookup_key:
		# 			print("found dict it:", v)
		# 			yield v
		# 		else:
		# 			yield from update_param(v, lookup_key, update_value)
		# elif isinstance(json_input, list):
		# 	for item in json_input:
		# 		print("found list it:", v)
		# 		yield from update_param(item, lookup_key, update_value)

	except:
		print("Key not found - cannot update value!")


# Helper func to read from nested JSON
def get_param(json_input, lookup_key):

	# break up lookup_key
	key_list = [try_as_int(key) for key in lookup_key.split(".")]
	print(key_list)
	node = json_input

	try:
		for key in key_list:
			node = node[key]
		return node
	except:
		print("Key not found")


# Open every JSON file in path
for file in glob.glob(os.path.join(path, '*.json')):

	try:
		if file.endswith(".json"):
			print ("JSON file found:\t", file)

			# Read in
			with open(file, 'r') as json_file:
				data = json.load(json_file)

			# Update
			for key, new_value in updates.items():
				update_param(data, key, new_value)

			# Save and close to same file.
			with open(file, 'w') as json_file:
				json.dump(data, json_file, indent=4, sort_keys=True)


	except Exception as e:
		raise e
		print ("No files found!")
