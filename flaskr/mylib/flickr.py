import requests
import yaml as yaml

class Flickr(object):
    def __init__(self):
        self.base_url = 'https://api.flickr.com/services/rest/'
        with open("../../config.yml", 'r') as stream:
            self.config = yaml.load(stream)
            
        self.key = self.config['api']['key']
        self.secret = self.config['api']['key']

    def send_request(self, method, args):
        full_url = self.base_url + '?method={method}&api_key={key}&{args}'.format(method=method, key=self.key, args=args)
        print(full_url)
        r = requests.get(full_url, auth=('user', 'pass'))
        
        return r

    def get_photos(self, person):
        r = self.send_request(method='flickr.people.getPhotos', args='user_id={person}'.format(person=person))

        return r


flickr = Flickr()
r = flickr.get_photos('robertbjork')
print(r.text)