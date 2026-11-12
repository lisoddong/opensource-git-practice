package edu.testing;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class AccountServiceIntegrationTest {
    @Test void serviceWithdrawalUpdatesRepositoryState() {
        AccountRepository repo = new AccountRepository();
        repo.save(new Account("A", 1000));
        AccountService service = new AccountService(repo);
        service.withdraw("A", 400);
        assertEquals(600, repo.findById("A").balance());
        assertEquals(600, service.balanceOf("A"));
    }
    @Test void rejectedWithdrawalDoesNotModifyStoredAccount() {
        AccountRepository repo = new AccountRepository();
        repo.save(new Account("A", 1000));
        AccountService service = new AccountService(repo);
        assertThrows(IllegalArgumentException.class, () -> service.withdraw("A", 1001));
        assertEquals(1000, repo.findById("A").balance());
    }
    @Test void unknownAccountRejects() {
        AccountService service = new AccountService(new AccountRepository());
        assertThrows(IllegalArgumentException.class, () -> service.withdraw("missing", 100));
    }
}
