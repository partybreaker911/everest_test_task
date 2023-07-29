from celery import shared_task

from app.orders.controller import get_order_by_id


@shared_task
def change_order_status(order_id, status):
    try:
        new_status = get_order_by_id(order_id).status
    except ValueError:
        return False
    order = get_order_by_id(order_id)
    if order:
        order.status = new_status
        db.session.commit()
        return True
    return False
