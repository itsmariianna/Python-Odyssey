# Ի՞նչ տարբերութուն truncating division-ի և floor division-ի միջև։ Հիմնավորել պատասխանը։



# floor division-ը բաժանումը հատարում է դեպի "հատակ" / "ներքև"։ Այս բաժանումը կարող ենք կատարել // գործողության միջոցով, կամ էլ
# math module-ի միջոցով։ Օրինակ՝

print(9 // -7)      # Output -2

import math
print(math.floor(5 / -2))   # Output -3


# truncating division-ը բաժանման ժամանակ անտեսում է ստորակետից հետո եկող թվերը և վերադարձնում է ամբողջ մասը։ Ավելի պարզ երևում է 
# բացասական թվերի բաժանման ժամանակ։ Այս բաժանումը կարող ենք կատարել math module-ի միջոցով։ Օրինակ՝


print(math.trunc(9 / -7))      # Output -1
print(math.trunc(5 / -2))      # Output -2
