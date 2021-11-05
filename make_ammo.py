### Utility for generating Yandex.Tank ammo

import requests as http
import uuid
from urllib.parse import urlparse

paths = []


def generate_links():
    f = open("links.txt", "w+")
    print("generating urls")
    for i in range(2000):
        tmp = (
            "http://%s.ru\n"
        )
        f.write(tmp % "".join(str(uuid.uuid4()).split('-')))
    f.close()
    print("done")


def set_links(paths_arr):
    with open("links.txt") as file:
        while url_to_short := file.readline().rstrip():
            resp = http.post("http://37.139.34.190/set?url=" + url_to_short)
            paths.append(resp.text)
    return paths_arr

generate_links()
paths = set_links(paths)

f = open("ammo_get.txt", "w+")
f.write("[Connection: close]\n"
        "[User-Agent: Tank]\n")

ammo_template = (
        "%s\n\n"
    )

print("generating ammo for tank")
for path in paths:
    f.write(ammo_template % urlparse(path).path)
f.close()
print("done")