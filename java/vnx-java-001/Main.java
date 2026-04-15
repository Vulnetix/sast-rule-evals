public class Main {
    public static void main(String[] args) throws Exception {
        String userInput = args[0];
        // VNX-JAVA-001: Runtime.exec() with string concatenation
        Runtime.getRuntime().exec("cmd /c " + userInput);
    }
}
