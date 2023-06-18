class SampleA():
    class_val = "class val"

    def set_val(self):
        self.instance_val = "instance val"

    def print_val(self):
        print("class val = {}".format(self.class_val))
        print("instance val = {}".format(self.instance_val))

isinstance_a = SampleA()
isinstance_a.set_val()
print(isinstance_a.instance_val)
isinstance_a.print_val()
print(SampleA.class_val)
print(isinstance_a.__class__.class_val)
isinstance_b = SampleA()
isinstance_b.set_val()
isinstance_b.print_val()
isinstance_a.__class__.class_val = "class val 2"
isinstance_b.print_val()

print("*****")
print(id(isinstance_a.__class__.class_val))
print(id(isinstance_b.__class__.class_val))