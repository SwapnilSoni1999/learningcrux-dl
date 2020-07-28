from .course import Course
from .downloader import download
import click


@click.command()
@click.option("-u", "--url", required=True, prompt="Please Enter the Url to Download",
              help="Course Url link eg. https://www.learningcrux.com/course/the-complete-2020-web-development-bootcamp")
@click.option("-o", "--output", help="[optional] The output Path where the material will be downloaded")
def lcx(url, output):
    course = Course(url)
    download(course.data, course.title, output)
