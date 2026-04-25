// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-JAVA-024: XML Entity Expansion (Billion Laughs) — DTD not disabled

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.SAXParserFactory;
import org.w3c.dom.Document;
import java.io.InputStream;

public class XmlEntityExpansion {

    public Document parseXml(InputStream xmlStream) throws Exception {
        // TRIGGERS: DocumentBuilderFactory.newInstance() without disallow-doctype-decl
        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        DocumentBuilder builder = factory.newDocumentBuilder();
        return builder.parse(xmlStream);
    }

    public void parseWithSax(InputStream xmlStream) throws Exception {
        // TRIGGERS: SAXParserFactory.newInstance() without security features
        SAXParserFactory factory = SAXParserFactory.newInstance();
        factory.newSAXParser().parse(xmlStream, new org.xml.sax.helpers.DefaultHandler());
    }
}
