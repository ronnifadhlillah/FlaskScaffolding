import routes
import engine

apps=engine.build()

# Registering Blueprint sample
aut=routes.auth

apps.register_blueprint(aut.bp)

if __name__=="__main__":
    apps.run()
