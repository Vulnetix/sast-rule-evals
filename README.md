# sast-rule-evals

Evaluation test cases for [Vulnetix CLI](https://github.com/Vulnetix/cli) built-in SAST rules.

Each directory contains a minimal code fixture designed to trigger exactly one SAST rule. Run the scanner against any fixture to verify the rule fires correctly:

```bash
vulnetix scan --path go/vnx-go-001
```

## Structure

```
<language>/
  <rule-id>/
    <manifest + source files that trigger the rule>
```

| Directory | Rule | What it tests |
|-----------|------|---------------|
| `go/vnx-go-001` | VNX-GO-001 | Missing go.sum |
| `go/vnx-go-002` | VNX-GO-002 | exec.Command with fmt.Sprintf |
| `node/vnx-node-001` | VNX-NODE-001 | Missing npm lock file |
| `node/vnx-node-002` | VNX-NODE-002 | eval() / new Function() |
| `node/vnx-node-003` | VNX-NODE-003 | child_process.exec injection |
| `node/vnx-node-004` | VNX-NODE-004 | Express without helmet |
| `node/vnx-node-005` | VNX-NODE-005 | innerHTML / dangerouslySetInnerHTML |
| `python/vnx-py-001` | VNX-PY-001 | Missing Python lock file |
| `python/vnx-py-002` | VNX-PY-002 | eval() / exec() |
| `python/vnx-py-003` | VNX-PY-003 | pickle.load / pickle.loads |
| `python/vnx-py-004` | VNX-PY-004 | yaml.load without SafeLoader |
| `python/vnx-py-005` | VNX-PY-005 | random for security operations |
| `python/vnx-py-006` | VNX-PY-006 | Django DEBUG=True |
| `ruby/vnx-ruby-001` | VNX-RUBY-001 | Missing Gemfile.lock |
| `ruby/vnx-ruby-002` | VNX-RUBY-002 | eval() / system() |
| `rust/vnx-rust-001` | VNX-RUST-001 | Missing Cargo.lock |
| `php/vnx-php-001` | VNX-PHP-001 | Missing composer.lock |
| `php/vnx-php-002` | VNX-PHP-002 | exec / system / passthru |
| `java/vnx-java-001` | VNX-JAVA-001 | Runtime.exec() with concat |
| `java/vnx-java-002` | VNX-JAVA-002 | Spring actuator exposed |
| `secrets/vnx-sec-001` | VNX-SEC-001 | AWS access key ID |
| `secrets/vnx-sec-002` | VNX-SEC-002 | Private key committed |
| `secrets/vnx-sec-004` | VNX-SEC-004 | GitHub / GitLab token |
| `docker/vnx-docker-001` | VNX-DOCKER-001 | Dockerfile missing USER |
| `docker/vnx-docker-002` | VNX-DOCKER-002 | FROM :latest tag |
| `crypto/vnx-crypto-001` | VNX-CRYPTO-001 | MD5 usage |
| `crypto/vnx-crypto-002` | VNX-CRYPTO-002 | SHA-1 usage |

## Important

All secrets, keys, and tokens in this repository are **fake test values**. They exist solely to trigger detection rules and have never been valid credentials.

## License

Apache-2.0
