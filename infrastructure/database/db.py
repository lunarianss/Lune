

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
from config import lune_config
import logging
import pymysql


pymysql.version_info = (1, 4, 13, "final", 0)
pymysql.install_as_MySQLdb()


logger = logging.getLogger(__name__)

engine = None
db_session = None


def init_app():
    global engine, db_session
    engine = create_engine(lune_config.SQLALCHEMY_DATABASE_URI, **
                           lune_config.SQLALCHEMY_ENGINE_OPTIONS)
    db_session = scoped_session(sessionmaker(autocommit=False,
                                             autoflush=False,
                                             bind=engine))
    logger.info("mysql is ready!")


def get_session():
    return db_session
