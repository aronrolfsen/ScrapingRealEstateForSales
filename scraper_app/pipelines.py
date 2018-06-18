from sqlalchemy.orm import sessionmaker
from scraper_app.models import Houses, db_connect, create_houses_table


class HousesPipeline(object):
    def __init__(self):
        engine = db_connect()
        create_houses_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        house = Houses(**item)

        try:
            session.add(house)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
        return item
