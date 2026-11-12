package edu.testing;

import java.util.HashMap;
import java.util.Map;

public final class AccountRepository {
    private final Map<String, Account> accounts = new HashMap<>();

    public void save(Account account) { accounts.put(account.id(), account); }

    public Account findById(String id) {
        Account found = accounts.get(id);
        if (found == null) throw new IllegalArgumentException("unknown account: " + id);
        return found;
    }
}
