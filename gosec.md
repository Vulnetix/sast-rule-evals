# Gosec Rule Evaluation Report

**Generated:** 2026-04-25  
**Tool:** `gosec dev`  
**Fixtures:** `sast-rule-evals/go/gosec-g*/`  
**Command per fixture:** `cd <fixture> && GOWORK=off gosec -fmt=json ./...`

---

## Summary

| Status | Count |
|--------|-------|
| ✅ Verified — gosec finds target rule | 60 |
| ⚠️ Partial — findings but not target rule | 0 |
| ❌ Not detected | 0 |
| 🔷 No fixture | 0 |
| **Total rules** | **60** |

---

## Rule Coverage

| Rule | Name | CWE | Fixture | Result | Notes |
|------|------|-----|---------|--------|-------|
| [G101](https://github.com/securego/gosec/blob/master/rules) | Hard-coded credentials | [798](https://cwe.mitre.org/data/definitions/798.html) | `gosec-g101` | ✅ **G101** (2 finding(s)) |  |
| [G102](https://github.com/securego/gosec/blob/master/rules) | Bind to all interfaces | [200](https://cwe.mitre.org/data/definitions/200.html) | `gosec-g102` | ✅ **G102** (1 finding(s)) |  |
| [G103](https://github.com/securego/gosec/blob/master/rules) | Use of unsafe block | [242](https://cwe.mitre.org/data/definitions/242.html) | `gosec-g103` | ✅ **G103** (1 finding(s)) |  |
| [G104](https://github.com/securego/gosec/blob/master/rules) | Errors unhandled | [703](https://cwe.mitre.org/data/definitions/703.html) | `gosec-g104` | ✅ **G104** (2 finding(s)) | also triggers: G301 |
| [G106](https://github.com/securego/gosec/blob/master/rules) | SSH InsecureIgnoreHostKey | [322](https://cwe.mitre.org/data/definitions/322.html) | `gosec-g106` | ✅ **G106** (1 finding(s)) | SSA import warning (findings still detected) |
| [G107](https://github.com/securego/gosec/blob/master/rules) | URL provided as taint input to HTTP | [88](https://cwe.mitre.org/data/definitions/88.html) | `gosec-g107` | ✅ **G107** (1 finding(s)) | also triggers: G104, G114, G704, G705 |
| [G108](https://github.com/securego/gosec/blob/master/rules) | Profiling endpoint auto-exposed | [200](https://cwe.mitre.org/data/definitions/200.html) | `gosec-g108` | ✅ **G108** (1 finding(s)) | also triggers: G104, G114 |
| [G109](https://github.com/securego/gosec/blob/master/rules) | strconv.Atoi to int32/int16 | [190](https://cwe.mitre.org/data/definitions/190.html) | `gosec-g109` | ✅ **G109** (1 finding(s)) | also triggers: G115 |
| [G110](https://github.com/securego/gosec/blob/master/rules) | Decompression bomb via io.Copy | [409](https://cwe.mitre.org/data/definitions/409.html) | `gosec-g110` | ✅ **G110** (1 finding(s)) | also triggers: G104 |
| [G111](https://github.com/securego/gosec/blob/master/rules) | http.Dir('/') path traversal | [22](https://cwe.mitre.org/data/definitions/22.html) | `gosec-g111` | ✅ **G111** (1 finding(s)) | also triggers: G104, G114 |
| [G112](https://github.com/securego/gosec/blob/master/rules) | ReadHeaderTimeout not set (slowloris) | [400](https://cwe.mitre.org/data/definitions/400.html) | `gosec-g112` | ✅ **G112** (1 finding(s)) | also triggers: G104 |
| [G113](https://github.com/securego/gosec/blob/master/rules) | Conflicting Transfer-Encoding/Content-Length | [400](https://cwe.mitre.org/data/definitions/400.html) | `gosec-g113` | ✅ **G113** (1 finding(s)) | also triggers: G104, G114 |
| [G114](https://github.com/securego/gosec/blob/master/rules) | HTTP serve without timeout | [676](https://cwe.mitre.org/data/definitions/676.html) | `gosec-g114` | ✅ **G114** (1 finding(s)) | also triggers: G104 |
| [G115](https://github.com/securego/gosec/blob/master/rules) | Integer overflow conversion | [190](https://cwe.mitre.org/data/definitions/190.html) | `gosec-g115` | ✅ **G115** (2 finding(s)) |  |
| [G116](https://github.com/securego/gosec/blob/master/rules) | Trojan Source bidirectional chars | [838](https://cwe.mitre.org/data/definitions/838.html) | `gosec-g116` | ✅ **G116** (1 finding(s)) |  |
| [G117](https://github.com/securego/gosec/blob/master/rules) | Sensitive struct field exposed via JSON | [499](https://cwe.mitre.org/data/definitions/499.html) | `gosec-g117` | ✅ **G117** (1 finding(s)) |  |
| [G118](https://github.com/securego/gosec/blob/master/rules) | Context propagation failure | [400](https://cwe.mitre.org/data/definitions/400.html) | `gosec-g118` | ✅ **G118** (1 finding(s)) | also triggers: G104, G114 |
| [G119](https://github.com/securego/gosec/blob/master/rules) | Unsafe redirect policy | [200](https://cwe.mitre.org/data/definitions/200.html) | `gosec-g119` | ✅ **G119** (1 finding(s)) |  |
| [G120](https://github.com/securego/gosec/blob/master/rules) | ParseMultipartForm without limit | [400](https://cwe.mitre.org/data/definitions/400.html) | `gosec-g120` | ✅ **G120** (1 finding(s)) | also triggers: G104, G114 |
| [G121](https://github.com/securego/gosec/blob/master/rules) | CORS AllowAll bypass | [346](https://cwe.mitre.org/data/definitions/346.html) | `gosec-g121` | ✅ **G121** (1 finding(s)) | also triggers: G104, G114 |
| [G122](https://github.com/securego/gosec/blob/master/rules) | TOCTOU race condition | [367](https://cwe.mitre.org/data/definitions/367.html) | `gosec-g122` | ✅ **G122** (1 finding(s)) |  |
| [G123](https://github.com/securego/gosec/blob/master/rules) | TLS session ticket key reuse | [295](https://cwe.mitre.org/data/definitions/295.html) | `gosec-g123` | ✅ **G123** (1 finding(s)) |  |
| [G124](https://github.com/securego/gosec/blob/master/rules) | Insecure cookie (no Secure/HttpOnly) | [614](https://cwe.mitre.org/data/definitions/614.html) | `gosec-g124` | ✅ **G124** (1 finding(s)) | also triggers: G104, G114 |
| [G201](https://github.com/securego/gosec/blob/master/rules) | SQL query via fmt.Sprintf | [89](https://cwe.mitre.org/data/definitions/89.html) | `gosec-g201` | ✅ **G201** (1 finding(s)) | also triggers: G104, G114, G701 |
| [G202](https://github.com/securego/gosec/blob/master/rules) | SQL string concatenation | [89](https://cwe.mitre.org/data/definitions/89.html) | `gosec-g202` | ✅ **G202** (1 finding(s)) | also triggers: G104, G114, G701 |
| [G203](https://github.com/securego/gosec/blob/master/rules) | Unescaped HTML in template | [79](https://cwe.mitre.org/data/definitions/79.html) | `gosec-g203` | ✅ **G203** (1 finding(s)) | also triggers: G104, G114 |
| [G204](https://github.com/securego/gosec/blob/master/rules) | Subprocess with variable args | [78](https://cwe.mitre.org/data/definitions/78.html) | `gosec-g204` | ✅ **G204** (1 finding(s)) | also triggers: G104, G114, G702, G705 |
| [G301](https://github.com/securego/gosec/blob/master/rules) | Directory created with excessive permissions | [276](https://cwe.mitre.org/data/definitions/276.html) | `gosec-g301` | ✅ **G301** (1 finding(s)) | also triggers: G104 |
| [G302](https://github.com/securego/gosec/blob/master/rules) | File chmod with excessive permissions | [276](https://cwe.mitre.org/data/definitions/276.html) | `gosec-g302` | ✅ **G302** (1 finding(s)) |  |
| [G303](https://github.com/securego/gosec/blob/master/rules) | Predictable tempfile in shared dir | [377](https://cwe.mitre.org/data/definitions/377.html) | `gosec-g303` | ✅ **G303** (1 finding(s)) |  |
| [G304](https://github.com/securego/gosec/blob/master/rules) | File path provided as taint input | [22](https://cwe.mitre.org/data/definitions/22.html) | `gosec-g304` | ✅ **G304** (1 finding(s)) | also triggers: G104, G114, G703, G705 |
| [G305](https://github.com/securego/gosec/blob/master/rules) | Zip/tar path traversal | [22](https://cwe.mitre.org/data/definitions/22.html) | `gosec-g305` | ✅ **G305** (1 finding(s)) | also triggers: G104, G301, G304 |
| [G306](https://github.com/securego/gosec/blob/master/rules) | File write with world-writable permissions | [276](https://cwe.mitre.org/data/definitions/276.html) | `gosec-g306` | ✅ **G306** (1 finding(s)) | also triggers: G104, G303 |
| [G307](https://github.com/securego/gosec/blob/master/rules) | Unsafe defer on os.Create/os.Open | [276](https://cwe.mitre.org/data/definitions/276.html) | `gosec-g307` | ✅ **G307** (1 finding(s)) | requires `-conf config.json` with `{"G307":"0600"}` |
| [G401](https://github.com/securego/gosec/blob/master/rules) | Weak hash (MD5/SHA1) | [328](https://cwe.mitre.org/data/definitions/328.html) | `gosec-g401` | ✅ **G401** (2 finding(s)) | also triggers: G501, G505 |
| [G402](https://github.com/securego/gosec/blob/master/rules) | Bad TLS configuration | [295](https://cwe.mitre.org/data/definitions/295.html) | `gosec-g402` | ✅ **G402** (1 finding(s)) |  |
| [G403](https://github.com/securego/gosec/blob/master/rules) | Weak RSA key length (<2048) | [310](https://cwe.mitre.org/data/definitions/310.html) | `gosec-g403` | ✅ **G403** (1 finding(s)) |  |
| [G404](https://github.com/securego/gosec/blob/master/rules) | Weak PRNG (math/rand) | [338](https://cwe.mitre.org/data/definitions/338.html) | `gosec-g404` | ✅ **G404** (1 finding(s)) |  |
| [G405](https://github.com/securego/gosec/blob/master/rules) | Weak cipher (DES/RC4) | [327](https://cwe.mitre.org/data/definitions/327.html) | `gosec-g405` | ✅ **G405** (1 finding(s)) | also triggers: G502 |
| [G406](https://github.com/securego/gosec/blob/master/rules) | Deprecated hash (MD4/RIPEMD-160) | [328](https://cwe.mitre.org/data/definitions/328.html) | `gosec-g406` | ✅ **G406** (1 finding(s)) | also triggers: G506 |
| [G407](https://github.com/securego/gosec/blob/master/rules) | Hardcoded IV/nonce | [1204](https://cwe.mitre.org/data/definitions/1204.html) | `gosec-g407` | ✅ **G407** (1 finding(s)) |  |
| [G408](https://github.com/securego/gosec/blob/master/rules) | SSH PublicKeyCallback abuse | [287](https://cwe.mitre.org/data/definitions/287.html) | `gosec-g408` | ✅ **G408** (1 finding(s)) |  |
| [G501](https://github.com/securego/gosec/blob/master/rules) | Import blocklist: crypto/md5 | [327](https://cwe.mitre.org/data/definitions/327.html) | `gosec-g501` | ✅ **G501** (1 finding(s)) | also triggers: G401 |
| [G502](https://github.com/securego/gosec/blob/master/rules) | Import blocklist: crypto/des | [327](https://cwe.mitre.org/data/definitions/327.html) | `gosec-g502` | ✅ **G502** (1 finding(s)) | also triggers: G405 |
| [G503](https://github.com/securego/gosec/blob/master/rules) | Import blocklist: crypto/rc4 | [327](https://cwe.mitre.org/data/definitions/327.html) | `gosec-g503` | ✅ **G503** (1 finding(s)) | also triggers: G405 |
| [G504](https://github.com/securego/gosec/blob/master/rules) | Import blocklist: net/http/cgi | [327](https://cwe.mitre.org/data/definitions/327.html) | `gosec-g504` | ✅ **G504** (1 finding(s)) |  |
| [G505](https://github.com/securego/gosec/blob/master/rules) | Import blocklist: crypto/sha1 | [327](https://cwe.mitre.org/data/definitions/327.html) | `gosec-g505` | ✅ **G505** (1 finding(s)) | also triggers: G401 |
| [G506](https://github.com/securego/gosec/blob/master/rules) | Import blocklist: x/crypto/md4 | [327](https://cwe.mitre.org/data/definitions/327.html) | `gosec-g506` | ✅ **G506** (1 finding(s)) | also triggers: G406 |
| [G507](https://github.com/securego/gosec/blob/master/rules) | Import blocklist: x/crypto/ripemd160 | [327](https://cwe.mitre.org/data/definitions/327.html) | `gosec-g507` | ✅ **G507** (1 finding(s)) | also triggers: G406 |
| [G601](https://github.com/securego/gosec/blob/master/rules) | Implicit memory aliasing in range loop | [118](https://cwe.mitre.org/data/definitions/118.html) | `gosec-g601` | ✅ **G601** (1 finding(s)) |  |
| [G602](https://github.com/securego/gosec/blob/master/rules) | Slice bounds check bypass | [118](https://cwe.mitre.org/data/definitions/118.html) | `gosec-g602` | ✅ **G602** (1 finding(s)) |  |
| [G701](https://github.com/securego/gosec/blob/master/rules) | SQL injection (taint) | [89](https://cwe.mitre.org/data/definitions/89.html) | `gosec-g701` | ✅ **G701** (1 finding(s)) | also triggers: G104, G114, G202 |
| [G702](https://github.com/securego/gosec/blob/master/rules) | Command injection (taint) | [78](https://cwe.mitre.org/data/definitions/78.html) | `gosec-g702` | ✅ **G702** (1 finding(s)) | also triggers: G104, G114, G204, G705 |
| [G703](https://github.com/securego/gosec/blob/master/rules) | Path traversal (taint) | [22](https://cwe.mitre.org/data/definitions/22.html) | `gosec-g703` | ✅ **G703** (1 finding(s)) | also triggers: G104, G114, G304, G705 |
| [G704](https://github.com/securego/gosec/blob/master/rules) | SSRF (taint) | [918](https://cwe.mitre.org/data/definitions/918.html) | `gosec-g704` | ✅ **G704** (1 finding(s)) | also triggers: G104, G107, G114, G705 |
| [G705](https://github.com/securego/gosec/blob/master/rules) | XSS (taint) | [79](https://cwe.mitre.org/data/definitions/79.html) | `gosec-g705` | ✅ **G705** (1 finding(s)) | also triggers: G104, G114 |
| [G706](https://github.com/securego/gosec/blob/master/rules) | Log injection (taint) | [117](https://cwe.mitre.org/data/definitions/117.html) | `gosec-g706` | ✅ **G706** (1 finding(s)) | also triggers: G104, G114 |
| [G707](https://github.com/securego/gosec/blob/master/rules) | SMTP injection (taint) | [93](https://cwe.mitre.org/data/definitions/93.html) | `gosec-g707` | ✅ **G707** (1 finding(s)) | also triggers: G104, G114 |
| [G708](https://github.com/securego/gosec/blob/master/rules) | Server-side template injection (taint) | [94](https://cwe.mitre.org/data/definitions/94.html) | `gosec-g708` | ✅ **G708** (1 finding(s)) | also triggers: G104, G114 |
| [G709](https://github.com/securego/gosec/blob/master/rules) | Unsafe deserialization (taint) | [502](https://cwe.mitre.org/data/definitions/502.html) | `gosec-g709` | ✅ **G709** (1 finding(s)) | also triggers: G104, G114 |

---

## Findings Detail

Each fixture that successfully triggered its target rule:

### gosec-g101 → G101- Line 9: Potential hardcoded credentials *(sev=HIGH, conf=LOW)*- Line 8: Potential hardcoded credentials *(sev=HIGH, conf=LOW)*
### gosec-g102 → G102- Line 10: Binds to all network interfaces *(sev=MEDIUM, conf=HIGH)*
### gosec-g103 → G103- Line 11: Use of unsafe calls should be audited *(sev=LOW, conf=HIGH)*
### gosec-g104 → G104- Line 8: Errors unhandled *(sev=LOW, conf=HIGH)*- Line 7: Errors unhandled *(sev=LOW, conf=HIGH)*
### gosec-g106 → G106- Line 12: Use of ssh InsecureIgnoreHostKey should be audited *(sev=MEDIUM, conf=HIGH)*
### gosec-g107 → G107- Line 11: Potential HTTP request made with variable url *(sev=MEDIUM, conf=MEDIUM)*
### gosec-g108 → G108- Line 5: Profiling endpoint is automatically exposed on /debug/pprof *(sev=HIGH, conf=HIGH)*
### gosec-g109 → G109- Line 14: Potential Integer overflow made by strconv.Atoi result conversion to int16/32 *(sev=HIGH, conf=MEDIUM)*
### gosec-g110 → G110- Line 24: Potential DoS vulnerability via decompression bomb *(sev=MEDIUM, conf=MEDIUM)*
### gosec-g111 → G111- Line 7: Potential directory traversal *(sev=MEDIUM, conf=MEDIUM)*
### gosec-g112 → G112- Line 7-9: Potential Slowloris Attack because ReadHeaderTimeout is not configured in the ht *(sev=MEDIUM, conf=LOW)*
### gosec-g113 → G113- Line 9: Setting both Transfer-Encoding and Content-Length headers may enable request smu *(sev=HIGH, conf=HIGH)*
### gosec-g114 → G114- Line 7: Use of net/http serve function that has no support for setting timeouts *(sev=MEDIUM, conf=HIGH)*
### gosec-g115 → G115- Line 10: integer overflow conversion int -> int32 *(sev=HIGH, conf=MEDIUM)*- Line 11: integer overflow conversion int -> int16 *(sev=HIGH, conf=MEDIUM)*
### gosec-g116 → G116- Line 1-9: Potential Trojan Source vulnerability via use of bidirectional text control char *(sev=HIGH, conf=MEDIUM)*
### gosec-g117 → G117- Line 13: Marshaled struct field "Password" (JSON key "password") matches secret pattern *(sev=MEDIUM, conf=MEDIUM)*
### gosec-g118 → G118- Line 13: Goroutine uses context.Background/TODO while request-scoped context is available *(sev=HIGH, conf=MEDIUM)*
### gosec-g119 → G119- Line 10: Unsafe redirect policy may propagate sensitive headers across origins *(sev=HIGH, conf=HIGH)*
### gosec-g120 → G120- Line 9: Unbounded form parsing in HTTP handlers can cause memory exhaustion *(sev=MEDIUM, conf=HIGH)*
### gosec-g121 → G121- Line 9: Overbroad AddInsecureBypassPattern disables cross-origin protections for too man *(sev=HIGH, conf=HIGH)*
### gosec-g122 → G122- Line 15: Filesystem operation in filepath.Walk/WalkDir callback uses race-prone path; con *(sev=HIGH, conf=MEDIUM)*
### gosec-g123 → G123- Line 13: tls.Config uses VerifyPeerCertificate while session resumption may remain enable *(sev=HIGH, conf=HIGH)*
### gosec-g124 → G124- Line 9: http.Cookie missing or has insecure Secure, HttpOnly, or SameSite attribute *(sev=MEDIUM, conf=HIGH)*
### gosec-g201 → G201- Line 14: SQL string formatting *(sev=MEDIUM, conf=HIGH)*
### gosec-g202 → G202- Line 14: SQL string concatenation *(sev=MEDIUM, conf=HIGH)*
### gosec-g203 → G203- Line 12: The used method does not auto-escape HTML. This can potentially lead to 'Cross-s *(sev=MEDIUM, conf=LOW)*
### gosec-g204 → G204- Line 12: Subprocess launched with variable *(sev=MEDIUM, conf=HIGH)*
### gosec-g301 → G301- Line 7: Expect directory permissions to be 0750 or less *(sev=MEDIUM, conf=HIGH)*
### gosec-g302 → G302- Line 7: Expect file permissions to be 0600 or less *(sev=MEDIUM, conf=HIGH)*
### gosec-g303 → G303- Line 10: File creation in shared tmp directory without using ioutil.Tempfile *(sev=MEDIUM, conf=HIGH)*
### gosec-g304 → G304- Line 12: Potential file inclusion via variable *(sev=MEDIUM, conf=HIGH)*
### gosec-g305 → G305- Line 19: File traversal when extracting zip/tar archive *(sev=MEDIUM, conf=HIGH)*
### gosec-g306 → G306- Line 7: Expect WriteFile permissions to be 0600 or less *(sev=MEDIUM, conf=HIGH)*
### gosec-g307 → G307- Line 11: Expect file permissions to be 0600 or less but os.Create used with default permi *(sev=MEDIUM, conf=HIGH)*
### gosec-g401 → G401- Line 14: Use of weak cryptographic primitive *(sev=MEDIUM, conf=HIGH)*- Line 11: Use of weak cryptographic primitive *(sev=MEDIUM, conf=HIGH)*
### gosec-g402 → G402- Line 13: TLS InsecureSkipVerify set to true. *(sev=HIGH, conf=HIGH)*
### gosec-g403 → G403- Line 11: RSA keys should be at least 2048 bits *(sev=MEDIUM, conf=HIGH)*
### gosec-g404 → G404- Line 10: Use of weak random number generator (math/rand or math/rand/v2 instead of crypto *(sev=HIGH, conf=MEDIUM)*
### gosec-g405 → G405- Line 11: Use of weak cryptographic primitive *(sev=MEDIUM, conf=HIGH)*
### gosec-g406 → G406- Line 10: Use of deprecated weak cryptographic primitive *(sev=MEDIUM, conf=HIGH)*
### gosec-g407 → G407- Line 13: Use of hardcoded IV/nonce for encryption by passing hardcoded slice/array by pas *(sev=HIGH, conf=HIGH)*
### gosec-g408 → G408- Line 11: Stateful misuse of ssh.PublicKeyCallback leading to auth bypass *(sev=HIGH, conf=HIGH)*
### gosec-g501 → G501- Line 4: Blocklisted import crypto/md5: weak cryptographic primitive *(sev=MEDIUM, conf=HIGH)*
### gosec-g502 → G502- Line 4: Blocklisted import crypto/des: weak cryptographic primitive *(sev=MEDIUM, conf=HIGH)*
### gosec-g503 → G503- Line 4: Blocklisted import crypto/rc4: weak cryptographic primitive *(sev=MEDIUM, conf=HIGH)*
### gosec-g504 → G504- Line 5: Blocklisted import net/http/cgi: Go versions < 1.6.3 are vulnerable to Httpoxy a *(sev=MEDIUM, conf=HIGH)*
### gosec-g505 → G505- Line 4: Blocklisted import crypto/sha1: weak cryptographic primitive *(sev=MEDIUM, conf=HIGH)*
### gosec-g506 → G506- Line 6: Blocklisted import golang.org/x/crypto/md4: deprecated and weak cryptographic pr *(sev=MEDIUM, conf=HIGH)*
### gosec-g507 → G507- Line 6: Blocklisted import golang.org/x/crypto/ripemd160: deprecated and weak cryptograp *(sev=MEDIUM, conf=HIGH)*
### gosec-g601 → G601- Line 9: Implicit memory aliasing in for loop. *(sev=MEDIUM, conf=MEDIUM)*
### gosec-g602 → G602- Line 7: slice bounds out of range *(sev=LOW, conf=HIGH)*
### gosec-g701 → G701- Line 14: SQL injection via taint analysis *(sev=HIGH, conf=HIGH)*
### gosec-g702 → G702- Line 11: Command injection via taint analysis *(sev=HIGH, conf=HIGH)*
### gosec-g703 → G703- Line 11: Path traversal via taint analysis *(sev=HIGH, conf=HIGH)*
### gosec-g704 → G704- Line 11: SSRF via taint analysis *(sev=HIGH, conf=HIGH)*
### gosec-g705 → G705- Line 12: XSS via taint analysis *(sev=MEDIUM, conf=HIGH)*
### gosec-g706 → G706- Line 10: Log injection via taint analysis *(sev=LOW, conf=HIGH)*
### gosec-g707 → G707- Line 13: SMTP command/header injection via taint analysis *(sev=HIGH, conf=HIGH)*
### gosec-g708 → G708- Line 11: Server-side template injection via taint analysis *(sev=HIGH, conf=HIGH)*
### gosec-g709 → G709- Line 16: Unsafe deserialization of untrusted data via taint analysis *(sev=HIGH, conf=HIGH)*

---

## Notes

- **G307** requires a gosec config file: `echo '{"G307":"0600"}' > config.json && GOWORK=off gosec -conf config.json ./...`
- **G106**, **G406**, **G408**, **G506**, **G507** use `golang.org/x/crypto` — gosec reports an SSA import warning but still finds the target rule.
- Fixtures for taint-analysis rules (G701–G709) also trigger G104/G114 co-findings because they use `http.ListenAndServe` and bare error discards to wire up the vulnerable HTTP handler.
- All fixtures use `go 1.21` to ensure Go 1.22 range-variable semantics do not suppress G601 findings.

---

## How to Re-run

```bash
cd sast-rule-evals/go
for dir in gosec-g*/; do
  rule=$(basename "$dir")
  (cd "$dir" && GOWORK=off gosec -fmt=json ./...) > /tmp/gosec-${rule}.json
done
```

For G307 specifically:
```bash
cd sast-rule-evals/go/gosec-g307
echo '{"G307":"0600"}' > config.json
GOWORK=off gosec -conf config.json -fmt=json ./...
```
