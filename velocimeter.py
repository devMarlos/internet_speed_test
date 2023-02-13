#speedtest~cli
import speedtest as sp

test = sp.Speedtest()

#Download
down = test.download()
rsDown = round(down)
#Conversão para MB
Fdown = int(rsDown/1e+6)

#Upload
upl = test.upload()
rsUp = round(upl)
#Conversão para MB
Fup = int(rsUp/1e+6)

print(f"DOWNLOAD: {Fdown} mb/")
print(f"UPLOAD: {Fup} mb/")