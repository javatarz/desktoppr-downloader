import os

__author__ = 'karunab'
import urllib
import json

from resolution import Resolution


class Desktoppr:
    def __init__(self, next, page_break_count):
        self.__next = next
        self.__page_break_count = page_break_count
        self.__url = 'https://api.desktoppr.co/1/wallpapers?page=%d'

    def __get_images(self):
        response = urllib.urlopen(self.__url % self.__next)
        data = json.loads(response.read())
        images = list()

        for wallpaper in data['response']:
            image_resolution = Resolution(wallpaper['width'], wallpaper['height'])
            wallpaper_url = wallpaper['image']['url']

            images.append(Wallpaper(image_resolution, wallpaper_url))

        self.__next = data['pagination']['next']

        return images

    def next(self, screen_resolution):
        usable_images = list()
        for image in filter(lambda x: x.resolution.__ge__(screen_resolution), self.__get_images()):
            usable_images.append(image)

        return usable_images

    def has_next(self):
        return self.__next is not None

    def should_break(self):
        return self.__next % self.__page_break_count == 1

    def get_next_page_no(self):
        return self.__next


class Wallpaper:
    def __init__(self, image_resolution, image_url):
        self.resolution = image_resolution
        self.url = image_url

    def __str__(self):
        return "%s || URL: %s" % (self.resolution, self.url)