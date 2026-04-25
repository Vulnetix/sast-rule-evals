import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.DocumentBuilder;
import org.w3c.dom.Document;
import java.io.InputStream;

// VNX-JAVA-004: XXE - DocumentBuilderFactory without secure features
public class XxeParser {
    public Document parse(InputStream xml) throws Exception {
        DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
        DocumentBuilder db = dbf.newDocumentBuilder();
        return db.parse(xml);
    }
}
