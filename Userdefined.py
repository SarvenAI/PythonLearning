def get_grade(mark):
    return "c"

def greeting(name,place = None):
    if place:
            message = f"hello {name} ! welcome to {place}"
    else:
        message = f"hello {name} ! welcome"
    return message