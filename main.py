from paddleocr import PaddleOCR
from fastapi import FastAPI
from paddleocr.paddleocr import main
import uvicorn
ocr = PaddleOCR(use_angle_cls=True, lang="ch")


app = FastAPI()


@app.get('/')
async def root():
    return {1: 1}


@app.get('/api/ocr/{imgpath}')
async def get_orc(imgpath: str):
    """
    curl -XGET http://localhost:8000/api/ocr/test.png
    """
    results = ocr.ocr(imgpath, cls=True)
    text = [r[1][0] for r in results]
    return {
        'ok': True,
        'data': text
    }

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, reload=True, debug=True)