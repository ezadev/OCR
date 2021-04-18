import easyocr


def run_ocr():
    reader = easyocr.Reader(['en', 'id'], gpu=False)
    result = reader.readtext('img/text.png', detail=0)
    print(" ".join(result))


if __name__ == '__main__':
    run_ocr()
