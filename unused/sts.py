
import os
# OpenMP Error #15 को ठीक करने के लिए
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"


import whisper
import json
model = whisper.load_model("large-v2")

result = model.transcribe(audio = "audios/sample audio song.mp3",
                          language = "hi",
                          task="translate",
                          word_timestamps = False)

chunks = []
for segment in result["segments"]:
    chunks.append({"start": segment["start"],"end": segment["end"],"text": segment["text"]})

print(chunks)

with open("output.json","w") as f:
   json.dump(chunks,f)


