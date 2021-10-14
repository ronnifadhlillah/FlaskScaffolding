from flask import render_template
import routes
import engine

apps=engine.Build()
# apps.register_blueprint(routes.block)

@apps.route('/')
def index():
    return render_template('index.html')

if __name__=="__main__":
    apps.run()
