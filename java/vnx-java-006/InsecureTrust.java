import javax.net.ssl.*;

// VNX-JAVA-006: Insecure TrustManager that accepts all certificates
public class InsecureTrust {
    private static final TrustManager[] trustAllCerts = new TrustManager[]{
        new X509TrustManager() {
            public void checkClientTrusted(java.security.cert.X509Certificate[] certs, String authType) {}
            public void checkServerTrusted(java.security.cert.X509Certificate[] certs, String authType) {}
            public java.security.cert.X509Certificate[] getAcceptedIssuers() { return null; }
        }
    };
}
