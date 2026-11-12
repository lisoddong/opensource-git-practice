package edu.testing;

public final class AccountService {
    private final AccountRepository repository;
    public AccountService(AccountRepository repository) { this.repository = repository; }
    public void withdraw(String id, int amount) {
        Account account = repository.findById(id);
        account.withdraw(amount);
        repository.save(account);
    }
    public int balanceOf(String id) { return repository.findById(id).balance(); }
}
