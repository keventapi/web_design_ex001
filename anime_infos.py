import requests
class API_USAGE():
    def __init__(self, user=''):
        self.CLIENT_ID = 'e29fe4120a686914b88e4b23a1e41bf9'
        self.user = user
        self.data = {}
        self.formated_request = []

    def start(self):
          self.get_all_anime_watched()
          self.get_anime_name()
          return self.data

    def get_all_anime_watched(self):
            url = f"https://api.myanimelist.net/v2/users/{self.user}/animelist?status=completed&limit=1000"
            response = requests.get(url, headers = {'X-MAL-CLIENT-ID': self.CLIENT_ID})
            response .raise_for_status()
            watched_animes = response.json()
            response.close()
            self.format_data(watched_animes)

    def format_data(self, data):
            for i in data['data']:
                self.formated_request.append(i['node'])

    def get_anime_name(self):
            for i in self.formated_request:
                  self.data[str(i['id'])] = {'title': i['title']}
                  self.get_anime_main_image(i)
         
    def get_anime_main_image(self, id):
          image = id['main_picture']['medium']
          self.data[str(id['id'])]['image'] = image

    def get_anime_sinopse(self, id):
        url = f"https://api.myanimelist.net/v2/anime/{id}?fields=synopsis"
        response = requests.get(url, headers = {'X-MAL-CLIENT-ID': self.CLIENT_ID})
        response .raise_for_status()
        anime_info = response.json()
        response.close()
        return anime_info['synopsis']
