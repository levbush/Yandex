import wave
import struct


def pitch_and_toss():
    with wave.open('in.wav', 'rb') as source, wave.open('out.wav', 'wb') as dest:
        dest.setparams(source.getparams())
        data = list(struct.unpack(f'<{source.getnframes()}h', source.readframes(source.getnframes())))
        q = len(data) // 4
        q1 = data[:q]
        q2 = data[q:2 * q]
        q3 = data[2 * q:3 * q]
        q4 = data[3 * q:]
        dest.writeframes(struct.pack(f'<{len(data)}h', *(q3 + q4 + q1 + q2)))