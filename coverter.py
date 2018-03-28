PATH = r"F:\Subs\Inglourious.Basterds.2009.720p.BRRip.1.4GB.MkvCage-heb.srt"

with open(PATH) as f:
    data = f.read()

with open(r"D:\Desktop\try.txt", "w+") as f:
    f.write(data.decode("cp1255").encode("utf8"))