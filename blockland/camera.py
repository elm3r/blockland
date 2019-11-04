# Blockland library camera implementation

class Camera:
    def __init__(self):
        self.x = 0
        self.y = 0

    def centerOn(self, object):
        try:
            self.x = object.x - 400
            self.y = object.y - 300
        except:
            print("Camera center error!")
