from youtube_transcript_api import YouTubeTranscriptApi
import pandas as pd
import os

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

print(video_id)

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

print(f"Excel file saved to: {output_file_path}")

print(dataframe)