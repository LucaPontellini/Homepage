from datetime import datetime

class Platform:
    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type
        self.profiles = []
        self.videos = []
        self.playlists = []
        self.subscriptions = []
        self.comments = []

    def manages_profile(self, profile):
        self.profiles.append(profile)

    def manages_video(self, video):
        self.videos.append(video)

    def manages_playlist(self, playlist):
        self.playlists.append(playlist)

    def manages_subscription(self, subscription):
        self.subscriptions.append(subscription)

    def manages_comment(self, comment):
        self.comments.append(comment)

class Profile:
    def __init__(self, name: str, email: str, password: str, subscription, videos_viewed: list):
        self.name = name
        self.email = email
        self.password = password
        self.subscription = subscription
        self.videos_viewed = videos_viewed
        self.playlists = []

    def create_different_playlists(self, playlist_name: str):
        playlist = Playlist(name=playlist_name, creator=self.name)
        self.playlists.append(playlist)
        return playlist

    def add_videos_to_playlist(self, playlist, video):
        if playlist in self.playlists:
            playlist.add_videos(video)

    def remove_videos_from_playlist(self, playlist, video):
        if playlist in self.playlists:
            playlist.remove_videos(video)

    def delete_playlist(self, playlist):
        if playlist in self.playlists:
            self.playlists.remove(playlist)

    def leave_comments(self, video, comment_text: str):
        comment = Comment(author=self.name, text=comment_text, date_of_publication=datetime.now())
        video.add_comments(comment)
        return comment

class Video:
    def __init__(self, title: str, description: str, url: str, duration: datetime):
        self.title = title
        self.description = description
        self.url = url
        self.duration = duration
        self.views = 0
        self.comments = []

    def add_comments(self, comment):
        self.comments.append(comment)

    def increment_views(self):
        self.views += 1

class Playlist:
    def __init__(self, name: str, creator: str):
        self.name = name
        self.creator = creator
        self.videos = []

    def add_videos(self, video):
        self.videos.append(video)

    def remove_videos(self, video):
        if video in self.videos:
            self.videos.remove(video)

class Subscription:
    def __init__(self, type: str, price: float, start_date: datetime, end_date: datetime):
        self.type = type
        self.price = price
        self.start_date = start_date
        self.end_date = end_date

class Comment:
    def __init__(self, author: str, text: str, date_of_publication: datetime):
        self.author = author
        self.text = text
        self.date_of_publication = date_of_publication

if __name__ == "__main__":
    platform = Platform(name="Youtube", type="video-sharing")

    subscription = Subscription(type="Premium", price=9.99, start_date=datetime(2025, 3, 1), end_date=datetime(2026, 3, 1))

    profile = Profile(name="Alice", email="alice@example.com", password="securepassword123", subscription=subscription, videos_viewed=[])
    platform.manages_profile(profile)

    video1 = Video(title="Python Tutorial", description="Learn Python programming.", url="https://youtu.be/python_tutorial", duration=datetime(2025, 3, 21, 1, 0))
    video2 = Video(title="Data Science Basics", description="Introduction to Data Science.", url="https://youtu.be/data_science_basics", duration=datetime(2025, 3, 21, 0, 45))
    platform.manages_video(video1)
    platform.manages_video(video2)

    video1.increment_views()
    video1.increment_views()
    video2.increment_views()

    playlist = profile.create_different_playlists("Python Lessons")
    profile.add_videos_to_playlist(playlist, video1)
    profile.add_videos_to_playlist(playlist, video2)

    profile.remove_videos_from_playlist(playlist, video2)

    comment = profile.leave_comments(video1, "Great lesson! Thank you so much!")
    platform.manages_comment(comment)

    print(f"Platform: {platform.name}, Type: {platform.type}")
    print(f"User: {profile.name}, Email: {profile.email}")
    print(f"Subscription: {profile.subscription.type}, Price: {profile.subscription.price}")
    print(f"Playlist: {playlist.name}, Videos in playlist: {[v.title for v in playlist.videos]}")
    print(f"Video \"{video1.title}\" has {video1.views} views and {len(video1.comments)} comment(s).")
    print(f"Comment by {comment.author}: \"{comment.text}\" published on {comment.date_of_publication}")