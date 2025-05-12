from datetime import date
import uuid

def generate_unique_id(prefix = "") -> str:
    return f"{prefix}{str(uuid.uuid4())[:8]}"

class InstrumentType:
    DRUMS = "Drums"
    GUITAR = "Guitar"
    BASS = "Bass"

class EffectType:
    REVERB = "Reverb"
    DELAY = "Delay"
    DISTORTION = "Distortion"

class VirtualInstrument:
    def __init__(self, instrument_id, instrument_name, instrument_type):
        self.instrument_id = instrument_id
        self.instrument_name = instrument_name
        self.virtual_instrument_type = instrument_type

    def play_note(self, note, duration):
        print(f"Playing {note} for {duration} seconds on {self.instrument_name}")

class AudioEffect:
    def __init__(self, effect_id, effect_name, effect_type):
        self.effect_id = effect_id
        self.effect_name = effect_name
        self.audio_effect_type = effect_type

class AudioTrack:
    def __init__(self, track_id, track_name, duration_seconds, volume_db):
        self.track_id = track_id
        self.track_name = track_name
        self.duration_seconds = duration_seconds
        self.volume_db = volume_db
        self.manual_note_sequence = ""
        self.used_instrument = None
        self.applied_effects = []

    def add_instrument(self, instrument):
        self.used_instrument = instrument

    def apply_effect(self, effect):
        self.applied_effects.append(effect)

    def remove_effect(self, effect):
        if effect in self.applied_effects:
            self.applied_effects.remove(effect)

    def set_note_sequence(self, notes):
        self.manual_note_sequence = notes

    def adjust_volume(self, new_volume_db):
        self.volume_db = new_volume_db

    def has_effects(self):
        return len(self.applied_effects) > 0

    def note_count(self):
        return len(self.manual_note_sequence)

class MusicalProject:
    def __init__(self, project_id, project_title, creation_date, musical_genre):
        self.project_id = project_id
        self.project_title = project_title
        self.creation_date = creation_date
        self.musical_genre = musical_genre
        self.tracks = []

    def add_track(self, track_name):
        track = AudioTrack(str(len(self.tracks) + 1), track_name, 0, 0)
        self.tracks.append(track)
        return track

    def percentage_tracks_with_effects(self):
        if not self.tracks:
            return 0.0
        return sum(track.has_effects() for track in self.tracks) / len(self.tracks) * 100

    def most_used_effect(self):
        effect_count = {}
        for track in self.tracks:
            for effect in track.applied_effects:
                effect_count[effect.effect_name] = effect_count.get(effect.effect_name, 0) + 1
        return max(effect_count, key=effect_count.get) if effect_count else None

class User:
    def __init__(self, user_id, user_name, email):
        self.user_id = user_id
        self.user_name = user_name
        self.email = email
        self.projects = []

    def create_project(self, title):
        project = MusicalProject(str(len(self.projects) + 1), title, date.today(), "")
        self.projects.append(project)
        return project

    def projects_by_genre(self):
        genre_count = {}
        for project in self.projects:
            genre_count[project.musical_genre] = genre_count.get(project.musical_genre, 0) + 1
        return genre_count

    def count_total_projects(self):
        return len(self.projects)

    def most_used_instrument(self):
        instrument_count = {}
        for project in self.projects:
            for track in project.tracks:
                if track.used_instrument:
                    instrument_name = track.used_instrument.instrument_name
                    instrument_count[instrument_name] = instrument_count.get(instrument_name, 0) + 1
        return max(instrument_count, key=instrument_count.get)

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
    print(f"Projects per genre: {user.projects_by_genre()}")
    print(f"Total number of projects: {user.count_total_projects()}")
    print(f"Most used instrument: {user.most_used_instrument().instrument_name}")

    print("\nRock project statistics:")
    print(f"Percentage of tracks with effects: {rock_project.percentage_of_tracks_with_effects()}%")
    print(f"Most used effect: {rock_project.most_used_effect().effect_name}")

    print("\nBass track statistics:")
    print(f"Has effects: {bass_track.has_effects()}")
    print(f"Number of notes: {bass_track.note_count()}")