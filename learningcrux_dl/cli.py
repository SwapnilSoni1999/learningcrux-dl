from learningcrux_dl.course import Course
from learningcrux_dl.downloader import download
import click

@click.command()
@click.option("-u", "--url", required=True, prompt="Please Enter the Url to Download: ", help="The url to download")
@click.option("-o", "--output", help="[optional] The output Path where the material will be downloaded")
def lcx(url, output):
    if output:
        print(output)
    course = Course(url)
    download(course.getData(), course.title)
