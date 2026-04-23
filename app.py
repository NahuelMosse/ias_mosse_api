from app import app, enviroment

if __name__ == "__main__":
    app.run(debug=enviroment.debug)
