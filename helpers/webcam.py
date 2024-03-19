from aiogram import Router
from aiogram.types import Message, FSInputFile
from aiogram.filters.command import Command
import logging
import cv2
import os
from sys import platform

router: Router = Router()


@router.message(Command("webcam"))
async def cmd_webcam(message: Message):
    try:
        if platform == "win32":
            path = os.path.expanduser('~') + r'\\'
        else:
            path = os.path.expanduser('~') + r'/'

        args = message.text.split(' ')

        if len(args) == 1:
            path = f'{path}cam.jpg'
            cap = cv2.VideoCapture(0)
            if cap.isOpened():
                ret, frame = cap.read()
                cv2.imwrite(path, frame)
                photo = FSInputFile(path)
                await message.answer_photo(photo)
                cap.release()
                os.remove(path)
            else:
                await message.answer(f'No camera detected')
        elif len(args) == 2:
            path = path + 'cam.avi'
            cap = cv2.VideoCapture(0)
            if cap.isOpened():
                codec = cv2.VideoWriter_fourcc(*'XVID')
                out = cv2.VideoWriter(path, codec, 30.0, (640, 480))
                for _ in range(int(args[1]) * 30):
                    ret, frame = cap.read()
                    if ret:
                        out.write(frame)
                video = FSInputFile(path)
                await message.answer_video_note(video)
                await message.answer_video(video)
                cap.release()
                out.release()
                os.remove(path)
            else:
                await message.answer('No camera detected')
        else:
            await message.answer(f'/webcam or /webcam 10\nTime in seconds')
        cv2.destroyAllWindows()
    except ValueError:
        await message.answer(f'Argument must be in integer. Value in seconds\n/webcam 10')
    except Exception as e:
        logging.error(e)
