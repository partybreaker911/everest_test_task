import eventlet

eventlet.monkey_patch()

from app import create_app, ext_celery, socketio

app = create_app()


if __name__ == "__main__":
    socketio.run(app, debug=True, use_reloader=True, host="0.0.0.0")
