class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [pages * []]

    @classmethod
    def from_photos_count(cls, photos_count):
        pass
