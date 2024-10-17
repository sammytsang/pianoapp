import pyaudio
import requests
from io import BytesIO
from loguru import logger

# Constants
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024 * 4
API_TOKEN = "9be264eef7f3e6259a7d2117d0b6d766"
RECOGNITION_URL = "https://api.audd.io/"

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open stream
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

audio_file_path = "song.mp3"

try:
    while True:
        # data = stream.read(CHUNK, exception_on_overflow=False)
        # print(data)
        files = {'file': open(audio_file_path, 'rb')}
        data = {'api_token': API_TOKEN, 'return': 'apple_music,spotify'}
        response = requests.post(
            RECOGNITION_URL,
            data=data,
            files=files,
            stream=True
        )
        logger.info(response.text)  # Print raw API response for testing
        exit()

except KeyboardInterrupt:
    print("\nStopping...")

finally:
    stream.stop_stream()
    stream.close()
    audio.terminate()
