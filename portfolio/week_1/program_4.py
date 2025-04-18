""" In a long career for Yorkshire, Geoffrey Boycott played 609 matches, batted 1014
times, was not out 162 times, and scored 48426 runs. Write a program to calculate
and display Boycott's batting average.
Note: A batting average is the number of runs scored divided by the number of
completed innings (i.e. the total times batted minus the times not out)."""

runs = 48426
times_batted = 1014
not_out = 162
innings = times_batted - not_out
average = runs / innings
print("Geoffrey Boycott's batting average is", round(average, 2))

