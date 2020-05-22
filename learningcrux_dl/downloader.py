from youtube_dl import YoutubeDL
import os
import re

def download(course, title):
    title = re.sub(r'[^\w\-_\. ]', '_', title)
    if os.path.exists(title) == False:
        os.mkdir(title)
    index = 0
    for section in course:
        index += 1
        if os.path.exists(os.path.join(title, section['section'])) == False:
            os.mkdir(os.path.join(title, section['section']))
        print(f"[learningcrux] Section {index}: {section['section']}")
        video_count = 0
        for video in section['videos']:
            video_count += 1
            print(f"[learningcrux] Title: {str(video_count)}. {video['title']}")
            with YoutubeDL({ 'outtmpl': os.path.join(title, section['section'], str(video_count) + ". " + video['title']) + '.mp4' }) as ytdl:
                ytdl.download([video['url']])
                
                
                

