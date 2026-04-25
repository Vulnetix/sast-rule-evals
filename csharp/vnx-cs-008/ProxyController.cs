// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-CS-008: SSRF via WebClient/HttpClient with user-supplied URL

using System.Net;
using System.Net.Http;
using Microsoft.AspNetCore.Mvc;

public class ProxyController : Controller
{
    // VULNERABLE: WebClient.OpenRead with user-supplied URL
    public string FetchUrl(string targetUrl)
    {
        WebClient client = new WebClient();
        using var stream = client.OpenRead(targetUrl);
        using var reader = new System.IO.StreamReader(stream);
        return reader.ReadToEnd();
    }

    // VULNERABLE: WebClient.DownloadString with variable URL
    public string FetchContent(string url)
    {
        WebClient wc = new WebClient();
        return wc.DownloadString(url);
    }

    // VULNERABLE: HttpClient.GetAsync with user-controlled URL
    public async System.Threading.Tasks.Task<string> FetchAsync(string userUrl)
    {
        var httpClient = new HttpClient();
        var response = await httpClient.GetAsync(userUrl);
        return await response.Content.ReadAsStringAsync();
    }
}
