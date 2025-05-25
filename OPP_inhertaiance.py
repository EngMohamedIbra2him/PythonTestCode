# -------------------------------------------------
# ------------- Inheritance -----------------------
# -------------------------------------------------

class parrent :
    def __init__(self):
        print(f"this is the parent class")
    def action(self):
        return f"this class in the parent class"

class child(parrent):

    def __init__(self):
        print(f"this parent in the parent class")

mohamed= parrent()
ahmed=child()
print(mohamed.action())
print(ahmed.action())
