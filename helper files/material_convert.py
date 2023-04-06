import os
import json

directory = '.'

# Loop through all files in current directory
for filename in os.listdir(directory):

    # only select files that end with .json
    if filename.endswith('.json'):
        filepath = os.path.join(directory, filename)

        # Open the file and read contents
        with open(filepath, 'r') as file:
            contents = file.read()
            data = json.loads(contents)

            # Loop through nested keys in json dictionary and update units depending on the property key.
            for grade in data:
                for treatment in data[grade]:
                    for property in data[grade][treatment]:
                        if (property == "den"):
                            value = data[grade][treatment][property]
                            data[grade][treatment][property] = {
                                "unit": {
                                    "numerator": ["pound"],
                                    "denominator": ["inches_cubed"]
                                },
                                "val": value
                            }
                        if (property == "yield_str"):
                            value = data[grade][treatment][property]
                            data[grade][treatment][property] = {
                                "unit": {
                                    "numerator": ["pound"],
                                    "denominator": ["inches_squared"]
                                },
                                "val": value
                            }
                        if (property == "ult_str"):
                            value = data[grade][treatment][property]
                            data[grade][treatment][property] = {
                                "unit": {
                                    "numerator": ["pound"],
                                    "denominator": ["inches_squared"]
                                },
                                "val": value
                            }
                        if (property == "elongation"):
                            value = data[grade][treatment][property]
                            data[grade][treatment][property] = {
                                "unit": None,
                                "val": value
                            }
                        if (property == "moe"):
                            value = data[grade][treatment][property]
                            data[grade][treatment][property] = {
                                "unit": {
                                    "numerator": ["pound"],
                                    "denominator": ["inches_squared"]
                                },
                                "val": value
                            }
                        if (property == "pr"):
                            value = data[grade][treatment][property]
                            data[grade][treatment][property] = {
                                "unit": None,
                                "val": value
                            }
                        if ('temp' in property):
                            value = data[grade][treatment][property]
                            data[grade][treatment][property] = {
                                "unit": "degrees_fahrenheit",
                                "val": value
                            }
                        if (property == 'coef_thermal_exp'):
                            value = data[grade][treatment][property]
                            data[grade][treatment][property] = {
                                "unit": None,
                                "val": value
                            }

        # Rewrite the json file with updates
        with open(filepath, 'w') as file:
            file.write(json.dumps(data, indent=4))
