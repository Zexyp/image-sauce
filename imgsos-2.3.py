from PIL import Image
import numpy
import requests
import shutil
import os
import image_filter

def PixelToShadeSymbol(pixel):
    luminance = (int(pixel[0]) + int(pixel[1]) + int(pixel[2])) / 3
    if(luminance >= 0 and luminance < 51.2):
        return ' '
    if(luminance >= 51.2 and luminance < 102.4):
        return '░'
    if(luminance >= 102.4 and luminance < 153.6):
        return '▒'
    if(luminance >= 153.6 and luminance < 204.8):
        return '▓'
    if(luminance >= 204.8 and luminance < 256):
        return '█'

def PrintList(array):
    for element in array:
        print("   ", element)

def GetImageLinkFromHTML(html, suffix, index):
    image = 0
    oldend = 0
    end = 0
    start = 0
    while (image < index + 1):
        oldend = end
        end += html[end:].find(suffix) + len(suffix)
        #print(end, oldend)
        start = html.rfind('"https://', oldend, end)
        if not(html.rfind('"http://', oldend, end) > 0):
            if (start != -1):
                image += 1
                print("{} image in html found at: {} with url: {}".format(suffix, end, html[start + 1 : end]))
    
    if (end == -1):
        return None
    if (start == -1):
        return None
    return html[start + 1 : end]

    """
    image = 0
    end = 0
    start = 0
    for _ in range(index + 1):
        end += html[end:].find(suffix) + len(suffix)
        image += 1
        print(suffix, "image in html found at:", end)
    
    if (end == -1):
        return None
    start = html.rfind('"', 0, end)
    if (start == -1):
        return None
    return html[start + 1 : end]
    
    end = html.find(suffix)
    print(suffix, "image in html found at:", end)
    if (end == -1):
        return None
    start = html.rfind('"', 0, end)
    if (start == -1):
        return None
    return html[start + 1 : end + len(suffix)]
    """

def GetAllImageLinksFromHTML(html, suffix, safe, debug):
    if not(safe):
        image = 0
        oldend = 0
        end = 0
        start = 0

        active = True
        array = []
        
        while (active):
            oldend = end
            end += html[end:].find(suffix) + len(suffix)
            #print(end, oldend)
            start = html.rfind('"http', oldend, end)
            if (start != -1):
                image += 1
                array.append(html[start + 1 : end])
                if (debug):
                    print("{} image in html found at: {} with url: {}".format(suffix, end, html[start + 1 : end]))
            elif (end == -1 or start == -1):
                active = False
        
        return array
    
    else:
        image = 0
        oldend = 0
        end = 0
        start = 0

        active = True
        array = []
        
        while (active):
            oldend = end
            end += html[end:].find(suffix) + len(suffix)
            #print(end, oldend)
            start = html.rfind('"https://', oldend, end)
            if not(html.rfind('"http://', oldend, end) > 0):
                if (start != -1):
                    image += 1
                    array.append(html[start + 1 : end])
                    print("{} image in html found at: {} with url: {}".format(suffix, end, html[start + 1 : end]))
                elif (end == -1 or start == -1):
                    active = False
        
        return array

def DownloadImage(url, folder, filename):
    image_response = requests.get(image_url, stream = True)
    
    if image_response.status_code == 200:
        image_response.raw.decode_content = True
        
        with open(folder + filename,'wb') as f:
            shutil.copyfileobj(image_response.raw, f)
        
        print("image downloaded:", filename)
    else:
        print("image couldn't be retreived!")

    return image_response

def ScaleImageToFit(image, max_width, max_height):
    if (image.size[0] > max_width or image.size[1] > max_height):
        if (image.size[0] > max_width):
            factor = image.size[0] / max_width
            height = int(image.size[1] / factor)
            image = image.resize((max_width, height))
        if (image.size[1] > max_height):
            factor = image.size[1] / max_height
            width = int(image.size[0] / factor)
            image = image.resize((width, max_height))
        print("modified size: {}×{}".format(image.size[0], image.size[1]))
    return image

def RemoveImage(file):
    try:
        if (os.path.isfile(file)):
            os.remove(file)
    except Exception as error:
        print("error while trying to delete image! ({})".format(error))

def CheckFolderOrCreate(path):
    if (not os.path.isdir(path)):
        os.mkdir(path)

def DrawImage(image):
    image_array = numpy.array(image)

    for row in image_array:
        for pixel in row:
            print(PixelToShadeSymbol(pixel) * 2, end = '')
        print()


tmp_folder="tmp/"

debug = False
safemode = False

site = "https://www.bing.com"
url = site + "/images/search?q={}"
image_type = ".jpg"
html_image_offset = 0

fltr = image_filter.Filter()

command = ""
selection_index = 0

if (debug):
    print("debug mode")
while (True):
    

    if (command == ""):        
        search = input("search: ")

        response = requests.get(url.format(search) + fltr.AssembleFilter())

        if (debug):
            with open('response.txt', 'w', encoding='utf-8') as response_file:
                response_file.write(response.text)

        image_urls = GetAllImageLinksFromHTML(response.text, image_type, safemode, False)

    #image_url = GetImageLinkFromHTML(response.text, ".jpg", html_image_offset)
    
    
    print("images ({}):".format(len(image_urls)))
    PrintList(image_urls)

    if (len(image_urls)):
        image_url = image_urls[selection_index]
        print("current image ({}):".format(selection_index + 1), image_url)
        filename = image_url.split("/")[-1]

        CheckFolderOrCreate(tmp_folder)
        
        image_response = DownloadImage(image_url, tmp_folder, filename)
        
        if (image_response.status_code == 200):
            file = tmp_folder + filename #input("file: ")

            if (debug):
                max_width = 48
                max_height = 32
            else:
                max_width = 96
                max_height = 64
            try:
                image = Image.open(file)
                print("format:", image.format)
                print("mode:", image.mode)
                print("original size: {}×{}".format(image.size[0], image.size[1]))

                image = ScaleImageToFit(image, max_width, max_height)

                #image.show()

                DrawImage(image)
            except OSError:
                print("error while trying to open image!")
    else:
        print("no output!")
    while (command != "/"):
        command = input()
        if (len(command) > 0):
            if (command[0] == "/"):
                command_array = command.split() 
                #if (command_array[0] == "/quit"):
                #    RemoveImage(file)
                #    break
                if (command_array[0] == "/next"):
                    if (selection_index < len(image_urls) - 1):
                        selection_index += 1
                        break
                    else:
                        print("nothing more")
                if (command_array[0] == "/prev"):
                    if (selection_index > 0):
                        selection_index -= 1
                        break
                    else:
                        print("nothing more")
                if (command_array[0] == "/filter"):
                    fltr.Command(command)
                    command = ""

                if (command == "/"):
                    command = ""
                    selection_index = 0
                    break
                if (command == "/q"):
                    break
                
                command = ""
    
    #flushing
    if 'file' in locals():
        RemoveImage(file)

    #quiting
    if (command == "/q"):
        break
