// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-JAVA-015: Java JPQL/HQL injection

import javax.persistence.*;

public class UserRepository {

    @PersistenceContext
    private EntityManager em;

    public List<User> findByRole(String role) {
        // VULNERABLE: user input concatenated into JPQL query
        return em.createQuery("SELECT u FROM User u WHERE u.role = '" + role + "'")
                 .getResultList();
    }

    public User findByUsername(String username) {
        // VULNERABLE: String.format used to build JPQL
        String jpql = String.format("FROM User WHERE username = '%s'", username);
        return (User) em.createQuery(jpql).getSingleResult();
    }

    public List<Order> findOrders(String status, String userId) {
        // VULNERABLE: concatenation into native SQL query
        return em.createNativeQuery(
            "SELECT * FROM orders WHERE status = '" + status + "' AND user_id = " + userId
        ).getResultList();
    }
}
