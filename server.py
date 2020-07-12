import flask
from flask import request

app = flask.Flask(__name__)

app.config["DEBUG"] = True


def main():
    @app.route('/', methods=['GET']) 
    def sart():
        return '''
        <form method="POST">
            <button type="submit" class="button1">Start</button></center>
        </form>'''

    @app.route('/', methods=['POST']) 
    def start():
        data = request.get_json()
        teste = data['full_name']
        print(teste)
        return 'bjhb'

    app.run()


if __name__ == "__main__":
    main()
