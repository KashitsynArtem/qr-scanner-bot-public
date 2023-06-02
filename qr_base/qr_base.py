import qrcode
from io import BytesIO
from pyzbar.pyzbar import decode
from PIL import Image
from typing import Union


async def qr_gen(user_id: str) -> BytesIO:
    buf = BytesIO()
    qrcode.make(str(user_id)).save(buf)
    buf.seek(0)
    return buf


async def qr_scan(qr: BytesIO) -> Union[None, str]:
    if data := decode(Image.open(qr)):
        return data[0].data.decode('utf-8')

