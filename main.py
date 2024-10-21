import pandas as pd
from fuzzywuzzy import fuzz
import numpy as np


# 1. Read the main Excel file, starting from the 8th row (index 7)
file_path = 'kopsavilkums_par_profesijam_2024_gada_augusts_bez_retajam_profesijam.xlsx'  # Replace with your actual file path
df = pd.read_excel(file_path, header=None, skiprows=7)

# 2. Initialize a list to store the valid rows
valid_rows = []

# 3. Process each row in the DataFrame
for index, row in df.iterrows():
    # Get the first column value
    first_col_value = str(row[0])  # Convert to string for further processing
    
    # 4. Split the first column value to isolate the ID
    parts = first_col_value.split(' ', 1)  # Split into ID and the rest
    id_part = parts[0]  # The first part is the ID

    # 5. Check if the ID part has at least 6 digits and starts with '6'
    if len(id_part) > 5 and id_part.isdigit():
        # 6. Extract the values from the row and remove commas
        values = [str(value).replace(',', '') for value in row[:7]]  # Get first 7 values and remove commas
        valid_rows.append(values)

# 7. Print the valid rows for verification
for row in valid_rows:
    print(row[0]) 

# --- Local Comparison Section ---

# 8. Define the local word/sentence to compare against
comparison_word = "DEŽURANTS"  # Replace with your actual word or sentence

succesfull_words = []

# 9. Compare valid rows with the local comparison word using multiple fuzzy matching methods
def Meklēšana(percentage):
    print("meklē")
    
    succesfull_words = []  # Initialize the list to store successful words
    
    for row in valid_rows:
        parts = row[0].split(' ', 1) 
        if len(parts) > 1:  # Ensure the row has more than one part
            parts = parts[1]
        else:
            continue
        
        scores = []
        
        # FuzzyWuzzy comparison methods
        scores.append(fuzz.partial_ratio(parts, comparison_word))  # Partial ratio
        scores.append(fuzz.token_sort_ratio(parts, comparison_word))  # Token sort ratio
        scores.append(fuzz.token_set_ratio(parts, comparison_word))  # Token set ratio

        # Calculate the average score
        average_score = sum(scores) / len(scores)

        # Check if the average score meets the threshold
        if average_score >= percentage:
            succesfull_words.append(parts)
    
    return succesfull_words

# Call the function and process the results
succesfull_words = Meklēšana(90)

if len(succesfull_words) < 1:
    print("0")
    succesfull_words = Meklēšana(80)  # Try again with a lower threshold
elif len(succesfull_words) < 2:
    print(succesfull_words, "1")
    #atgriež uzreiz, pajautā vai ie pareizi
elif len(succesfull_words) < 5 and len(succesfull_words) >= 2:
    print(succesfull_words, "2")
    #atgriež piedāvā izvēlēties
else:
    print("Varat būt specifiskāks?")