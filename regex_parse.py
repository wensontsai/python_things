import os
import glob
import json

# Get root paths.
curr_root = os.getcwd()
# print(curr_root)

# Result.
output_file = "sanitized.json"

# Can define path further.
path = curr_root

# Open every JSON file in path
for file in glob.glob(os.path.join(path, '*.json')):
    if file.split("/")[-1] == "transcripts_block.json":
        print("found: ", file.split("/")[-1])

        # output
        parsed_data = {}

        try:
            # Read in
            with open(file, 'r') as json_file:
                data = json.load(json_file)

                # get body text
                text = data.get('body')

                # use regex to parse sections into json
                

            # Save and close to same file.
            with open(output_file, 'w') as json_file:
                json.dump(parsed_data, json_file, indent=4, sort_keys=True)


        except Exception as e:
            raise e
            print("No files found!")
