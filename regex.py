import re

# Sample input string
input_string = "Session Token-> BAMAuthToken: token <- for User : <user>"

# Define a regular expression pattern to match the desired substring
pattern = r'BAMAuthToken:\s*(.*?)\s*<'

# Use re.search to find the first match
match = re.search(pattern, input_string)

# Check if a match is found
if match:
    # Extract the matched substring
    extracted_string = match.group(1)

    # Create a dictionary for JSON formatting
    json_data = {"BAMAuthToken": extracted_string}

    # Convert the dictionary to JSON format
    json_string = json.dumps(json_data, indent=2)

    print(json_string)
else:
    print("Pattern not found in the input string.")
