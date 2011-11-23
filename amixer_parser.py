#-*- coding: utf-8 -*-

import os

class AmixerParser():
    """Get audio volume from temporary file
        created by another shell script
    """
    def __init__(self):
        self.current = 10
        self.path = '/tmp/currentvolume'
        
    def get_volume(self):
        if os.path.exists(self.path):
            with open(self.path, 'r') as f:
                self.current = int(f.read())

        return self.current
        
if __name__ == "__main__":
    parser = AmixerParser()
    print parser.get_volume()
