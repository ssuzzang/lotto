from flask import Flask, render_template 
import mongodb
from flask_migrate import Migrate

def create_app():

    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'suzzang'

    @app.route('/mongo')
    def mongotest():
        COLLECTION_NAME = 'lotto'
        HOST, USER, PASSWORD, DATABASE_NAME = mongodb.db_info()
        MONGO_URI = f'mongodb+srv://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}?retryWrites=true&w=majority'
        collection = mongodb.db_connect(MONGO_URI, DATABASE_NAME, COLLECTION_NAME)
        documents = collection.find()
        return render_template('mongo.html',data=documents)

    @app.route('/suzzang')
    def dashboard():
        return render_template('suzzang.html')

    #return app

    #mongodb.init_app(app)
    #migrate.init_app(app, mongodb)

    #from flask_app.routes.main_route import main_bp
    #app.register_blueprint(main_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)