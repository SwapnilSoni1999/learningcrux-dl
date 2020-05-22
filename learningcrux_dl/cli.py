from learningcrux_dl.course import Course
from learningcrux_dl.downloader import download
import argparse

def lcx():
    args = argparse.ArgumentParser()
    args.add_argument('--url', required=True)
    args.add_argument('--output')
    
    arguments = args.parse_args()
    url = arguments.url
    output = arguments.output

    if output:
        print(output)

    course = Course(url)
    download(course.getData(), course.title)
