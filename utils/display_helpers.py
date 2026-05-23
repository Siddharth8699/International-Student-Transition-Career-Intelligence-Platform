def display_result(data, empty_message="No records found."):

    if not data:
        print(empty_message)
        return

    if isinstance(data, list):

        for row in data:
            print(row)

    else:
        print(data)