package edu.testing;

public final class Account {
    private final String id;
    private int balance;

    public Account(String id, int openingBalance) {
        if (id == null || id.isBlank()) throw new IllegalArgumentException("id required");
        if (openingBalance < 0) throw new IllegalArgumentException("negative opening balance");
        this.id = id;
        this.balance = openingBalance;
    }

    public String id() { return id; }
    public int balance() { return balance; }

    public void withdraw(int amount) {
        if (amount <= 0) throw new IllegalArgumentException("amount must be positive");
        if (amount > balance) throw new IllegalArgumentException("insufficient funds");
        balance -= amount;
    }
}
