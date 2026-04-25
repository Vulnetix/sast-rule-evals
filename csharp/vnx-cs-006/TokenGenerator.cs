// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-CS-006: Insecure random (System.Random for security use)

using System;
using System.Security.Cryptography;

public class TokenGenerator
{
    // VULNERABLE: System.Random used to generate a session token
    public string GenerateSessionToken()
    {
        var rng = new Random();
        var tokenBytes = new byte[32];
        rng.NextBytes(tokenBytes);  // NextBytes is predictable
        return Convert.ToBase64String(tokenBytes);
    }

    // VULNERABLE: System.Random for password reset token
    public string GeneratePasswordResetToken()
    {
        var random = new Random(Environment.TickCount);
        var chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
        var secret = new char[32];
        for (int i = 0; i < secret.Length; i++)
        {
            secret[i] = chars[random.Next(chars.Length)];
        }
        return new string(secret);
    }
}
