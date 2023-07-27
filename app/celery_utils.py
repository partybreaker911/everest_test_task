from celery import current_app as current_celery_app


def make_celery(app):
    """
    Creates a Celery instance using the provided Flask app.

    Parameters:
        app (Flask): The Flask app instance.

    Returns:
        Celery: The Celery instance configured with the Flask app's configuration.
    """
    celery = current_celery_app
    celery.config_from_object(app.config, namespace="CELERY")

    return celery
