import base64
import zlib
import json
from qrcode import QRCode
from gcQr.models import GameLineup


def encode_and_compress(lineup: GameLineup) -> bytes:
    lineup_str = json.dumps(lineup, default=lambda x: x.__json__)
    compressed_data = zlib.compress(lineup_str.encode(), level=-1, wbits=-zlib.MAX_WBITS)
    return base64.b64encode(compressed_data)


def save_image(qr_data: bytes, filename: str):
    qrcode = QRCode()
    qrcode.add_data(qr_data)
    qrcode.make(fit=True)
    img = qrcode.make_image(fill='black', back_color='white')
    img.save(filename)


def qr_code_from_lineup(lineup: GameLineup, filename: str = "lineup.png"):
    save_image(encode_and_compress(lineup), filename)


def lineup_from_qr_code_data(compressed_data: str) -> GameLineup:
    decoded_data = base64.b64decode(compressed_data)
    decompressed_data = zlib.decompress(decoded_data, -zlib.MAX_WBITS)
    some_dict = json.loads(decompressed_data)
    return GameLineup.from_dict(some_dict)
