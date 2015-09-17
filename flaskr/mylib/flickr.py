import requests
import yaml as yaml
import xml.etree.ElementTree as ET


class Flickr(object):
    def __init__(self):
        self.base_url = 'https://api.flickr.com/services/rest/'
        with open("../config.yml", 'r') as stream:
            self.config = yaml.load(stream)
            
        self.key = self.config['api']['key']
        self.secret = self.config['api']['key']
        self.farm = self.config['api']['farm']
        self.server_id = self.config['api']['server_id']

    def send_request(self, method, args):
        full_url = self.base_url + '?method={method}&api_key={key}&{args}'.format(method=method, key=self.key, args=args)
        r = requests.get(full_url, auth=('user', 'pass'))
        
        return r

    def get_photos(self, person, page, per_page, size):
        urls = []
        r = self.send_request(method='flickr.people.getPhotos', args='user_id={person}&page={page}&per_page={per_page}'\
        .format(person=person, page=page, per_page=per_page))

        root = ET.fromstring(r.text)

        for child in root.getchildren():
            for photo in child.getchildren():
                url = 'https://farm{farm}.staticflickr.com/{server_id}/{photo_id}_{secret}_{size}.jpg'

                id = photo.attrib['id']
                secret = photo.attrib['secret']
                server = photo.attrib['server']
                title = photo.attrib['title']

                urls.append(url.format(farm=self.farm, server_id=server, photo_id=id, secret=secret, size=size))

        return urls