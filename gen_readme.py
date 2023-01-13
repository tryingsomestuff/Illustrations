import glob, os

url_base = "https://raw.githubusercontent.com/tryingsomestuff/Illustrations/master/img/"


with open('README.md', 'w') as f:

    f.write('# DALL-E and stable-diffusion generated chess illustrations\n\n')
    os.chdir('img')
    i = 0
    for file in sorted(glob.glob("dall-e*.png")):
        if i%2 == 0:
            f.write('<p align="center">\n')
        f.write('<img src="{}{}" width="350">\n'.format(url_base,file))
        if i%2 == 1:
            f.write('</p>\n')
        i+=1
    for file in sorted(glob.glob("stablediffusion*.png")):
        if i%2 == 0:
            f.write('<p align="center">\n')
        f.write('<img src="{}{}" width="350">\n'.format(url_base,file))
        if i%2 == 1:
            f.write('</p>\n')
        i+=1
    for file in sorted(glob.glob("MidJourney*.png")):
        if i%2 == 0:
            f.write('<p align="center">\n')
        f.write('<img src="{}{}" width="350">\n'.format(url_base,file))
        if i%2 == 1:
            f.write('</p>\n')
        i+=1




