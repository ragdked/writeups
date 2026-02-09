package thm.crypto;

import burp.api.montoya.BurpExtension;
import burp.api.montoya.MontoyaApi;
import burp.api.montoya.core.ByteArray;
import burp.api.montoya.http.message.HttpRequestResponse;
import burp.api.montoya.http.message.requests.HttpRequest;
import burp.api.montoya.http.message.responses.HttpResponse;
import burp.api.montoya.ui.Selection;
import burp.api.montoya.ui.editor.RawEditor;
import burp.api.montoya.ui.editor.extension.ExtensionProvidedHttpRequestEditor;
import burp.api.montoya.ui.editor.extension.ExtensionProvidedHttpResponseEditor;

import javax.crypto.Cipher;
import java.awt.Component;
import java.io.ByteArrayOutputStream;
import java.nio.charset.StandardCharsets;
import java.security.KeyFactory;
import java.security.PrivateKey;
import java.security.PublicKey;
import java.security.interfaces.RSAKey;
import java.security.spec.PKCS8EncodedKeySpec;
import java.security.spec.X509EncodedKeySpec;
import java.util.Base64;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class CryptoEditExtension implements BurpExtension
{
    private static final String SERVER_PRIVATE_PEM = """
-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC/CmDZoFEtP1F+
2VwTxCdyZiLbB4tPQScfBcOwATgD/O9HV1P1fikUis1dWdMqUirxEEyKXKhOfcYd
SAmgUcYZ2pl+cIIfF/QhVfY2GliLUepl5c0KCpjgW0wf1a+NgQfb+3CFSe/KZPx6
AbdznRqlPyxOwmuFaLYz6WFDbJhcZ5xkeAAzsR11q+nJMR0zDXGEh540ejVDE+OK
LX50khTyIgnwXc1C26RN78RDJOMkbHuoPFWhs76eOeet6p2odno+pgP/qOWb2bJe
1S4lCqDExbBvEk25LkDL0lBJEYR/AS6Ake4oS6h8l1ORb8+Jsb0bfNrCzg2GZyjy
vDn2PWttAgMBAAECggEAQ8Mco1TYNmJ1N7dFj8VN8KgFyQceBNipVbmntbBY/CEl
hnqVT0iWrbCmM2x/GE3Y6XTMkW9YS68VLKG2uGUJDXaaZ1zk6r6GW6SwFnS134UI
zWf7mIo1u67mi4wyHtEbxo2jVcPqCDJV07j0J1AceWy0/KK9nK6NolAvrcjBKlUA
F9PIOzwS7tlmoX6tN7X8xKcoTwa+W/2poFZFlsBrWDlrQO0+mnIu/ne/nTlBZHIR
53n4Qg+G7bxs3xKp5DJ9T+K8hd/4iv2zYLBqC1T3WmdNWHD7CDFP4D4GJw9sqoWO
IYxI8GjJn+jWN6pUvSIHu0HFTOpieJl/v+Hc/FSlCQKBgQD4NEFLiu4eo9ZNk4I2
a/x8Ixi/NroDhEqtYutdn7IH+IEol7nTtEKkRrA1Z7FMnYh1/1iRQwms8YIr9KsG
3GeFCGNP8g+9YZ8aXIEU11gML8T+jpN2Y3z7mqRnJIzDeOzPiMYmaopmyKcP7RYS
L+h2fdjYJtxFu8D3C3ZZS4WXkwKBgQDFCnxZWmoT0lZakIBJwUhH4VtYl0FmxioJ
+HpLJyO7vR3V46igmarvU3KW+U7ouoYf2lDcfLWOK3VXpW5FpXzp3WNRe7KA70vQ
QeVTV8vKtIOBfXz5jJNhlm5Dp5iDgfgr4Q+zbR+RjxXLPwc02AbZWyx+q4q1dKmr
zFcdJWzQ/wKBgQCnO6Ym/RPVxzQ0jsf0XSwAhDE/XONWTUN3sae+LERrBHAZ5qkJ
UHJ6dzpwsU4PvjDcuFB3h4C0awD3FuJJPCXvx6gKjKE4S9dEjsFWRoYHqAQGNBB9
eykR6a8N492IMyjz6EcCSVS5Tkbp/yeY13i8pax+byiJP6kTi0CRh8YaSwKBgQCh
fQaM9N0bgbfkYanCyPZEcx46bTzczmyF32/bSCixJT3enscFWOwPWYUA1zMk6joi
wPqkulDSRCvXuW23BvppcViE36xcn8Ky3E7nD32mlGtzJTXYEK55vKCCMkl8/ng2
/i2wEC9fTLW/7dgqJyL14ROGfXEhZovokYCUEqgsYQKBgG4bMelGkTgiGPLc2g7c
TvAc9T7XlUkRqS5ZvoulZuJsJ2BfnDtYjzzVlRU35kDzEBja0Rkv9Rwys+Ft47Md
CEaGB/Nz8hBvA3wQjpLYUW4HXul3j5igRvZ/u8CwW+YDqkMpoCcYqTFJnqDOx8I9
KmaZV/MVPurxIhmwtUrMOjzH
-----END PRIVATE KEY-----
""";

    private static final String SERVER_PUBLIC_PEM = """
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvwpg2aBRLT9RftlcE8Qn
cmYi2weLT0EnHwXDsAE4A/zvR1dT9X4pFIrNXVnTKlIq8RBMilyoTn3GHUgJoFHG
GdqZfnCCHxf0IVX2NhpYi1HqZeXNCgqY4FtMH9WvjYEH2/twhUnvymT8egG3c50a
pT8sTsJrhWi2M+lhQ2yYXGecZHgAM7EddavpyTEdMw1xhIeeNHo1QxPjii1+dJIU
8iIJ8F3NQtukTe/EQyTjJGx7qDxVobO+njnnreqdqHZ6PqYD/6jlm9myXtUuJQqg
xMWwbxJNuS5Ay9JQSRGEfwEugJHuKEuofJdTkW/PibG9G3zaws4Nhmco8rw59j1r
bQIDAQAB
-----END PUBLIC KEY-----
""";

    private static final String CLIENT_PRIVATE_PEM = """
-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCHFhkwcfgZNVDe
KogLYzQSTTr8wgCi7WNepqeMuTTSXIX22SbzlK/gYlKtPPPxi2JzCkfa9VnTLsTd
3M4ZAL6d0rfo3L0KJ/SKMPq8VnGV9/y5YGyPmgbE1Dy8R2llP0m5GuO4giAoahZX
ePHsPbhNxtQuNW/EiGKcZaz5GQHILEQk2/0ZzqT0e/8jQMljpnbMUoGKe4yhT4JG
QGB7w7wPtQpFhDcASctUO8j3bcOL8tyrPfUcpNKFrkSNY0XT1gqnOuKe29YP0YnC
3bE/m5UPn7atBxP/4FrVRaQvM2S9ta+tZiDU5jP+xU3sBmMLlZByY5KiEeUGkvEz
FjfaMHihAgMBAAECggEAAMiqAvD721dW47Gh7EU+L/Of1afxZ5CeoaXQWcOoutZh
qn5tRHdAv6HJbJb6nESKkMvi0apoG+6g4r/PaDer63v1sEuw2v9jKta8uzlaD5B+
uGOG4LzQSI3J2A625dEImjLlxrAmXC6sqFN3zaboaAbg+/9IUabYEePRBYlhpEv7
jP9IquO6pO3q13gDhot0fS7MM4sTfYKdPfb8qEwYCpsz3Qi7lFdbBqZxz/O/tkPq
giNJNJnHBLmXNOIdSCocMldIhZaPMmcDODPXAehmrru7l/Kh5hnfdK7Njcoph5T4
EJqAPOU7XVSyBeJKiKj1x/S+2jzLn8s3hOKCiBbbwQKBgQC+IvSbRXVA16he1yBE
183VRAALdVRDDTZcFALaexuNfly2SMU9SL/AAFrbNMaQ83y79XtAbDqk8C6YRhyi
z2Il9puVu8G61UB2lWzD5DvDYbb4OS+AroluYZQzeR1+02sZUkR4R0QnfNRQUtMR
3awfBIgf9B6Kr90Dnn/OLmQrYQKBgQC14V2azqz4Nkg4bg1LLk612H2fhwz38Evj
mlMmxAxdIqGJUz+wGb3tSGmGz7fPxmIga9k8n22nMpfZOyyGF9D93LVa+/9NeFEV
DWH5yph+xBN7SSyQMb+Q1xD6gTigLmkIynUXzcucgZB8oUGtexR2IoFu3Li7R9F3
HYpUpsKVQQKBgQCFB3X20TEJbhm6SW+lWwwDY7FYUv3ib/MRl1qrvCh55eg+DUoa
57RpRJZM+m7XadRiuY1DdLXPQtCG778HVmvIPfN7XsNb0eppTYCsyhnaSJq4r2IB
+ZvkI9eJ7/poCsnLDJklQk94BUmS7XAJ9vt/NC99k9JunD7ZUmL/QcwJ4QKBgQCG
a812gJEt0VCHBC8nBU5+70XJBVL8W8h6qrAR0osguluQ1soXKK9KE16KmDJNiV00
gQDI4Tt1etrnXeiGIkv/k4Mlf2EsrGOgn4dtyeHyro+HaolY+KuQLKMLwT1MhYBz
Us4/jYWSYd+bfMLBqFlzBgWLHe4Z2/ZfhqGZ9rWRAQKBgGX7uHz9nUaldXxt4lBn
94FR8D6FJxyKGr0/35XrPE3gc1nDJIQGl62E9vk8eVuBsFgqhm2ISroRSxeRI6ml
djzuBNJ/gQ5hxhj7ifv1ZakiwvxR2D5uJBPU5gve19Fyrq5On6R+KvVR4b+vcZ5A
0HuYuUaGZhtLd9ouH49CvSXj
-----END PRIVATE KEY-----
""";

    @Override
    public void initialize(MontoyaApi api)
    {
        api.extension().setName("THM CryptoEdit (Full)");
        RSAUtil rsa = new RSAUtil(SERVER_PRIVATE_PEM, SERVER_PUBLIC_PEM, CLIENT_PRIVATE_PEM);

        api.userInterface().registerHttpRequestEditorProvider(ctx -> new RequestCryptoEditor(api, rsa));
        api.userInterface().registerHttpResponseEditorProvider(ctx -> new ResponseCryptoEditor(api, rsa));

        api.logging().logToOutput("[+] THM CryptoEdit loaded");
    }

    static class RequestCryptoEditor implements ExtensionProvidedHttpRequestEditor
    {
        enum Mode { NONE, BODY_B64, JSON_FIELD_B64 }

        private final RSAUtil rsa;
        private final RawEditor editor;
        private HttpRequest current;
        private Mode mode = Mode.NONE;
        private String jsonFieldName;

        RequestCryptoEditor(MontoyaApi api, RSAUtil rsa)
        {
            this.rsa = rsa;
            this.editor = api.userInterface().createRawEditor();
            this.editor.setEditable(true);
        }

        @Override
        public String caption()
        {
            return "CryptoEdit";
        }

        @Override
        public void setRequestResponse(HttpRequestResponse requestResponse)
        {
            current = null;
            mode = Mode.NONE;
            jsonFieldName = null;

            if (requestResponse == null || requestResponse.request() == null)
            {
                editor.setContents(ByteArray.byteArray());
                editor.setEditable(false);
                return;
            }

            current = requestResponse.request();
            String body = current.bodyToString().trim();

            try
            {
                String pt = rsa.decryptRequestBodyBase64(body);
                mode = Mode.BODY_B64;
                editor.setContents(ByteArray.byteArray(pt));
                editor.setEditable(true);
                return;
            }
            catch (Exception ignored) {}

            try
            {
                ParseResult parsed = tryExtractEncryptedField(body);
                if (parsed.found)
                {
                    String clean = unescapeJsonString(parsed.fieldValue);
                    String pt = rsa.decryptRequestBodyBase64(clean);
                    mode = Mode.JSON_FIELD_B64;
                    jsonFieldName = parsed.fieldName;
                    editor.setContents(ByteArray.byteArray(pt));
                    editor.setEditable(true);
                    return;
                }
            }
            catch (Exception ignored) {}

            editor.setContents(ByteArray.byteArray("[decrypt failed]\n\nRaw body:\n" + body));
            editor.setEditable(false);
        }

        @Override
        public HttpRequest getRequest()
        {
            if (current == null || mode == Mode.NONE || !editor.isModified())
            {
                return current;
            }

            String editedPlain = editor.getContents().toString();
            String newB64 = rsa.encryptRequestPlainToBase64(editedPlain);

            if (mode == Mode.BODY_B64)
            {
                return current.withBody(newB64);
            }

            if (mode == Mode.JSON_FIELD_B64 && jsonFieldName != null)
            {
                String replaced = replaceJsonField(current.bodyToString(), jsonFieldName, escapeForJsonString(newB64));
                return current.withBody(replaced);
            }

            return current;
        }

        @Override
        public boolean isEnabledFor(HttpRequestResponse requestResponse)
        {
            return requestResponse != null && requestResponse.request() != null;
        }

        @Override
        public boolean isModified()
        {
            return editor.isModified();
        }

        @Override
        public Selection selectedData()
        {
            return editor.selection().orElse(null);
        }

        @Override
        public Component uiComponent()
        {
            return editor.uiComponent();
        }
    }

    static class ResponseCryptoEditor implements ExtensionProvidedHttpResponseEditor
    {
        private final RSAUtil rsa;
        private final RawEditor editor;

        ResponseCryptoEditor(MontoyaApi api, RSAUtil rsa)
        {
            this.rsa = rsa;
            this.editor = api.userInterface().createRawEditor();
            this.editor.setEditable(false);
        }

        @Override
        public String caption()
        {
            return "CryptoEdit";
        }

        @Override
        public void setRequestResponse(HttpRequestResponse requestResponse)
        {
            if (requestResponse == null || requestResponse.response() == null)
            {
                editor.setContents(ByteArray.byteArray());
                return;
            }

            HttpResponse response = requestResponse.response();
            String body = response.bodyToString().trim();

            try
            {
                String pt = rsa.decryptResponseBodyBase64(body);
                editor.setContents(ByteArray.byteArray(pt));
                return;
            }
            catch (Exception ignored) {}

            try
            {
                ParseResult parsed = tryExtractEncryptedField(body);
                if (parsed.found)
                {
                    String clean = unescapeJsonString(parsed.fieldValue);
                    String pt = rsa.decryptResponseBodyBase64(clean);
                    editor.setContents(ByteArray.byteArray(pt));
                    return;
                }
            }
            catch (Exception ignored) {}

            editor.setContents(ByteArray.byteArray("[decrypt failed]\n\nRaw body:\n" + body));
        }

        @Override
        public HttpResponse getResponse()
        {
            return null;
        }

        @Override
        public boolean isEnabledFor(HttpRequestResponse requestResponse)
        {
            return requestResponse != null && requestResponse.response() != null;
        }

        @Override
        public boolean isModified()
        {
            return false;
        }

        @Override
        public Selection selectedData()
        {
            return editor.selection().orElse(null);
        }

        @Override
        public Component uiComponent()
        {
            return editor.uiComponent();
        }
    }

    static class RSAUtil
    {
        private final PrivateKey serverPrivate;
        private final PublicKey serverPublic;
        private final PrivateKey clientPrivate;

        RSAUtil(String serverPrivPem, String serverPubPem, String clientPrivPem)
        {
            try
            {
                serverPrivate = parsePrivateKey(serverPrivPem);
                serverPublic = parsePublicKey(serverPubPem);
                clientPrivate = parsePrivateKey(clientPrivPem);
            }
            catch (Exception e)
            {
                throw new RuntimeException("Key parse failed", e);
            }
        }

        String decryptRequestBodyBase64(String b64)
        {
            return decryptBase64Smart(b64, new PrivateKey[]{serverPrivate, clientPrivate});
        }

        String decryptResponseBodyBase64(String b64)
        {
            return decryptBase64Smart(b64, new PrivateKey[]{clientPrivate, serverPrivate});
        }

        String encryptRequestPlainToBase64(String plain)
        {
            byte[] enc = rsaEncryptMaybeChunked(
                    plain.getBytes(StandardCharsets.UTF_8),
                    serverPublic,
                    "RSA/ECB/PKCS1Padding"
            );
            return Base64.getEncoder().encodeToString(enc);
        }

        private String decryptBase64Smart(String b64, PrivateKey[] keys)
        {
            Exception last = null;
            byte[][] candidates = buildCipherCandidates(b64.trim());

            String[] transforms = new String[] {
                    "RSA/ECB/PKCS1Padding",
                    "RSA/ECB/OAEPWithSHA-1AndMGF1Padding",
                    "RSA/ECB/OAEPWithSHA-256AndMGF1Padding"
            };

            for (byte[] candidate : candidates)
            {
                if (candidate == null || candidate.length == 0) continue;

                for (PrivateKey key : keys)
                {
                    for (String transform : transforms)
                    {
                        try
                        {
                            byte[] pt = rsaDecryptMaybeChunked(candidate, key, transform);
                            return new String(pt, StandardCharsets.UTF_8);
                        }
                        catch (Exception e)
                        {
                            last = e;
                        }
                    }
                }
            }

            throw new RuntimeException("Decrypt failed: " + (last != null ? last.getMessage() : "unknown"));
        }

        private static byte[][] buildCipherCandidates(String raw)
        {
            byte[] a = null;
            byte[] b = null;
            byte[] c = null;
            byte[] d = null;

            try { a = Base64.getDecoder().decode(raw); } catch (Exception ignored) {}
            try { b = Base64.getUrlDecoder().decode(raw); } catch (Exception ignored) {}

            c = trySecondDecode(a);
            d = trySecondDecode(b);

            return new byte[][] { a, b, c, d };
        }

        private static byte[] trySecondDecode(byte[] first)
        {
            if (first == null || first.length == 0) return null;

            try
            {
                String s = new String(first, StandardCharsets.UTF_8).trim();
                try { return Base64.getDecoder().decode(s); } catch (Exception ignored) {}
                try { return Base64.getUrlDecoder().decode(s); } catch (Exception ignored) {}
            }
            catch (Exception ignored) {}

            return null;
        }

        private static PrivateKey parsePrivateKey(String pem) throws Exception
        {
            return KeyFactory.getInstance("RSA").generatePrivate(new PKCS8EncodedKeySpec(pemToDer(pem)));
        }

        private static PublicKey parsePublicKey(String pem) throws Exception
        {
            return KeyFactory.getInstance("RSA").generatePublic(new X509EncodedKeySpec(pemToDer(pem)));
        }

        private static byte[] pemToDer(String pem)
        {
            String n = pem
                    .replaceAll("-----BEGIN [A-Z ]+-----", "")
                    .replaceAll("-----END [A-Z ]+-----", "")
                    .replaceAll("\\s+", "");
            return Base64.getDecoder().decode(n);
        }

        private static byte[] rsaDecryptMaybeChunked(byte[] cipherText, PrivateKey key, String transform)
        {
            try
            {
                Cipher cipher = Cipher.getInstance(transform);
                cipher.init(Cipher.DECRYPT_MODE, key);

                int keySize = ((RSAKey) key).getModulus().bitLength() / 8;

                if (cipherText.length == keySize)
                {
                    return cipher.doFinal(cipherText);
                }

                if (cipherText.length % keySize == 0)
                {
                    ByteArrayOutputStream bos = new ByteArrayOutputStream();
                    for (int i = 0; i < cipherText.length; i += keySize)
                    {
                        byte[] block = new byte[keySize];
                        System.arraycopy(cipherText, i, block, 0, keySize);
                        bos.write(cipher.doFinal(block));
                    }
                    return bos.toByteArray();
                }

                return cipher.doFinal(cipherText);
            }
            catch (Exception e)
            {
                throw new RuntimeException(e);
            }
        }

        private static byte[] rsaEncryptMaybeChunked(byte[] plain, PublicKey key, String transform)
        {
            try
            {
                Cipher cipher = Cipher.getInstance(transform);
                cipher.init(Cipher.ENCRYPT_MODE, key);

                int keySize = ((RSAKey) key).getModulus().bitLength() / 8;
                int maxPlainBlock = "RSA/ECB/PKCS1Padding".equals(transform) ? (keySize - 11) : (keySize - 42);

                if (plain.length <= maxPlainBlock)
                {
                    return cipher.doFinal(plain);
                }

                ByteArrayOutputStream bos = new ByteArrayOutputStream();
                for (int i = 0; i < plain.length; i += maxPlainBlock)
                {
                    int len = Math.min(maxPlainBlock, plain.length - i);
                    byte[] block = new byte[len];
                    System.arraycopy(plain, i, block, 0, len);
                    bos.write(cipher.doFinal(block));
                }
                return bos.toByteArray();
            }
            catch (Exception e)
            {
                throw new RuntimeException(e);
            }
        }
    }

    static class ParseResult
    {
        final boolean found;
        final String fieldName;
        final String fieldValue;

        ParseResult(boolean found, String fieldName, String fieldValue)
        {
            this.found = found;
            this.fieldName = fieldName;
            this.fieldValue = fieldValue;
        }
    }

    private static ParseResult tryExtractEncryptedField(String body)
    {
        Matcher m = Pattern.compile("\"(data|payload|enc|token)\"\\s*:\\s*\"([^\"]+)\"").matcher(body);
        if (m.find())
        {
            return new ParseResult(true, m.group(1), m.group(2));
        }
        return new ParseResult(false, null, null);
    }

    private static String replaceJsonField(String body, String fieldName, String newValueEscaped)
    {
        String regex = "(\"" + Pattern.quote(fieldName) + "\"\\s*:\\s*\")([^\"]+)(\")";
        return body.replaceFirst(regex, "$1" + Matcher.quoteReplacement(newValueEscaped) + "$3");
    }

    private static String escapeForJsonString(String s)
    {
        if (s == null) return null;
        return s.replace("\\", "\\\\")
                .replace("\"", "\\\"")
                .replace("/", "\\/");
    }

    private static String unescapeJsonString(String s)
    {
        if (s == null) return null;

        s = s.replace("\\\\", "\\");
        s = s.replace("\\/", "/");
        s = s.replace("\\\"", "\"");
        s = s.replace("\\b", "\b");
        s = s.replace("\\f", "\f");
        s = s.replace("\\n", "\n");
        s = s.replace("\\r", "\r");
        s = s.replace("\\t", "\t");

        StringBuilder out = new StringBuilder();
        for (int i = 0; i < s.length(); i++)
        {
            char c = s.charAt(i);
            if (c == '\\' && i + 5 < s.length() && s.charAt(i + 1) == 'u')
            {
                String hex = s.substring(i + 2, i + 6);
                try
                {
                    int code = Integer.parseInt(hex, 16);
                    out.append((char) code);
                    i += 5;
                    continue;
                }
                catch (NumberFormatException ignored) {}
            }
            out.append(c);
        }
        return out.toString();
    }
}
