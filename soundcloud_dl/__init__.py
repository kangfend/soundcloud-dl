import argparse
import os
import requests

from soundcloud_dl import SoundCloud


def main():
    parser = argparse.ArgumentParser(description='Soundcloud downloader')
    parser.add_argument('link', nargs='?', help='soundcloud link')
    parser.add_argument('-o', '--output')
    args = parser.parse_args()
    if args.link:
        try:
            soundcloud = SoundCloud(args.link, output=args.output)
            print '[+] Trying to download file...'
            soundcloud.download_mp3()
            path = os.path.join(soundcloud.output, soundcloud.get_title())
            print '[+] Download completed, file saved to "{0}.mp3"'.format(path)
        except requests.exceptions.ConnectionError:
            print '[-] Download failed, please check your connection!'
        except KeyboardInterrupt:
            print '\b\b[!] Download aborted!'
    else:
        print parser.print_help()
