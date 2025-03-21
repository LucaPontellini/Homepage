class Platform:
    def __init__(self, name: str, type: str):
            self.name = name
            self.type = type

    def manages_profile(Profile: profile):
        pass
    def manages_video(Video: video):
        pass
    def manages_playlist(Playlist: playlist):
        pass
    def manages_subscription(Subscription: subscription):
        pass
    def manages_comment(Comment: comment):
        pass

class Profile:
    def __init__(self, name: str, email: str, password: str, subscription: Subscription, videos_viewed: list[Video]):
        pass
    def create_different_playlists(Playlist: list[str]):
        pass
    def add_videos_to_playlist(Playlist: playlist, Video: video):
        pass
    def remove_videos_from_playlist(Playlist: playlist, Video: video):
        pass
    def delete_playlist(Playlist: playlist):
        pass
    def leave_comments(Video: video, Comment: comment):
        pass
class Video:
    def __init__(self, title: str, description: str, url: str, duration: datetime, views: int):
        self.title = title
        self.description = description
        self.url = url
        self.duration = duration
        self.views = views
    def add_comments(Comment: comment):
        pass

class Playlist:
    def __init__(self, name: str, creator: str):
        self.name = name
        self.creator = creator

    def add_videos(Video: video):
        pass
    def remove_videos(Video: video):
        pass