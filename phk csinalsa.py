from os import defpath


phk = []
vid_phk = []


with open ("C:\\Users\\botond\\Documents\\programozás\\pornhub roulette\\phk.txt", "r") as reader:
    for line in reader.readlines():
        if "ph" in line:
            phk.append(line)



for i in phk:
    vid_phk.append("https://www.pornhub.com/view_video.php?viewkey=" + i)

print(vid_phk)

with open ("C:\\Users\\botond\\Documents\\programozás\\pornhub roulette\\links.txt", "w") as s:
    s.writelines(vid_phk)
