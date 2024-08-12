# 4. Ի՞նչ գործողություն է կատարում slicing Python-ում, բերել կոդի օրինակներ։

# Slicing-ի միջոցով կարող ենք բաժանումներ կատարել հերթականությունների վրա (string, list, tuple):
# Այն իրականացվում է offset-ի միջոցով, այսինքն ըստ ինդեքսի ենք նշումներ կատարում։
# ընդհանուր տեսքն այսպես է sequence = [start:end:step]
# Start: այն ինդեքսն է, որից պետք է սկսել գործողությունը
# End։ այն ինդեքսն է, որտեղ պետք է ընդհատվի գործողությունը, և այդ ինդեքս տարրը չի ներառվի
# Step։ քայլերի քանակը, default 1 

word = 'Pyton'
print(word[1:3])                  # Output: yt

ls = [45, 46, 47, 48, 49]
print(ls[:-1])                    # Output: [45, 46, 47, 48]

tp = (3, 'hello', 90, 89, 21, 'Python')
print(tp[::2])                      # Output: (3, 90, 21), 