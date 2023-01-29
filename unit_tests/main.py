USERS_TO_LET_IN = ['Alice', 'Bob']


def let_this_user_in(username):
    return _in_list_case_insensitive(USERS_TO_LET_IN, username)


def _in_list_case_insensitive(items, item):
    lowercased_items = [x.lower() for x in items]
    lowercased_item = item.lower()

    return lowercased_item in lowercased_items
