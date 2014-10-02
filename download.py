__author__ = 'karunab'

import os
import urllib2


class Downloadable:
    def __init__(self, path_on_disk, url):
        self.path_on_disk = path_on_disk
        self.url = url

    @staticmethod
    def from_wallpaper(base_path, wallpaper):
        file_name = os.path.basename(wallpaper.url)
        path_on_disk = '%s/%s' % (base_path, file_name)

        return Downloadable(path_on_disk, wallpaper.url)

    def __str__(self):
        return "Download: %s -> %s" % (self.url, self.path_on_disk)


def perform_download(downloadable):
    if not os.path.exists(os.path.dirname(downloadable.path_on_disk)):
        os.makedirs(os.path.dirname(downloadable.path_on_disk))

    if os.path.exists(downloadable.path_on_disk):
        print "%s already exists. Skipping download" % downloadable.path_on_disk
        return

    print "Starting download for %s" % downloadable.url
    with open(downloadable.path_on_disk, 'w+') as f:
        try:
            f.write(urllib2.urlopen(downloadable.url).read())
        except urllib2.HTTPError:
            f.write('Error in writing %s' % downloadable.__url)
            return downloadable, False

    print "Ending download for %s" % downloadable.url
    return downloadable, True