// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-CS-001: SQL injection via string concatenation in SqlCommand

using System.Data.SqlClient;

public class UserController
{
    private readonly string _connectionString = "Server=db;Database=app;Integrated Security=True";

    public User GetUser(string username)
    {
        using var conn = new SqlConnection(_connectionString);
        conn.Open();

        // VULNERABLE: SqlCommand constructed with string concatenation
        var query = "SELECT * FROM Users WHERE Username = '" + username + "'";
        var cmd = new SqlCommand(query, conn);

        using var reader = cmd.ExecuteReader();
        if (reader.Read())
        {
            return new User { Id = reader.GetInt32(0), Name = reader.GetString(1) };
        }
        return null;
    }

    public bool LoginUser(string username, string password)
    {
        using var conn = new SqlConnection(_connectionString);
        conn.Open();

        // VULNERABLE: CommandText assigned with string.Format
        var cmd = new SqlCommand();
        cmd.Connection = conn;
        cmd.CommandText = string.Format("SELECT COUNT(*) FROM Users WHERE Username='{0}' AND Password='{1}'", username, password);

        return (int)cmd.ExecuteScalar() > 0;
    }

    public class User
    {
        public int Id { get; set; }
        public string Name { get; set; }
    }
}
