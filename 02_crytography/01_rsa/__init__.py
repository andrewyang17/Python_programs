from flask import Flask, send_from_directory
from flask_uploads import UploadSet, configure_uploads, TEXT

File = UploadSet('FILES', TEXT)


def create_app():

    app = Flask(__name__)
    app.config['UPLOADED_FILES_DEST'] = '/tmp/example'
    app.config['SECRET_KEY'] = b'u\xaa_\xf8N^\x98\x1f\xeb\xe1\x0cg\x1f\x0e%\xe1\xb7\x05D\x03\xdf\xc8}\x85'
    configure_uploads(app, File)

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint)

    @app.route('/_uploads/file/<filename>')
    def uploaded_file(filename):
        return send_from_directory(directory="/tmp/example", filename=filename)

    return app
