class SampleA():
    class_val = "class val"

    def set_val(self):
        self.instance_val = "instance val"

    def print_val(self):
        print("class val = {}".format(self.class_val))
        print("instance val = {}".format(self.instance_val))

