""" A kindly teacher wishes to distribute a tub of sweets between her pupils. She will
first count the sweets and then divide them according to how many pupils attend
that day. Write a program that will tell the teacher how many sweets to give to each
pupil, and how many she will have left over. """

total_sweets = int(input("Total number of sweets: "))
total_pupils = int(input("Total number of attending pupils: "))

sweets_per_pupil = total_sweets // total_pupils
remaining_sweets = total_sweets % total_pupils

plural_sweet = "sweets" if sweets_per_pupil != 1 else "sweet"
plural_sweet2 = "sweets" if remaining_sweets != 1 else "sweet"
print(f"Each pupil will get {sweets_per_pupil} {plural_sweet} "
      f"with {remaining_sweets} {plural_sweet2} left over. ")
