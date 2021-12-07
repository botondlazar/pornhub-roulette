links = []

vid_links = []



with open("C:\\Users\\botond\\Documents\\programozás\\pornhub roulette\\linkslinks.txt", "r") as reader:
    for line in reader.readlines():
        links.append(line)

#print(links)

for s in links:
    if"view_video.php?viewkey=" in s:
        vid_links.append(s)

print(*vid_links)

with open("C:\\Users\\botond\\Documents\\programozás\\pornhub roulette\\gec.txt", "w") as f:
    f.writelines(str(vid_links))






        

