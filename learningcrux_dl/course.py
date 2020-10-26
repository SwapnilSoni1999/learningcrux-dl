import requests
from bs4 import BeautifulSoup
import re


class Course:
    def __init__(self, course_url):
        supported_sites = ('learningcrux.com', 'freetutorials.ca')

        if not any(site in course_url for site in supported_sites):
            print("Not a learningcrux or freetutorials url!")
            exit()

        self.title = ''
        self.course_url = course_url
        self.data = []
        headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/81.0.4044.138 Safari/537.36'
        }
        res = requests.get(course_url, headers=headers)
        self.soup = BeautifulSoup(res.content, 'lxml')

        if 'freetutorials.ca' in course_url:
            self.process_freetutorials()

        elif 'learningcrux.com' in course_url:
            self.process_learningcrux()

    def process_freetutorials(self):
        sections = self.soup.find_all('div', {'class': 'list-brief-content__item'})

        self.title = self.soup.select_one('.bundle-header__about > h1').text.strip()

        print(f'[Course] {self.title}')
        print("[learningcrux] Building course json data...")

        for section in sections:
            section_title = get_section_title(section.find('div', {'class': 'list-brief__top__title'}))
            videos = self.get_videos(section)

            data = {'section': section_title, 'videos': videos}
            self.data.append(data)

    def process_learningcrux(self):
        sections = self.soup.find_all('section', {'class': 'sectionRow'})
        self.title = self.soup.select_one('#content > h1').text.strip()

        print(f'[Course] {self.title}')
        print("[learningcrux] Building course json data...")

        for section in sections:
            section_title = get_section_title(section.find('h2', {'class': 'rowHeading'}))
            videos = self.get_videos(section)

            data = {'section': section_title, 'videos': videos}
            self.data.append(data)

    def get_videos(self, section):
        if 'freetutorials.ca' in self.course_url:
            return get_freetutorials_videos(section)
        elif 'learningcrux.com' in self.course_url:
            return get_learningcrux_videos(section)
        else:
            print('Unknown Error Occurred!')
            exit()


def get_freetutorials_videos(section):
    videos = []
    new_sec = section.find('div', {'class': 'list-brief__list'})

    for vid_raw in new_sec.find_all('div', {'class': 'list-brief__item'}):
        video_title = vid_raw.find('a', {'class': 'list-brief__item__content'})
        video_title = video_title.text.strip()

        relative_link = vid_raw.find('a', {'class': 'list-brief__item__content'})['href'].replace('play', 'video')
        video_link = 'https://learningcrux.com' + relative_link

        data = {'title': video_title, 'url': video_link}
        videos.append(data)
    return videos


def get_learningcrux_videos(section):
    videos = []
    for vid_raw in section.find_all('div', {'class': ['panel', 'panel-default']}):
        video_title = vid_raw.find('span', {'class': 'accOpenerCol'})
        for i in video_title.find_all('i'):
            i.decompose()
        video_title.find('span').decompose()
        video_title = video_title.text.strip()

        relative_link = vid_raw.find('a')['href'].replace('video', 'play')
        video_link = 'https://learningcrux.com' + relative_link

        data = {'title': video_title, 'url': video_link}
        videos.append(data)

    return videos


def get_section_title(title):
    title = title.text.replace('\n', '')
    section_title = re.sub(r"Section \d{0,3}:", '', title)

    # sanitize
    section_title = re.sub(r"[-]{2,}", '', section_title)

    return section_title.strip()
