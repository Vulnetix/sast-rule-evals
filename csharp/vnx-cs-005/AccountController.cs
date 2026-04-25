// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-CS-005: Missing ValidateAntiForgeryToken on state-changing MVC action

using Microsoft.AspNetCore.Mvc;

public class AccountController : Controller
{
    // VULNERABLE: HttpPost without [ValidateAntiForgeryToken]
    [HttpPost]
    public IActionResult ChangePassword(string currentPassword, string newPassword)
    {
        // No CSRF token validation — any site can forge this request
        // ... password change logic ...
        return Ok();
    }

    // VULNERABLE: HttpDelete without anti-forgery validation
    [HttpDelete]
    public IActionResult DeleteAccount(int userId)
    {
        // Attacker can craft a request that deletes any account
        return Ok();
    }

    // SAFE (would not be flagged): has [ValidateAntiForgeryToken]
    // [HttpPost]
    // [ValidateAntiForgeryToken]
    // public IActionResult UpdateProfile(ProfileModel model) { ... }
}
