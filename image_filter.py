def PrintList(array):
        for element in array:
            print("   ", element)

class Filter:
    def __init__(self):
        self.prefix = "&qft="
        
        self.size_filter = "+filter:imagesize-"
        self.sizes = ["small", "medium", "large", "wallpaper", "custom_{}_{}"]
        self.size_custom = ("","")
        self.size_index = -1

        self.color_filter = "+filter:color2-"
        self.colors = ["color", "bw", "FGcls_RED", "FGcls_ORANGE", "FGcls_YELLOW", "FGcls_GREEN", "FGcls_TEAL", "FGcls_BLUE", "FGcls_PURPLE", "FGcls_PINK", "FGcls_BROWN", "FGcls_BLACK", "FGcls_GRAY", "FGcls_WHITE"]
        self.color_index = -1

        self.type_filter = "+filter:photo-"
        self.types = ["photo", "clipart", "linedrawing", "animatedgif", "transparent"]
        self.type_index = -1

        self.aspect_filter = "+filter:aspect-"
        self.aspects = ["square", "wide", "tall"]
        self.aspect_index = -1

        self.face_filter = "+filter:face-"
        self.faces = ["face", "portrait"]
        self.face_index = -1

        self.age_filter = "+filter:age-"
        self.age = "lt{}"
        self.age_custom = -1

        self.filters = ["size", "color", "type", "aspect", "face", "age"]
    
    def AssembleFilter(self):
        full_filter = ""

        if (self.size_index > -1):
            if (self.size_index == len(self.sizes) - 1):
                full_filter += self.size_filter + self.sizes[self.size_index].format(self.size_custom[0], self.size_custom[1])
            else:
                full_filter += self.size_filter + self.sizes[self.size_index]
        if (self.color_index > -1):
            full_filter += self.color_filter + self.colors[self.color_index]
        if (self.type_index > -1):
            full_filter += self.type_filter + self.types[self.type_index]
        if (self.aspect_index > -1):
            full_filter += self.aspect_filter + self.aspects[self.aspect_index]
        if (self.face_index > -1):
            full_filter += self.face_filter + self.faces[self.face_index]
        if (self.age_custom > -1):
            full_filter += self.age_filter + self.age.format(self.age_custom)

        if (full_filter != ""):
            full_filter = self.prefix + full_filter

        return full_filter
    
    def UnsetAll(self):
        self.size_index = -1
        self.color_index = -1
        self.type_index = -1
        self.aspect_index = -1
        self.face_index = -1
        self.age_custom = -1
    
    def Command(self, command):
        command_array = command.split()
        if (command_array[0] == "/filter"):
            if (len(command_array) == 1):
                PrintList(self.filters)
            if (len(command_array) >= 2):
                if (command_array[1] == "size"):
                    if (len(command_array) >= 3):
                        self.size_index = int (command_array[2]) - 1
                        if (len(command_array) == 5 and self.size_index == len(self.sizes) - 1):
                            self.size_custom = (command_array[3], command_array[4])
                    else:
                        PrintList(self.sizes)
                        if (self.size_index > -1):
                            if (self.size_index == len(self.sizes) - 1):
                                print("current:", self.sizes[self.size_index].format(self.size_custom[0], self.size_custom[1]))
                            else:
                                print("current:", self.sizes[self.size_index])
                if (command_array[1] == "color"):
                    if (len(command_array) == 3):
                        self.color_index = int (command_array[2]) - 1
                    else:
                        PrintList(self.colors)
                        if (self.color_index > -1):
                            print("current:", self.colors[self.color_index])
                if (command_array[1] == "type"):
                    if (len(command_array) == 3):
                        self.type_index = int (command_array[2]) - 1
                    else:
                        PrintList(self.types)
                        if (self.type_index > -1):
                            print("current:", self.types[self.type_index])
                if (command_array[1] == "aspect"):
                    if (len(command_array) == 3):
                        self.aspect_index = int (command_array[2]) - 1
                    else:
                        PrintList(self.aspects)
                        if (self.aspects_index > -1):
                            print("current:", self.aspects[self.aspect_index])
                if (command_array[1] == "face"):
                    if (len(command_array) == 3):
                        self.face_index = int (command_array[2]) - 1
                    else:
                        PrintList(self.faces)
                        if (self.faces_index > -1):
                            print("current:", self.faces[self.face_index])
                if (command_array[1] == "age"):
                    if (len(command_array) == 3):
                        self.age = int (command_array[2])
                    else:
                        if (self.age > -1):
                            print("current:", self.age)

                if (command_array[1] == "clear"):
                    self.UnsetAll();
                    print("cleared")
