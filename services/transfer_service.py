def valid_transfer_status(status):

    return status in [
        "Pending",
        "Approved",
        "Completed",
        "Cancelled"
    ]


def same_warehouse(source, destination):

    return source == destination


def sufficient_stock(
    available_stock,
    requested_stock
):

    return available_stock >= requested_stock
