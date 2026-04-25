// VNX-ANDROID-002: WebView JavaScript enabled
import android.webkit.WebView;
import android.webkit.WebSettings;

public class MainActivity {
    void setupWebView() {
        WebView webView = new WebView(this);
        webView.getSettings().setJavaScriptEnabled(true);
        webView.addJavascriptInterface(new WebAppInterface(), "Android");
    }
}
