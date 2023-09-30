import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Transaction {
    private double amount;
    private String type;

    public Transaction(double amount, String type) {
        this.amount = amount;
        this.type = type;
    }

    public String toString() {
        return type + ": $" + amount;
    }
}

class Account {
    private int accountNumber;
    private double balance;
    private List<Transaction> transactions;

    public Account(int accountNumber) {
        this.accountNumber = accountNumber;
        this.balance = 0.0;
        this.transactions = new ArrayList<>();
    }

    public double getBalance() {
        return balance;
    }

    public void deposit(double amount) {
        balance += amount;
        transactions.add(new Transaction(amount, "Deposit"));
    }

    public boolean withdraw(double amount) {
        if (balance >= amount) {
            balance -= amount;
            transactions.add(new Transaction(amount, "Withdraw"));
            return true;
        }
        return false;
    }

    public void transfer(Account recipient, double amount) {
        if (withdraw(amount)) {
            recipient.deposit(amount);
            transactions.add(new Transaction(amount, "Transfer to Account #" + recipient.accountNumber));
        }
    }

    public List<Transaction> getTransactionHistory() {
        return transactions;
    }
}

class User {
    private int userId;
    private int pin;
    private Account account;

    public User(int userId, int pin) {
        this.userId = userId;
        this.pin = pin;
        this.account = new Account(userId); 
    }

    public Account getAccount() {
        return account;
    }

    public int getUserId() {
        return userId;
    }

    public int getPin() {
        return pin;
    }
}

class ATM {
    private List<User> users;
    private User currentUser;

    public ATM() {
        users = new ArrayList<>();
    }

    public void addUser(User user) {
        users.add(user);
    }

    public boolean authenticateUser(int userId, int pin) {
        for (User user : users) {
            if (user.getUserId() == userId && user.getPin() == pin) {
                currentUser = user;
                return true;
            }
        }
        return false;
    }

    public User getCurrentUser() {
        return currentUser;
    }

    public static void main(String[] args) {
        ATM atm = new ATM();
        User user1 = new User(12345, 1234); 
        atm.addUser(user1);

        Scanner scanner = new Scanner(System.in);
        int userId, pin;
        System.out.println("Welcome to the ATM!");
        
        do {
            System.out.print("Enter User ID: ");
            userId = scanner.nextInt();
            System.out.print("Enter PIN: ");
            pin = scanner.nextInt();
        } while (!atm.authenticateUser(userId, pin));
        
        User loggedInUser = atm.getCurrentUser();
        System.out.println("Welcome, User #" + loggedInUser.getUserId());
        
        scanner.close();
        System.out.println("Thank you for using the ATM!");
    }
}
