import java.io.*;

// VNX-JAVA-005: Insecure deserialization
public class Deserialize {
    public Object load(InputStream input) throws Exception {
        ObjectInputStream ois = new ObjectInputStream(input);
        Object obj = ois.readObject();
        ois.close();
        return obj;
    }
}
