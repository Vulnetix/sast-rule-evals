// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-CS-002: Command injection via Process.Start with user input

using System.Diagnostics;

public class CommandExecutor
{
    // VULNERABLE: Process.Start with string concatenation
    public string RunReport(string reportName)
    {
        var output = Process.Start("cmd.exe", "/c report.exe " + reportName);
        return output.ToString();
    }

    // VULNERABLE: FileName/Arguments with interpolation
    public void ConvertFile(string inputFile, string outputFile)
    {
        var proc = new Process();
        proc.StartInfo.FileName = "ffmpeg";
        proc.StartInfo.Arguments = $"-i {inputFile} {outputFile}";
        proc.Start();
        proc.WaitForExit();
    }

    // VULNERABLE: ProcessStartInfo with concatenation
    public string PingHost(string hostname)
    {
        var psi = new ProcessStartInfo
        {
            FileName = "ping",
            Arguments = "-c 4 " + hostname,
            RedirectStandardOutput = true
        };
        var p = Process.Start(psi);
        return p.StandardOutput.ReadToEnd();
    }
}
