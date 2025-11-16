print("Welcome to Calki, your Forex Profit/Loss Calculator")
print("Fortune Favors the Brave")
def calculate_profit(entry_price, exit_price, lot_size, position):
    if position == 'long':
        profit = (exit_price - entry_price) * 10000 * lot_size
    elif position == 'short':
        profit = (entry_price - exit_price) * 10000 * lot_size
    else:
        profit = 0
    return profit
while True:    
       entry_price= float(input("Entry price: "))
       exit_price=float(input("Exit price: "))
       lot_size=float(input("Lot size: "))
       position=input("Position (long/short): ")
       print("\n--- Your Trade Details---")
       print(f" Entry price: {entry_price} ")
       print(f"Exit price: {exit_price} ")
       print(f"Lot size: {lot_size} ")
       print(f"Position: {position} ")
       result=calculate_profit(entry_price,   exit_price,lot_size,position)
       print("\n" + "="*40)
       if result > 0:
            print(f"✓ PROFIT: ${result:.2f}")
       elif result < 0:
            print(f"✗ LOSS: ${abs(result):.2f}")
       else:
            print(f"BREAKEVEN: $0.00")
       print("="*40)
       another = input("\nCalculate another trade? (yes/no): ").lower()
       if another != 'yes':
            print("\nThanks for using Calki! Keep building! 🚀")
       break
