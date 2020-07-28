from youtube_dl import YoutubeDL
import os
import re


def download(course, course_title, output):
    if not output:
        output = os.getcwd()

    course_title = re.sub(r'[^\w\-_\. ]', '_', course_title)

    for index, section in enumerate(course, 1):
        section_dir = os.path.join(output, course_title, f"{index}. {section['section']}")
        if not os.path.exists(section_dir):
            os.makedirs(section_dir)
        print(f'[learningcrux] Section {index}: {section["section"]}')

        for video_count, video in enumerate(section['videos'], 1):
            video_title = f'{video_count}. {video["title"]}.mp4'
            print(f'[learningcrux] title: {video_title[:-4]}')

            with YoutubeDL({'outtmpl': os.path.join(section_dir, video_title)}) as ytdl:
                ytdl.download([video['url']])
