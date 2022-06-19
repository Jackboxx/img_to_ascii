from PIL import Image
import requests

# example urls: 
#   https://data.whicdn.com/images/336288688/original.jpg?t=1571016657
#   https://227263-694567-raikfcquaxqncofqfm.stackpathdns.com/wp-content/uploads/2020/12/Among-Us-Red-Crewmate.png
#   https://i1.sndcdn.com/artworks-XJdVplPCbvDvJlH7-jF9c4A-t500x500.jpg 
#   https://image.shutterstock.com/z/stock-vector-red-heart-pixel-art-style-icon-vector-abstract-isolated-pixel-heart-object-design-classic-606257843.jpg

url = input('Enter an image url: ')
res = requests.get(url, stream=True)

img = Image.open(res.raw)
pixels = img.load()

chunk_size_x = int(img.size[0] / 80);
chunk_size_y = int(img.size[1] / 40);

output = ""

def assign_char(num):
    opt = int(num / 32)
    
    match opt:
        case 7:
            return '#'
        case 6:
            return '@'
        case 5:
            return 'M'
        case 4:
            return '&'
        case 3:
            return 't'
        case 2:
            return '/'
        case 1:
            return '*'
        case 0:
            return '\''

for y in range(0, img.size[1] - chunk_size_y, chunk_size_y):
    for x in range(0, img.size[0] - chunk_size_x, chunk_size_x):
        sum = 0;
        for i in range(0, chunk_size_x):
            for j in range(0, chunk_size_y):
                sum += pixels[x + i, y + j][0] + pixels[x + i, y + j][1] + pixels[x + i, y + j][2];
    
        sum /= (chunk_size_x*chunk_size_y*3)
        output += assign_char(sum);
    output += "\n";

print(output)