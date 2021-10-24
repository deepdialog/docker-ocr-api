import sys
sys.path.append('..')
from main import ocr

ocr.ocr('test1.png', cls=True)
ocr.ocr('test2.png', cls=True)