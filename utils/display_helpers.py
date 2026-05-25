def display_result(records, empty_message="No records found."):

    if not records:
        print(empty_message)
        return

    if not isinstance(records, list):
        records = [records]

    for row in records:
        print(row)


def display_metric(value, metric_name="Result", empty_message="No data available."):

    if value is None:
        print(empty_message)
        return

    print(f"{metric_name}: {value}")