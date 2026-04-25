// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-CS-003: XXE via XmlDocument with XmlResolver enabled

using System.Xml;

public class XmlParser
{
    // VULNERABLE: XmlDocument with XmlUrlResolver (allows XXE)
    public string ParseUserXml(string xmlContent)
    {
        var doc = new XmlDocument();
        doc.XmlResolver = new XmlUrlResolver();
        doc.LoadXml(xmlContent);
        return doc.InnerText;
    }

    // VULNERABLE: XmlReaderSettings with DtdProcessing.Parse
    public void ProcessXmlStream(System.IO.Stream stream)
    {
        var settings = new XmlReaderSettings
        {
            DtdProcessing = DtdProcessing.Parse,
            XmlResolver = new XmlUrlResolver()
        };
        using var reader = XmlReader.Create(stream, settings);
        while (reader.Read()) { }
    }

    // VULNERABLE: XmlTextReader with ProhibitDtd = false
    public void ParseLegacyXml(string path)
    {
        var reader = new XmlTextReader(path);
        reader.ProhibitDtd = false;
        while (reader.Read()) { }
    }
}
