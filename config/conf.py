import random
import time





# Here i converted m to Km and second to hour then divison to reach Speed in this form (KM/H)
# # the 9.144 is distance of free space between two lines # found in https://news.osu.edu/slow-down----those-lines-on-the-road-are-longer-than-you-think/
# # i know that the 9.144 is an standard and my video may not be that but its like guess and its need Field research
def CalSpeed():
    time = random.uniform(0.44583048820495605, 0.42808566093444824)
    speed = ((9.144 * 3600) / ((time) * 1000))
    return speed
