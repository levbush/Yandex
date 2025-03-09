import wave
import struct


def break_the_silence():
    in_file, out_file = wave.open('in.wav', 'rb'), wave.open('out.wav', 'wb')
    out_file.setparams(in_file.getparams())
    data = struct.unpack(f'<{in_file.getnframes()}h', in_file.readframes(in_file.getnframes()))
    data = [x for x in data if abs(x) > 5]
    out_file.writeframes(struct.pack(f'<{len(data)}h', *data))