from youtube_transcript_api import YouTubeTranscriptApi
import pandas as pd
import os

def concanate_transcript(dataFrame):
    concanated_transcript = ""
    for i in range(len(dataFrame)):
        # print(len(dataFrame))
        # print(dataFrame["text"][i])
        concanated_transcript += dataFrame["text"][i] + " "
    return concanated_transcript

video_url = "https://www.youtube.com/watch?v=JJ0St6OmTp0"

def extract_video_id(url):
    try:
        chars = ""
        index = 0
        while chars != "v=":
            chars = url[index : index + 2]
            index += 1
        video_id = url[index + 1:]
        return video_id
    except:
        return 0

video_id = extract_video_id(video_url)


# assigning srt variable with the list of dictionaries
# obtained by the .get_transcript() function
# and this time it gets only the subtitles that
# are of the English language.

srt = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])

# specify the file path for the Excel file
output_file_path = os.path.join(os.getcwd(), "output.xlsx")

# create DataFrame
dataframe = pd.DataFrame(data=srt)

# save to Excel
dataframe.to_excel(output_file_path, index=False, sheet_name=video_id, engine="openpyxl")

#save to csv
dataframe.to_csv("output.csv", index=False)

# print the success message
# print(f"Excel file saved to: {output_file_path}")

string = concanate_transcript(dataframe)

# save to txt
text_file = open("output.txt", "w")
text_file.write(string)
text_file.close()

