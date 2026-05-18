# Secret Auction Program 💰

A simple command-line Secret Auction application built with Python. Multiple users can place bids anonymously, and the program automatically determines the highest bidder at the end of the auction.

---

## Features

* Anonymous bidding system
* Multiple participant support
* Automatic highest bid detection
* User-friendly command-line interface
* Real-time bid storage using dictionaries

---

## Technologies Used

* Python 3

---

## How the Program Works

1. Users enter their name and bid amount.
2. The program stores each bid securely.
3. Additional bidders can continue participating.
4. Once bidding ends, the program identifies the highest bidder.
5. The winner and winning amount are displayed.

---

## How to Run the Project

### Step 1: Clone the Repository

```bash id="7m2p9x"
git clone <your-github-repo-link>
```

### Step 2: Navigate to the Project Folder

```bash id="9x1k4q"
cd secret-auction-program
```

### Step 3: Run the Python File

```bash id="2n7v6z"
python main.py
```

---

## Project Structure

```bash id="8v5r1c"
secret-auction-program/
│
├── main.py
└── README.md
```

---

## Sample Output

```bash id="6t3k8p"
What is your name?: John
What is your bid?: $300
Are there any other bidders? Type 'yes' or 'no'.

yes

What is your name?: David
What is your bid?: $450
Are there any other bidders? Type 'yes' or 'no'.

no

The winner is David with a bid of $450.
```

---

## Learning Outcomes

This project helps in understanding:

* Python dictionaries
* Functions and loops
* Conditional statements
* User input handling
* Data comparison logic
* Simple auction system implementation

---

## Future Improvements

* Add secret password protection
* Store auction history in files
* Add GUI using Tkinter
* Support multiple auction rounds
* Add currency formatting and validations

---

## Author

Developed by [Charan S]

