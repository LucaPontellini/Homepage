from datetime import date

class User:
    def __init__(self, username: str, email: str, password: str, profile: str):
        self.username = username
        self.email = email
        self.password = password
        self.profile = profile
    
    def __str__(self):
        return f"Username {self.username}, email {self.email}, password {self.password}, profile {self.profile}"
    
    def register(self, username: str, email: str, password: str):
        pass

    def create_a_profile(self):
        pass

    def upload_photo(self):
        pass

    def follow_other_users(self):
        pass

    def create_albums(self):
        pass

class Photo:
    def __init__(self, id: str, title: str, description: str, upload_date: date, user: User, album: Album):
        self.id = id
        self.title = title
        self.description = description
        self.upload_date = upload_date
        self.user = user
        self.album = album
    
    def __str__(self):
        return f"Id {self.id}, title {self.title}, description {self.description}, upload_date {self.upload_date}, user {self.user}, album {self.album}"
    
class Album:
    def __init__(self, title: str, description: str, user: User, photo: Photo):
        self.title = title
        self.description = description
        self.user = User
        self.photo = Photo

class Comments:
    def __init__(self, author: User, lease: Photo):
        self.author = author
        self.lease = lease