from io import BytesIO
import requests
from pathlib import Path

class LocalImage:
    """파일로부터 이미지를 얻음"""

    def __init__(self, path):
        self._path = path

    def get_image(self):
        return open(self._path, mode='rb')

class RemoteImage:
    """URL로부터 이미지를 얻음"""

    def __init__(self, path):
        self._url = path

    def get_image(self):
        data = requests.get(self._url)
        # 바이트 데이터를 파일 객체로 변환
        return BytesIO(data.content)        

class _LoremFlickr(RemoteImage):
    """검색 키워드로부터 이미지를 얻음"""
    LOREM_FLICKR_URL = 'https://loremflickr.com'
    WIDTH = 800
    HEIGHT = 600

    def __init__(self, keyword):
        super().__init__(self._build_url(keyword))

    def _build_url(self, keyword):
        return (f'{self.LOREM_FLICKR_URL}/'
                f'{self.WIDTH}/{self.HEIGHT}/{keyword}')

class _LoremPicsum(RemoteImage):
    """검색 키워드로부터 이미지를 얻음"""
    LOREM_PICSUM_URL = 'https://picsum.photos'
    WIDTH = 300
    HEIGHT = 400

    def __init__(self):
        super().__init__(self._build_url())

    def _build_url(self):
        return (f'{self.LOREM_PICSUM_URL}/'
                f'{self.WIDTH}/{self.HEIGHT}')


KeywordImage = _LoremFlickr    
KeywordImage2 = _LoremPicsum    

def ImageSource(keyword):
    """ghgjhg
    """
    if keyword.startswith(('http://', 'https://')):
        return RemoteImage(keyword)
    elif Path(keyword).exists():
        return LocalImage(keyword)
    else:
        # return KeywordImage2()
        return KeywordImage(keyword)


def get_image(keyword):
    """hgjhgj
    """
    return ImageSource(keyword).get_image()