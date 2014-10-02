import multiprocessing

__author__ = 'karunab'

from resolution import Resolution

from download import Downloadable, perform_download
from display import get_resolution
from desktoppr import Desktoppr


def add_to_downloads_queue():
    is_first = True
    while desktoppr.has_next() and (is_first or not desktoppr.should_break()):
        is_first = False

        print "Fetching page %d" % desktoppr.get_next_page_no()
        for wallpaper in desktoppr.next(screen):
            downloads.append(Downloadable.from_wallpaper(base_path_on_disk, wallpaper))


def process_downloads():
    pool = multiprocessing.Pool(processes=5)  # use 5 processes to download the data
    return pool.map(perform_download, downloads)


## Main code
screen = Resolution.from_tuple(get_resolution())
print "Screen details: %s\n" % screen

start_page = 1
page_break_at = 5
desktoppr = Desktoppr(start_page, page_break_at)

downloads = list()
base_path_on_disk = '/Users/karunab/Pictures/Wallpapers/%s' % screen
while desktoppr.has_next():
    add_to_downloads_queue()
    process_downloads()