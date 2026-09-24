def main():
    print("🎟️ Welcome to CineMatrix Ticket Booking System 🎟️\n")
    
    # 1. User Authentication / Login
    def login_user():
        print("--- 🔐 User Authentication ---")
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        if username and password:
            print(f"✅ Welcome back, {username}!\n")
            return True
        else:
            print("❌ Invalid credentials. Please try again.")
            return False

    # 2. Display Movies Catalog
    def display_movies():
        movies = [
            "1. 🎬 Avatar: The Way of Water",
            "2. 🦸 Avengers: Secret Wars",
            "3. 🕷️ Spider-Man: Beyond the Spider-Verse",
            "4. 🦖 Jurassic World: Rebirth",
            "5. 👻 The Conjuring: Last Rites"
        ]
        print("--- 🎬 Available Movies ---")
        for movie in movies:
            print(movie)
        
        while True:
            try:
                choice = int(input("\nSelect movie number (1-5): "))
                if 1 <= choice <= 5:
                    selected = movies[choice - 1].split(". ")[1]
                    print(f"✅ Selected Movie: {selected}\n")
                    return selected
                else:
                    print("❌ Please enter a number between 1 and 5.")
            except ValueError:
                print("❌ Invalid input! Please enter a valid number.")

    # 3. Select Showtime
    def select_showtime():
        showtimes = [
            "1. 🌅 Morning (10:00 AM)", 
            "2. ☀️ Matinee (01:30 PM)", 
            "3. 🌆 Evening (05:00 PM)", 
            "4. 🌙 Night (09:00 PM)"
        ]
        print("--- ⏰ Select Showtime ---")
        for time in showtimes:
            print(time)
            
        while True:
            try:
                choice = int(input("\nSelect showtime number (1-4): "))
                if 1 <= choice <= 4:
                    selected_time = showtimes[choice - 1].split(". ")[1]
                    print(f"✅ Selected Showtime: {selected_time}\n")
                    return selected_time
                else:
                    print("❌ Please enter a number between 1 and 4.")
            except ValueError:
                print("❌ Invalid input! Please enter a number.")

    # 4. Interactive Seat Matrix
    def display_seat_matrix():
        print("--- 💺 Interactive Seat Matrix ---")
        print("Available: [ ]  |  Booked: [X]\n")
        seats = [
            ["[ ]", "[ ]", "[ ]"],
            ["[X]", "[ ]", "[ ]"],
            ["[ ]", "[X]", "[ ]"]
        ]
        for i, row in enumerate(seats):
            print(f"Row {i+1}: {' '.join(row)}")
        
        seat_num = input("\nEnter your preferred seat choice (e.g., Row 1 Seat 2): ").strip()
        print(f"✅ Seat '{seat_num}' locked successfully!\n")
        return seat_num

    # 5. Ticket Types & Pricing
    def get_ticket_type():
        print("--- 🎫 Ticket Types & Pricing ---")
        print("1. 🎟️ Standard - ₹250 per seat")
        print("2. ⭐ Premium  - ₹500 per seat")
        print("3. 👑 VIP Box  - ₹1000 per seat")
        
        prices = {1: 250, 2: 500, 3: 1000}
        names = {1: "Standard", 2: "Premium", 3: "VIP Box"}
        
        while True:
            try:
                choice = int(input("\nSelect ticket type (1-3): "))
                if choice in prices:
                    print(f"✅ Selected: {names[choice]} (₹{prices[choice]} per seat)\n")
                    return prices[choice], names[choice]
                else:
                    print("❌ Please choose between 1, 2, or 3.")
            except ValueError:
                print("❌ Invalid input! Please enter a number.")

    # 6. Customer Details
    def get_customer_details():
        print("--- 👤 Customer Details ---")
        name = input("Enter Full Name: ").strip()
        phone = input("Enter Phone Number: ").strip()
        print(f"✅ Details saved for {name} ({phone})\n")
        return name, phone

    # 7. Calculate Total Tickets & Subtotal
    def calculate_total(price_per_seat):
        while True:
            try:
                qty = int(input("Enter number of tickets: "))
                if qty > 0:
                    subtotal = price_per_seat * qty
                    return qty, subtotal
                else:
                    print("❌ Please book at least 1 ticket.")
            except ValueError:
                print("❌ Invalid input! Please enter a valid number.")

    # 8. Apply Promo Code
    def apply_promo_code(total):
        print("--- 🏷️ Promo Code ---")
        code = input("Enter promo code (Type 'CINE50' or 'FIRSTBOOK', or press Enter to skip): ").strip().upper()
        discount = 0
        if code == "CINE50":
            discount = total * 0.50
            print("🎉 Promo 'CINE50' applied! 50% discount unlocked.")
        elif code == "FIRSTBOOK":
            discount = 100
            print("🎉 Promo 'FIRSTBOOK' applied! Flat ₹100 discount unlocked.")
        else:
            if code:
                print("❌ Invalid promo code. No discount applied.")
            else:
                print("ℹ️ No promo code applied.")
        print()
        return discount

    # 9. Booking Confirmation & Passbook Details
    def booking_details(name, movie, time, seat, t_type, qty, total, discount):
        final_amount = total - discount
        print("\n" + "="*45)
        print("📋 🎟️ FINAL BOOKING PASSBOOK 🎟️ 📋")
        print("="*45)
        print(f"👤 Customer Name : {name}")
        print(f"🎬 Movie         : {movie}")
        print(f"⏰ Showtime      : {time}")
        print(f"💺 Seat Selected : {seat}")
        print(f"🎫 Ticket Tier   : {t_type}")
        print(f"🔢 Quantity      : {qty}")
        print(f"💰 Subtotal      : ₹{total}")
        print(f"🏷️ Discount      : -₹{discount}")
        print(f"💵 Final Payable : ₹{final_amount}")
        print("="*45)
        print("✅ Booking Confirmed Successfully! Enjoy your movie! 🍿")
        print("="*45 + "\n")
        return final_amount

    # 10 & 11. Ticket Cancellation & Refund Workflow
    def cancel_ticket(final_amount):
        choice = input("Do you want to cancel your ticket? (type 'yes' or 'no'): ").strip().lower()
        if choice == 'yes':
            print("\n--- ❌ Ticket Cancellation Workflow ---")
            refund = final_amount * 0.80  # 20% cancellation fee deduction
            print(f"💵 Refund Calculated (80% of final amount): ₹{refund}")
            print("🧾 Refund Details: Processed successfully back to your original source account within 3-5 business days.")
            print("❌ Ticket cancelled successfully.")
        else:
            print("🎉 Thank you for confirming! Have a wonderful cinematic experience!")

    # --- Execution Flow inside main() ---
    if login_user():
        movie = display_movies()
        time = select_showtime()
        seat = display_seat_matrix()
        price, t_type = get_ticket_type()
        name, phone = get_customer_details()
        qty, subtotal = calculate_total(price)
        discount = apply_promo_code(subtotal)
        final_amt = booking_details(name, movie, time, seat, t_type, qty, subtotal, discount)
        cancel_ticket(final_amt)

# Program entry point
if __name__ == "__main__":
    main()
