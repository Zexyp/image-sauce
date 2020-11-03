# image-sauce
#### **_The worst idea ever. (I have no idea how I came up with it (pls don't kill me)) It's just a test._**

### __Finaly description__
This is a python program that you can use to search images on Bing. It's giving mostly unpredictable results and might seem like it's not working.

## __The usage is simple (and description)__
  - At the start of the program you can search whatever you want.
  - After the program fineshes it's thing you should see a image of what you searched (it mostly doesn't work or it gives error or it crashes).
  - You can than type:
    - `/next` to show next result of the search
    - `/prev` to show previous result of the search
    - `/` to search again
    - `/quit` or just `/q` to quit
    - `/filter` to see all filters
      - `/filter "name of the filter"` to see filter's options
        - `/filter "name of the filter" "INDEX of the option"`
        - Example: `/filter color 3` → Activates color filter with option 3 which is red.
        
*The program only searches for jpg images and outputs with no color!*

### __Filters__
If you set any filter option to 0 you will disable it

  - `color` for color (tint)
    - `1` just colorful
    - `2` black and white
    - `3` - `12` specific colors
  - `size` for size of the image
    - `1` small
    - `2` medium
    - `3` large
    - `4` wallpaper
    - `5` custom (__you need to supply two more arguments__: the width and the height)
  - `type` for image type
    - `1` photo
    - `2` clipart
    - `3` linedrawing
    - `4` animated gif
    - `5` transparent
  - `aspect` for aspect ratio of the image
    - `1` square
    - `2` wide
    - `3` tall
  - `face` if image contains faces
    - `1` face
    - `2` portrait
  - `age` for age of the image
    - the age is specified in __minutes__
    - `-1` __to disable it!__

### Have fun!
