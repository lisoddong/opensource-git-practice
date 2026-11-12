package edu.testing;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class AccountTest {
    @Test void partialWithdrawalChangesBalance() {
        Account a = new Account("A", 1000);
        a.withdraw(400);
        assertEquals(600, a.balance());
    }
    @Test void fullWithdrawalAllowsZeroBalance() {
        Account a = new Account("A", 1000);
        a.withdraw(1000);
        assertEquals(0, a.balance());
    }
    @Test void insufficientBalanceRejectsAndPreservesBalance() {
        Account a = new Account("A", 1000);
        assertThrows(IllegalArgumentException.class, () -> a.withdraw(1001));
        assertEquals(1000, a.balance());
    }
    @Test void zeroAndNegativeAmountsReject() {
        Account a = new Account("A", 1000);
        assertThrows(IllegalArgumentException.class, () -> a.withdraw(0));
        assertThrows(IllegalArgumentException.class, () -> a.withdraw(-1));
        assertEquals(1000, a.balance());
    }
}
