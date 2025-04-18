from pet import Pet


my_pet = Pet(name="Rex")


print(" Rex is is not hungry:")
my_pet.eat()
my_pet.get_status()


print("\n Rex is energetic,cannot sleep:")
my_pet.sleep()
my_pet.get_status()


print("\nRex can play, energy level is high:")
my_pet.play()
my_pet.get_status()


print("\nTrained new trick:")
my_pet.train("roll over")
my_pet.train("play dead")
my_pet.show_tricks()

print("\n show_tricks :")
my_pet.show_tricks()