#!/usr/bin/env python

import os
import re
import requests


class SoundCloud:
    def __init__(self, url, output=None):
        self.url = url
        self.page = requests.get(self.url).content
        self.output = os.path.abspath(output if output else '.')

    def get_track_id(self):
        track_id = re.search(r'https://api.soundcloud.com/tracks/(\d+)', self.page)
        if track_id:
            return track_id.groups()[0]
        raise ValueError()

    def get_client_id(self):
        app_js = re.search(r'https://a-v2.sndcdn.com/assets/app-([a-z0-9-]+).js', self.page)
        if app_js:
            app_js_response = requests.get(app_js.group()).text
            client_id = re.search(r'query:{client_id:"(\w+)"}', app_js_response)
            if client_id:
                return client_id.groups()[0]
        raise ValueError()

    def get_title(self):
        title = re.search(r'property="og:title" content="(.*?)"', self.page)
        if title:
            return title.groups()[0]
        raise ValueError()

    def prepare(self):
        self.client_id = self.get_client_id()
        self.track_id = self.get_track_id()
        self.title = self.get_title()

    def download_mp3(self):
        self.prepare()
        media_file = requests.get(
            'https://api.soundcloud.com/tracks/{0}/stream?client_id={1}'
            .format(self.track_id, self.client_id)
        ).content
        path = os.path.join(self.output, self.get_title())
        with open('{0}.mp3'.format(path), 'wb') as mp3:
            mp3.write(media_file)
