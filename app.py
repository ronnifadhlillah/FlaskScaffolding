import routes
import engine

apps=engine.build()

# Registering Blueprint sample
aut=routes.auth
apps.register_blueprint(aut.bp)
# General routes / Routes for all
w=routes.web
apps.register_blueprint(w.bp)

if __name__=="__main__":
    apps.run()
