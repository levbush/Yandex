def line(s: str, t: str) -> None:
    s, t = list(map(float, s.split('x'))), list(map(float, t.split(';')))
    print(s[0] * t[0] + s[-1] == t[-1])