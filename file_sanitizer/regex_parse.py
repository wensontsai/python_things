import os
import glob
import json
import re

# Get root paths.
path = os.getcwd()

# Result file.
output_file = "sanitized.json"

# Open every JSON file in path
for file in glob.glob(os.path.join(path, '*.json')):

    # Find file.
    if file.split("/")[-1] == "transcripts_block.json":
        print("found: ", file.split("/")[-1])

        # Output dict.
        parsed_data = {}

        try:
            # Read in
            with open(file, 'r') as json_file:
                data = json.load(json_file)

                # Get body text
                text = data.get('body')

                # (1) use regex to parse into sections.
                result = re.findall(r'\n(.*?)\n', text)
                print(result)
                # a. Remove "=============" header breaker (assuming it is first element)
                result.pop(0)

                # b. convert to pairs as tuples
                paired_result = zip(result[0::2], result[1::2])

                # Parse data per section into JSON.
                for tuple in paired_result:
                    # Save every pair (assuming they are paired correctly)
                    parsed_data[tuple[0]] = tuple[1]

            # Save out to file.
            with open(output_file, 'w') as json_file:
                json.dump(parsed_data, json_file, indent=4, sort_keys=True)
                print("file saved to: ", path +  "/" +output_file)

        except Exception as e:
            raise e
            print("No files found!")
