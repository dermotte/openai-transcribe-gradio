# OpenAI Transcribe
A small project that should allow me to easily transcribe audio files using the OpenAI API. Run it with 

`uv run main.py`

You can use a gradio interface to transcribe an audio file.

3. Finds the next available temporary MP3 filename.
4. Converts the input audio file to MP3 format at 64 kbps.
5. Sends the MP3 file to the OpenAI transcription API.
6. Returns resulting transcription.

## How to set your API key?

In MS Powershell: 

`$Env:OPENAI_API_KEY = "<yourkey>"`