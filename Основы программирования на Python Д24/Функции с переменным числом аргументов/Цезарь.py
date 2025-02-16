def encrypt_caesar(msg: str, shift: int = 3):
    shift = shift % 32
    ords = [ord(i) for i in msg]
    for i in range(len(ords)):
        if 1039 < ords[i] < 1072:
            ords[i] += shift
            if ords[i] > 1071:
                ords[i] -= 32
        elif 1071 < ords[i] < 1104:
            ords[i] += shift
            if ords[i] > 1103:
                ords[i] -= 32
    return ''.join([chr(i) for i in ords])


def decrypt_caesar(msg, shift=3):
    return encrypt_caesar(msg, 32 - shift)