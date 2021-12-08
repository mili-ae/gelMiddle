from app.main import app
import os

if __name__ == "__main__":
    if not os.path.isdir("app/images/avatars"):
        os.mkdir("app/images/avatars")
    if not os.path.isdir("app/images/lvlups"):
        os.mkdir("app/images/lvlup")
    if not os.path.isdir("app/images/profiles"):
        os.mkdir("app/images/profile")
    
    app.run()