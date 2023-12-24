import nltk
import pandas as pd
import os
import math
nltk.download('punkt')

open_file = open("output.txt", "r")
string = open_file.read()
open_file.close()

# Separate into sentences
sentences = nltk.sent_tokenize(string)
# Separate into words
words = nltk.word_tokenize(string)

# Create data frame
df = pd.DataFrame(words, columns=["words"])

word_count = df["words"].value_counts().reset_index()
word_count.columns = ["words", "count"]

# Calculate frequency
word_count["frequency"] = word_count["count"] / len(words)  # Use len(words) instead of len(word_count)

# Calculate entropy
word_count["entropy"] = word_count["frequency"] * word_count["frequency"].apply(lambda x: -1 * math.log(x, 2))

# Calculate Shannon entropy
shannon_entropy = word_count["entropy"].sum()

# Calculate maximum Shannon entropy
max_entropy = math.log(len(word_count), 2)

print("Maximum Shannon Entropy:", max_entropy)
print("Calculated Shannon Entropy:", shannon_entropy)
print(word_count)

# save to excel
output_file_path = os.path.join(os.getcwd(), "shannon.xlsx")
word_count.to_excel(output_file_path, index=False, sheet_name="entropy", engine="openpyxl")