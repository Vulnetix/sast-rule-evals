// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-CS-010: Hardcoded connection string with credentials

using System.Data.SqlClient;

public class DataAccess
{
    // VULNERABLE: Hardcoded password in connection string
    private const string PrimaryConnection = "Server=prod-db.internal;Database=AppDb;User ID=appuser;Password=Sup3rS3cr3t!;";

    // VULNERABLE: Another hardcoded connection string
    private static string ReportConnection = "Data Source=reporting-server;Initial Catalog=Reports;User Id=sa;Password=Admin123;";

    public SqlConnection GetConnection()
    {
        return new SqlConnection(PrimaryConnection);
    }

    public SqlConnection GetReportConnection()
    {
        // Both should be flagged
        return new SqlConnection("Server=reports-db;Database=Analytics;User ID=analyst;Password=An@lytics2024;");
    }
}
