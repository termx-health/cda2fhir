import requests
import os

# Function to get data from the API and save files
def get_data_and_save_files(api_url):
    # Send GET request to the API
    response = requests.get(api_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        body = response.json()
        data = body['data']
        
        # Iterate over each element in the data array
        for element in data:
            # Check if element is a dictionary
            if isinstance(element, dict):
                id = element.get('id')
                name = element.get('name')

                transformation_url = api_url + "/" + str(id)
                transformation_response = requests.get(transformation_url)
                if transformation_response.status_code == 200:
                    obj = transformation_response.json()
                    mapping = ""
                    resources = ""
                    example = ""
                    #print(obj)

                    for key in obj:
                        if key == "mapping":
                            mapping = obj[key]
                        if key == "resources":
                            mapping = obj[key]
                        if key == "testSource":
                            example = obj[key]
                    
                    # Ensure all required fields are present
                    if mapping:
                        # Create the filename
                        filename = f"{name}.mapping.json"
                        
                        # Save the content to a file
                        with open(filename, 'w') as file:
                            file.write(str(mapping))
                    
                    if resources:
                        # Create the filename
                        filename = f"{name}.resources.json"
                        
                        # Save the content to a file
                        with open(filename, 'w') as file:
                            file.write(str(resources))

                    if example:
                        # Create the filename
                        filename = f"{name}.example.json"
                        
                        # Save the content to a file
                        with open(filename, 'w') as file:
                            file.write(example)

            else:
                print(f"Element is not a dictionary: {element}")
    else:
        print(f"Data is not a list: {data}")

# URL of the API
api_url = "https://termx.kodality.dev/api/transformation-definitions"

# Call the function
get_data_and_save_files(api_url)

