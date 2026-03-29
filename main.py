card1 = 300000
card2 = 100000

amount = int(input("O‘tkazmoqchi bo‘lgan summani kiriting: "))

if amount <= card1:
    card1 -= amount
    card2 += amount
    print("Pul o‘tkazildi.")
else:
    print("Yetarli mablag‘ yo‘q.")

print("1-karta:", card1)
print("2-karta:", card2)
