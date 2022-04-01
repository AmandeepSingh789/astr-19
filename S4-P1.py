class Lion:
    def __init__(self,arm_length,leg_length,num_eyes,tail,furry):
        self.arm_length= arm_length
        self.leg_length= leg_length
        self.num_eyes= num_eyes
        self.tail= tail
        self.furry = furry

    def print_details(self):

        print("Arm length: ", self.arm_length)
        print("Leg length: ", self.leg_length)
        print("Number Of Eyes: ", self.num_eyes)
        print("Does it have A Tail: ", self.tail)
        print("Is it Furry: ", self.furry)

def main():
    animal  = Lion(34,34,2,True,True)
    animal.print_details()


if __name__=="__main__":
    main()
