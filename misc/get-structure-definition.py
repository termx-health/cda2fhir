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
                # Extract the content, code, and contentFormat
                content = element.get('content')
                code = element.get('code')
                content_format = element.get('contentFormat')
                
                # Ensure all required fields are present
                if content and code and content_format:
                    # Determine the file extension based on the contentFormat
                    extension = content_format.split('/')[-1]
                    
                    # Create the filename
                    filename = f"{code}.{extension}"
                    
                    # Save the content to a file
                    with open(filename, 'w') as file:
                        file.write(content)
                    
                    print(f"File saved: {filename}")
                else:
                    print(f"Missing required fields in element: {element}")
            else:
                print(f"Element is not a dictionary: {element}")
    else:
        print(f"Data is not a list: {data}")

# URL of the API
api_url = "https://termx.taltech.ee/api/structure-definitions"

# Call the function
get_data_and_save_files(api_url)

