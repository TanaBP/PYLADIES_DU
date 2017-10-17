print("Napíš počet stĺpcov:")
n = int(input())

for dalsi_radky in range(n):
	for radek in range(n):
			print(radek*dalsi_radky, end=" ")

	print()
