def session_is_valid(store):
    if not store.exists('user'):
        return False

    user = store.get('user')
    if not user.get('token'):
        return False

    if not user.get('id'):
        return False

    return True


def clear_session(store):
    keys = list(store.keys())
    for key in keys:
        store.delete(key)
