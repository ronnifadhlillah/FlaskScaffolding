from engine.build import *
import routes
# print(routes)
apps=build()

# # Registering Blueprint sample
aut=routes.auth
apps.register_blueprint(aut.bp)
print(aut)
# # General routes / Routes for all
w=routes.web
apps.register_blueprint(w.bp)

if __name__=="__main__":
    apps.run()

