#-*- coding: utf-8 -*-

class AmixerParser():
    def __init__(self):
        self.current = 0
        
    def get_volume(self):
        with open('/tmp/currentvolume', 'r') as f:
            self.current = int(f.read())
        return self.current
        
if __name__ == "__main__":
    parser = AmixerParser()
    print parser.get_volume()
