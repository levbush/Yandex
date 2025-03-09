import wave
import struct


def chip_and_dale(i):
    in_file, out_file = wave.open('in.wav', 'rb'), wave.open('out.wav', 'wb')
    out_file.setparams(in_file.getparams())
    data = struct.unpack(f'<{in_file.getnframes()}h', in_file.readframes(in_file.getnframes()))[::i]
    out_file.writeframes(struct.pack(f'<{len(data)}h', *data))