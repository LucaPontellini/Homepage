from datetime import date

class User:
    def __init__(self, username: str, email: str, password: str, profile: str):
        self.username = username
        self.email = email
        self.password = password
        self.profile = profile
        self.photos = []
        self.albums = []
        self.following = []

    def __str__(self):
        return f"Username: {self.username}, Email: {self.email}, Profile: {self.profile}"

    def register(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.password = password

    def create_profile(self):
        self.profile = input("Enter your profile: ")

    def upload_photo(self, photo):
        self.photos.append(photo)

    def follow_user(self, user):
        self.following.append(user)

    def create_album(self, album):
        self.albums.append(album)

class Photo:
    def __init__(self, id: str, title: str, description: str, upload_date: date, user: User, album: 'Album'):
        self.id = id
        self.title = title
        self.description = description
        self.upload_date = upload_date
        self.user = user
        self.album = album
        self.comments = []

    def __str__(self):
        return f"ID: {self.id}, Title: {self.title}, Description: {self.description}, Upload Date: {self.upload_date}, User: {self.user.username}, Album: {self.album.title}"

    def add_comment(self, comment):
        self.comments.append(comment)

class Album:
    def __init__(self, title: str, description: str, user: User):
        self.title = title
        self.description = description
        self.user = user
        self.photos = []

    def add_photo(self, photo: Photo):
        self.photos.append(photo)

    def __str__(self):
        return f"Title: {self.title}, Description: {self.description}, User: {self.user.username}"

class Comment:
    def __init__(self, author: User, photo: Photo, content: str, date: date):
        self.author = author
        self.photo = photo
        self.content = content
        self.date = date

    def __str__(self):
        return f"Author: {self.author.username}, Photo: {self.photo.title}, Content: {self.content}, Date: {self.date}"
    
def main():
    user1 = User(username="alice", email="alice@gmail.com", password="password123", profile="Alice's profile")
    user2 = User(username="bob", email="bob@gmail.com", password="password456", profile="Bob's profile")

    album1 = Album(title="Holidays", description="Vacation photos", user=user1)
    album2 = Album(title="Events", description="Photos of the events", user=user2)

    photo1 = Photo(id="1", title="Spiaggia", description="Photos of the beach", upload_date=date.today(), user=user1, album=album1)
    photo2 = Photo(id="2", title="Concerto", description="Photos of the concert", upload_date=date.today(), user=user2, album=album2)

    album1.add_photo(photo1)
    album2.add_photo(photo2)

    comment1 = Comment(author=user2, photo=photo1, content="Nice picture!", date=date.today())
    comment2 = Comment(author=user1, photo=photo2, content="Sounds fun!", date=date.today())

    photo1.add_comment(comment1)
    photo2.add_comment(comment2)

    print(user1)
    print(user2)
    print(album1)
    print(album2)
    print(photo1)
    print(photo2)
    print(comment1)
    print(comment2)

if __name__ == "__main__":
    main()