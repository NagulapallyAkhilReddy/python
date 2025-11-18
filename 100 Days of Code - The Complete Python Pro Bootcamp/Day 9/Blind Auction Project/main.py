import art
print(art.logo)
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added

blind_auction={}
others="yes"
while others=="yes":
    name = input("what is your name? : ")
    bid = input("what is your bid? : ")
    others = input("Are there any other bidders? type yes or no")
    blind_auction[name]=bid
    print("\n"*100)
print(max(blind_auction))
# TODO-4: Compare bids in dictionary
maxprice=0
winner={}
for key in blind_auction:
    if int(blind_auction[key])>maxprice:
        maxprice=int(blind_auction[key])
        winner={}
        winner[key]=blind_auction[key]
for key in winner:
    print(f"the winner is {key} and the amount is {winner[key]}")


