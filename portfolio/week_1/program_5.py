""" The Head of Computing at the University of Poppleton is tasked with dividing a
group of students into lab groups. A lab group is 24 students, since this is the
number of PCs in a lab. Write a program that calculates how many groups are
needed for the following number of students: 113, 175, 12. Display how many full
groups there will be, and how many students will be in the smaller "left over"
group."""


students_list = [113, 175, 12]
for total in students_list:
    groups = total // 24
    leftover = total % 24
    print("For", total, "students:")
    print("  Full groups of 24:", groups)
    print("  Left over students:", leftover)

