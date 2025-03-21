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
    def __init__(self, name: str, email: str, password: str, subscription: float):
        self.name = name
        self.email = email
        self.password = password
        self.subscription = subscription

    def create_different_playlists(Playlist: list[str]): list[str]
    def leave_comments(Video: video): str