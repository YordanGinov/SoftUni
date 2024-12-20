from project.album import Album


class Band:
    def __init__(self, name: str) -> None:
        self.name = name
        self.albums: list[Album] = []

    def add_album(self, album: Album) -> str:
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str) -> str:
        try:
            current_album = [el for el in self.albums if el.name == album_name][0]
            if current_album.published:
                return f"Album has been published. It cannot be removed."
            self.albums.remove(current_album)
            return f"Album {current_album.name} has been removed."
        except IndexError:
            return f"Album {album_name} is not found."

    def details(self) -> str:
        result = f"Band {self.name}\n"
        for album in self.albums:
            result += f"{album.name}\n"
        return result