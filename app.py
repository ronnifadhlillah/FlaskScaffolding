from flask import render_template
import routes
import engine

apps=engine.build()

if __name__=="__main__":
    apps.run()
