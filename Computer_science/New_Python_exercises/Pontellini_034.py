import datetime

class User:
    def __init__(self, user_id: str, username: str, email: str, projects: list['MusicalProject']):
        self._user_id = user_id
        self._username = username
        self._email = email
        self._projects = projects

    def create_project(self, title: str) -> 'MusicalProject':
        project = MusicalProject(project_id="p1", project_title=title, creation_date=datetime.date.today(), musical_genre="", tracks=[])
        self._projects.append(project)
        return project
    
    def projects_by_genre(): dict[str, int]

    def count_total_projects(): int
    def most_used_instrument(): VirtualInstrument

class MusicalProject:
    def __init__(self, project_id: str, project_title: str, creation_date: datetime.date, musical_genre: str, tracks: list['AudioTrack']):
        self._project_id = project_id
        self._project_title = project_title
        self._creation_date = creation_date
        self._musical_genre = musical_genre
        self._tracks = tracks

    def add_track(track_name: str): AudioTrack
    def percentage_of_tracks_with_effects(): float
    def most_used_effect(): EffectType

class AudioTrack:
    def __init__(self, track_id: str, track_name: str, duration_seconds: float, volume_db: int, manual_note_sequence: str, used_instrument: 'VirtualInstrument', applied_effects: list['AudioEffect']):
        self._track_id = track_id
        self._track_name = track_name
        self._duration_seconds = duration_seconds
        self._volume_db = volume_db
        self._manual_note_sequence = manual_note_sequence
        self._used_instrument = used_instrument
        self._applied_effects = applied_effects

    def add_instrument(instrument: 'VirtualInstrument'): None
    def apply_effect(effect: 'AudioEffect'): None
    def remove_effect(effect: 'AudioEffect'): None
    def set_note_sequence(notes: str): None
    def modify_volume(new_volume_db: int): None
    def has_effects(): bool
    def number_of_notes(): int

class VirtualInstrument:
    def __init__(self, instrument_id: str, instrument_name: str, instrument_type: 'InstrumentType'):
        self._instrument_id = instrument_id
        self._instrument_name = instrument_name
        self._instrument_type = instrument_type
    
    def play_note(note: str, duration: float): None

class AudioEffect:
    def __init__(self, effect_id: str, effect_name: str, effect_type: 'EffectType'):
        self._effect_id = effect_id
        self._effect_name = effect_name
        self._effect_type = effect_type

class InstrumentType:
    GUITAR = "Guitar"
    BASS = "Bass"
    DRUMS = "Drums"

class EffectType:
    DISTORTION = "Distortion"
    DELAY = "Delay"
    REVERB = "Reverb"

# Example usage
if __name__ == "__main__":
    # User creation
    user = User("u1", "Mario Rossi", "mario@example.com")  # type: ignore # noqa: F821

    # Project creation
    rock_project = user.create_project("My Rock Song")
    rock_project.music_genre = "Rock"
    
    jazz_project = user.create_project("Jazz Session")
    jazz_project.music_genre = "Jazz"

    # Adding tracks to the rock project
    bass_track = rock_project.add_track("Bass Line")
    guitar_track = rock_project.add_track("Rhythm Guitar")

    # Creating and adding instruments
    bass = VirtualInstrument("s1", "Electric Bass", InstrumentType.BASS)  # type: ignore # noqa: F821
    guitar = VirtualInstrument("s2", "Electric Guitar", InstrumentType.GUITAR)  # type: ignore # noqa: F821
    
    bass_track.add_instrument(bass)
    guitar_track.add_instrument(guitar)

    # Adding effects
    distortion = AudioEffect("e1", "Heavy Distortion", EffectType.DISTORTION)  # type: ignore # noqa: F821
    delay = AudioEffect("e2", "Delay Echo", EffectType.DELAY)  # type: ignore # noqa: F821
    
    bass_track.apply_effect(distortion)
    guitar_track.apply_effect(distortion)
    guitar_track.apply_effect(delay)

    # Setting volume and notes
    bass_track.adjust_volume(-6)
    bass_track.set_note_sequence("C2 G2 C3 E3")
    guitar_track.adjust_volume(-3)
    guitar_track.set_note_sequence("C4 G4 C5 E5 G5")

    # Testing statistical methods
    print("\nUser-level statistics:")
    print(f"Projects per genre: {user.projects_per_genre()}")
    print(f"Total number of projects: {user.count_total_projects()}")
    print(f"Most used instrument: {user.most_used_instrument().instrument_name}")

    print("\nRock project statistics:")
    print(f"Percentage of tracks with effects: {rock_project.percentage_of_tracks_with_effects()}%")
    print(f"Most used effect: {rock_project.most_used_effect().effect_name}")

    print("\nBass track statistics:")
    print(f"Has effects: {bass_track.has_effects()}")
    print(f"Number of notes: {bass_track.note_count()}")