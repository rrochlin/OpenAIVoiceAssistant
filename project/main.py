import openai
import asyncio
import whisper
from pydub import playback, AudioSegment
import speech_recognition as sr
from gtts import gTTS
from configparser import ConfigParser
from pathlib import Path
from os import remove


def play_audio(filepath: Path):
    sound = AudioSegment.from_file(filepath, format="mp3")
    playback.play(sound)


async def main():
    # Initialize the OpenAI API
    config = ConfigParser()
    home = Path(__file__).parent.resolve()
    config.read(Path(home.parent.resolve(), "private.config"))
    openai.api_key = config["SECRETS"]["api_key"]
    question_audio_file = Path(home, "tmp", "question.mp3")
    response_audio_file = Path(home, "tmp", "response.mp3")

    # Create a recognizer object and wake word variables
    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 1
    while True:
        with sr.Microphone() as source:
            input("Press ENTER to begin")
            recognizer.adjust_for_ambient_noise(source)
            print("Recording Question\n")
            audio = recognizer.listen(source)

        with open(question_audio_file, "wb") as f:
            f.write(audio.get_wav_data())

        model = whisper.load_model("tiny.en")
        result = model.transcribe(audio=question_audio_file.__str__(), fp16=False)
        remove(question_audio_file)
        question = result["text"]
        if question.lower() == "quit":
            break
        print("You asked : ", question, "\n")
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=[
                {"role": "system", "content": "keep responses short"},
                {"role": "user", "content": question}]
        )
        print(completion.choices[0].message.content)
        tts = gTTS(completion.choices[0].message.content)
        tts.save(response_audio_file)
        play_audio(response_audio_file)
        remove(response_audio_file)

if __name__ == "__main__":
    asyncio.run(main())
