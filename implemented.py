from dao.movie import MovieDAO
from dao.director import DirectorDAO
from dao.genre import GenreDAO

from service.movie import MovieService
from service.director import DirectorService
from service.genre import GenreService

from setup_db import db

movie_dao = MovieDAO(session=db.session)
director_dao = DirectorDAO(session=db.session)
genre_dao = GenreDAO(session=db.session)

movie_service = MovieService(dao=movie_dao)
director_service = DirectorService(dao=director_dao)
genre_service = GenreService(dao=genre_dao)