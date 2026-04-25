// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-CS-004: Insecure deserialization via BinaryFormatter / SoapFormatter

using System.IO;
using System.Runtime.Serialization.Formatters.Binary;
using System.Runtime.Serialization.Formatters.Soap;

public class Deserializer
{
    // VULNERABLE: BinaryFormatter.Deserialize from untrusted stream
    public object DeserializeFromStream(Stream stream)
    {
        var formatter = new BinaryFormatter();
        return formatter.Deserialize(stream);
    }

    // VULNERABLE: SoapFormatter.Deserialize
    public object DeserializeSoap(Stream stream)
    {
        var formatter = new SoapFormatter();
        return formatter.Deserialize(stream);
    }

    // VULNERABLE: BinaryFormatter instantiation is sufficient to flag
    public void SaveObject(object obj, string path)
    {
        using var fs = new FileStream(path, FileMode.Create);
        new BinaryFormatter().Serialize(fs, obj);
    }
}
