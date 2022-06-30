from prettytable import PrettyTable
from prettytable import from_csv

aces_score = 0
twos_score = 0
threes_score = 0
fours_score = 0
fives_score = 0
sixes_score = 0
sum_of_number_scores = (
    aces_score + twos_score + threes_score + fours_score + fives_score + sixes_score
)
# if sum_of_number_scores >= 63 then bonus_upper_score = 35 points
bonus_upper_score = 0
if sum_of_number_scores >= 63:
    bonus_upper_score = 35
else:
    pass
total_upper_score = sum_of_number_scores + bonus_upper_score

three_of_a_kind_score = 0
four_of_a_kind_score = 0
full_house_score = 0
small_straight_score = 0
large_straight_score = 0
chance_score = 0
total_lower_score = 0

grand_total_score = 0

upper_section = PrettyTable(["Upper Section", "Score"])
upper_section.add_row(["[1] Aces", aces_score])
upper_section.add_row(["[2] Twos", twos_score])
upper_section.add_row(["[3] Threes", threes_score])
upper_section.add_row(["[4] Fours", fours_score])
upper_section.add_row(["[5] Fives", fives_score])
upper_section.add_row(["[6] Sixes", sixes_score])
upper_section.add_row(["Total", sum_of_number_scores])
upper_section.add_row(["Bonus ?", bonus_upper_score])
upper_section.add_row(["Total Upper", total_upper_score])

lower_section = PrettyTable(["Lower Section", "Score"])
lower_section.add_row(["[7] 3 of a kind", three_of_a_kind_score])
lower_section.add_row(["[8] 4 of a kind", four_of_a_kind_score])
lower_section.add_row(["[9] Full House", full_house_score])
lower_section.add_row(["[10] Small Straight", small_straight_score])
lower_section.add_row(["[11] Large Straight", large_straight_score])
lower_section.add_row(["[12] Chance", chance_score])
lower_section.add_row(
    ["Yahtzee", "yahtzee_score"]
)  # if Yahtzee is rolled add 50 if any more are rolled add 100 for each
lower_section.add_row(["Total Lower", total_lower_score])

grand_total = PrettyTable(["Grand Total", ""])
grand_total.add_row(["Score", grand_total_score])


def change_score(var, score):
    if var == 1:
        aces_score = score


def display_score_card():
    print(upper_section)
    # print(lower_section)
    # print(grand_total)
