from anyblok.blok import Blok


class TestBlok(Blok):

    version = '1.0.0'

    required = [
        'test-blok2',
    ]