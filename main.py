import os
import ffmpeg
import gradio as gr
from openai import OpenAI

def find_next_available_filename(base_name, extension):
  """
  Checks for the existence of sequentially numbered filenames and returns the next available one.

  Args:
    base_name: The base filename without the number and extension (e.g., "temp").
    extension: The file extension (e.g., "mp3").

  Returns:
    The next available filename (e.g., "temp0002.mp3") if found, otherwise returns None.
  """

  i = 1
  while True:
    filename = f"{base_name}{i:04d}.{extension}"  # Format number with leading zeros
    if not os.path.exists(filename):
      return filename
    i += 1
    if i > 9999:  # Prevent infinite loop if all possible filenames are taken.  Adjust as needed.
      return None # Or raise an exception - depends on the use case.

def save_transcription_to_file(transcription, original_mp3_filename):
  """
  Saves the transcription text to a .txt file with the same name as the original .mp3 file.

  Args:
    transcription: The text transcription to save.
    original_mp3_filename: The name of the original .mp3 file.

  Returns:
    True if the file was saved successfully, False otherwise.
  """
  try:
    # Extract the base filename without the extension
    base_name = os.path.splitext(original_mp3_filename)[0]

    # Construct the .txt filename
    txt_filename = base_name + ".txt"

    # Write the transcription to the .txt file
    with open(txt_filename, "w", encoding="utf-8") as f:  # Use utf-8 encoding for broader character support
      f.write(transcription)

    return txt_filename  # Indicate success

  except Exception as e:
    print(f"Error saving transcription to file: {e}")
    return False  # Indicate failure

def update(audio):
    sr, data = audio
    file = audio.value
    return ("Hello World!")

def process_file(fileobj):
    # 1. convert to mp3
    path = "./" + find_next_available_filename("temp", "mp3")
    # using ffmpeg to convert to an MP3 with 64 kbps
    stream = ffmpeg.input(fileobj.name)
    stream = ffmpeg.output(stream, path, audio_bitrate=64*1024)
    ffmpeg.run(stream)
    # 2. Use 
    audio_file= open(path, "rb")

    # starting the transcription
    client = OpenAI()

    transcription = client.audio.transcriptions.create(
        model="gpt-4o-mini-transcribe", 
        file=audio_file
    )
    return save_transcription_to_file(transcription=transcription.text, original_mp3_filename=path)

with gr.Blocks() as demo:
    upload_button = gr.UploadButton("Click to Upload a File", file_types=["audio"], file_count="single")
    file_output = gr.File()
    upload_button.upload(process_file, upload_button, file_output)


if __name__ == "__main__":
    demo.launch()


