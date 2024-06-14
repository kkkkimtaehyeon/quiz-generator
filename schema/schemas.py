def indivisual_serial(pdf) -> dict:
    return {
        "id": str(pdf['_id']),
        "name": pdf['name'],
        "url": pdf['url']
    }

def list_serial(pdfs) -> list:
    return [indivisual_serial(pdf) for pdf in pdfs]