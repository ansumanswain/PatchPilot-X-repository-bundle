users = []

def create_user(name):
    users.append(name)
    return {
        "success": True,
        "name": name
    }
