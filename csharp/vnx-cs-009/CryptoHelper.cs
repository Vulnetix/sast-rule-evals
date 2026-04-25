// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-CS-009: Weak cryptographic algorithms (MD5, SHA1, DES, RC2)

using System.Security.Cryptography;
using System.Text;

public class CryptoHelper
{
    // VULNERABLE: MD5 for password hashing
    public string HashPassword(string password)
    {
        var md5 = new MD5CryptoServiceProvider();
        var bytes = Encoding.UTF8.GetBytes(password);
        var hash = md5.ComputeHash(bytes);
        return Convert.ToBase64String(hash);
    }

    // VULNERABLE: SHA1 for data integrity check
    public byte[] ComputeChecksum(byte[] data)
    {
        using var sha1 = SHA1.Create();
        return sha1.ComputeHash(data);
    }

    // VULNERABLE: DES for encryption
    public byte[] EncryptData(byte[] plaintext, byte[] key)
    {
        using var des = new DESCryptoServiceProvider();
        des.Key = key;
        des.GenerateIV();
        using var encryptor = des.CreateEncryptor();
        return encryptor.TransformFinalBlock(plaintext, 0, plaintext.Length);
    }

    // VULNERABLE: TripleDES
    public byte[] EncryptTripleDES(byte[] data, byte[] key)
    {
        using var tripleDes = new TripleDESCryptoServiceProvider();
        tripleDes.Key = key;
        return tripleDes.CreateEncryptor().TransformFinalBlock(data, 0, data.Length);
    }
}
