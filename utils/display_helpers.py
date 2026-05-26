def display_result(records, empty_message="No records found."):

    if not records:
        print(empty_message)
        return

    if not isinstance(records, list):
        records = [records]

    for row in records:
        print(row)


def display_metric(value, metric_name=None, empty_message="No data available."):

    if value is None:
        print(empty_message)
        return

    if isinstance(value, dict):

        for metric_name, metric_value in value.items():

            display_metric(metric_value, metric_name)

        return

    print(f"{metric_name}: {value}")