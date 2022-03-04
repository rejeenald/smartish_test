## Setting up dependencies
- the list dependencies are inside requirements.txt. Run the command `pip install -r requirementx.txt` to install them. Make sure you are on the directory with 'requirements.txt'.

## Supported filter parameters
- --kwargs (required)
    - this is a necessary before any arguments for filter parameters and location of the the final csv file
- creation_date_range
    - Format: start_date-end_date. For each date the format is year/month/day
    - Example: creation_date_range=2021/11/02-2022/2/26 
- article_id
    - Positive Integer
    - Example: article_id=71270196 # use in lieu of model number
- save_to (required)
    - Location on where to store the csv file.
    - Format: path_to_location/filename.csv
    - Example: 
        1. save_to=clean_data.csv
            - it will store at the same directory as the script.
        2. save_to=/Users/dlaneejer/Documents/smartish/clean_data.csv
            - it will this directory /Users/dlaneejer/Documents/smartish/ with the filename of clean_data.csv

## Running the script
Run the following comman in this format
`python main.py --kwargs creation_date_range=2021/11/02-2022/2/26 article_id=71270196 save_to=clean_data.csv`