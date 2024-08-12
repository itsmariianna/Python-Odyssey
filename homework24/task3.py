# 3. Ի՞նչ տարբերութուն truncating division-ի և floor division-ի միջև։ Հիմնավորել պատասխանը։

# Truncating division-ը վերադարձնում է ամբողջ մասը, անտեսելով ստրոակետից հետո եկող թվերը։ 
# Իրականացվում է import անելով math մոդուլը։

import math

print(math.trunc(5 / -2))    # Output -2
print(math.trunc(13 / -4))   # Output -2


# Floow division-ը կլորացնում է թիվը դեպի "հատակ"։ Ավելի պարզ է երևում բացասական թվերի հետ նման բաժանում կատարելուց։
# Իրականացվում է // գործողության միջոցով կամ import անելով math մոդուլը։

print(math.floor(5 / -2))   # Output -3
print(13 // -7)             # Output -2