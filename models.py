"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""

    __tablename__ = "playlists"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False,  unique=True)
    description = db.Column(db.String(200))

    playlists_songs = db.relationship('PlaylistSong', backref='playlist')

    
    def songs(self):
        return [Song.query.get(s.song_id) for s in self.playlists_songs] 

    def __repr__(self):
        return f"<Playlist {self.name} {self.description}>"

class Song(db.Model):
    """Song."""

    __tablename__ = "songs"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    artist = db.Column(db.Text, nullable=False)

    playlists_songs = db.relationship('PlaylistSong', backref='song')

    def __repr__(self):
        return f"<Song {self.title} {self.artist}>"

class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    __tablename__ = "playlists_songs"
    
    playlist_id = db.Column(db.Integer, db.ForeignKey("playlists.id"), primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey("songs.id"), primary_key=True)

    

# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
