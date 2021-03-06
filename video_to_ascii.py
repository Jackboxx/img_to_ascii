import cv2
from time import sleep


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

def img_to_ascii(img):
    output = ''
    ration = img.shape[1] / img.shape[0]
    chunk_factor = 60
    chunk_size_x = int(img.shape[1] / chunk_factor);
    chunk_size_y = int((ration * img.shape[0]) / (chunk_factor*2));

    for x in range(0, img.shape[0] - chunk_size_x, chunk_size_x):
        for y in range(0, img.shape[1] - chunk_size_y, chunk_size_y):
            output += assign_char(img[x, y]);
        output += "\n";

    return output

filename = input('Enter a file name: ')
video_capture = cv2.VideoCapture('videos/' + filename)
fps = video_capture.get(cv2.CAP_PROP_FPS)
could_read, image = video_capture.read()
frame_buffer = []
looping = (input('Loop? Y/N ') == 'Y')

print('Loading...')
while could_read:
    frame_buffer.append(img_to_ascii(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)))
    could_read, image = video_capture.read()

print('Done!')
input('Press enter to play... ')
print('Playing now!')

while True:
    for frame in frame_buffer:
        print(chr(27) + "[2J")
        print(frame)
        sleep(1/fps)

    if not looping: 
        break

video_capture.release()