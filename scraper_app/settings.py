BOT_NAME = 'HouseScraper'

SPIDER_MODULES = ['scraper_app.spiders']

USER_AGENT = 'finn (https://www.finn.no)'

DATABASE = {
    'drivername': 'postgres',
    'host': 'localhost',
    'port': '5432',
    'username': 'postgres',
    'password': 'admin',
    'database': 'Houses'
}

ITEM_PIPELINES = {
    'scraper_app.pipelines.HousesPipeline': 100
}

