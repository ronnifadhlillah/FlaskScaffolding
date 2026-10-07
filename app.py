from engine.build import *
from engine.log import configure_logging
import routes

apps=build()
configure_logging(apps)

if __name__=="__main__":
    apps.run()
