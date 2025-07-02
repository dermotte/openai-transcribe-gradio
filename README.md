# OpenAI Transcribe
A small project that should allow me to easily transcribe audio files using the OpenAI API. Run it with 

`uv run main.py`

You can use a gradio interface to transcribe an audio file.

1. Finds the next available temporary MP3 filename.
2. Converts the input audio file to MP3 format at 64 kbps.
3. Sends the MP3 file to the OpenAI transcription API.
4. Provides resulting transcription for download.

## How to set your API key?

Use the Gradio interface.