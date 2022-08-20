from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer,  String, MetaData
)

# executing the intstructions from our localhost "chinook" db
db = create_engine("postgresql:///chinook")

meta = MetaData(db)

artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)

track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)

# making the connection
with db.connect() as connection:
    # Query1 - select all records from the Artist table
    #select_table = artist_table.select()

    # Query2 - select the name column from the Artist table
    #select_table = artist_table.select().with_only_columns([artist_table.c.Name])

    # Query3 - select Queen from the Artist table
    #select_table = artist_table.select().where(artist_table.c.Name == "Queen")

    # Query4 - select ArtistId of 51 from the Artist table
    #select_table = artist_table.select().where(artist_table.c.ArtistId == 51)

    # Query5 - select ArtistId of 51 from the Artist table
    #select_table = album_table.select().where(album_table.c.ArtistId == 51)

    # Query6 - select ArtistId of 51 from the Artist table
    select_table = track_table.select().where(track_table.c.Composer == "Queen")

    results = connection.execute(select_table)
    for result in results:
        print(result)

