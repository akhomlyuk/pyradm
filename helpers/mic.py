from aiogram import Router
from aiogram.types import Message, FSInputFile
from aiogram.filters.command import Command
import pyaudio
import wave
import logging
from sys import platform
import os

router: Router = Router()

if platform == "win32":
    path = os.path.expanduser('~') + r'\mic.wav'
else:
    path = os.path.expanduser('~') + r'/mic.wav'


@router.message(Command("mic"))
async def cmd_mic(message: Message):
    try:
        args = message.text.split(' ')
        if len(args) == 2:
            audio_format = pyaudio.paInt16
            channels = 1
            rate = 44100
            chunk = 1024
            record_seconds = int(args[1])

            audio = pyaudio.PyAudio()
            stream = audio.open(format=audio_format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk)
            frames = []

            for _ in range(0, int(rate / chunk * record_seconds)):
                data = stream.read(chunk)
                frames.append(data)

            stream.stop_stream()
            stream.close()
            audio.terminate()

            wave_file = wave.open(path, 'wb')
            wave_file.setnchannels(channels)
            wave_file.setsampwidth(audio.get_sample_size(audio_format))
            wave_file.setframerate(rate)
            wave_file.writeframes(b''.join(frames))
            wave_file.close()

            mic_file = FSInputFile(path)

            await message.answer_audio(mic_file)
        else:
            await message.answer(f"Usage: /mic 10\nSeconds int value")
    except Exception as e:
        logging.error(e)
