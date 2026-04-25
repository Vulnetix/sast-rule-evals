# Gosec CLI vs Vulnetix SAST — Timing Comparison

**Generated:** 2026-04-25  
**Fixtures:** 60 × `sast-rule-evals/go/gosec-g*/`  
**Vulnetix flags:** `--rule Vulnetix/opa-gosec --disable-default-rules`  
**Gosec flags:** `GOWORK=off gosec -fmt=json ./...` (per-fixture directory)  
**System:** Single run, wall-clock milliseconds, no warm-up

## Summary

| Metric | gosec CLI | vulnetix SAST | Ratio (vnx/gosec) |
|--------|-----------|---------------|-------------------|
| Total (60 fixtures) | 19,398 ms (19.4 s) | 40,719 ms (40.7 s) | 2.10× |
| Mean per fixture | 323 ms | 679 ms | 2.10× |
| Median per fixture | 323 ms | 678 ms | 2.10× |
| Min | 127 ms | 612 ms | — |
| Max | 930 ms | 762 ms | — |

## Notes

- gosec spawns a Go build and type-checks each package; its startup cost scales with
  dependency graph size and cache warmth.
- vulnetix SAST has a fixed per-invocation overhead (~650 ms) for OPA rule loading and
  file traversal; the actual Rego evaluation on a single `main.go` is sub-millisecond.
- For large codebases vulnetix's constant overhead amortises across many files, while
  gosec's cost grows with the size and complexity of the Go package graph.
- gosec benefits significantly from a warm `GOMODCACHE`; cold runs would be much slower.

## Per-Rule Results

| Rule | gosec (ms) | vulnetix (ms) | Faster |
|------|-----------|----------------|--------|
| gosec-g101 | 930 | 725 | vulnetix |
| gosec-g102 | 412 | 689 | gosec |
| gosec-g103 | 308 | 712 | gosec |
| gosec-g104 | 214 | 635 | gosec |
| gosec-g106 | 305 | 642 | gosec |
| gosec-g107 | 587 | 667 | gosec |
| gosec-g108 | 377 | 671 | gosec |
| gosec-g109 | 171 | 762 | gosec |
| gosec-g110 | 310 | 681 | gosec |
| gosec-g111 | 358 | 660 | gosec |
| gosec-g112 | 357 | 693 | gosec |
| gosec-g113 | 268 | 689 | gosec |
| gosec-g114 | 337 | 657 | gosec |
| gosec-g115 | 263 | 670 | gosec |
| gosec-g116 | 140 | 697 | gosec |
| gosec-g117 | 322 | 689 | gosec |
| gosec-g118 | 407 | 655 | gosec |
| gosec-g119 | 399 | 674 | gosec |
| gosec-g120 | 259 | 679 | gosec |
| gosec-g121 | 353 | 698 | gosec |
| gosec-g122 | 332 | 618 | gosec |
| gosec-g123 | 391 | 675 | gosec |
| gosec-g124 | 300 | 668 | gosec |
| gosec-g201 | 374 | 705 | gosec |
| gosec-g202 | 364 | 655 | gosec |
| gosec-g203 | 351 | 664 | gosec |
| gosec-g204 | 295 | 672 | gosec |
| gosec-g301 | 275 | 666 | gosec |
| gosec-g302 | 343 | 698 | gosec |
| gosec-g303 | 127 | 650 | gosec |
| gosec-g304 | 384 | 682 | gosec |
| gosec-g305 | 308 | 612 | gosec |
| gosec-g306 | 300 | 633 | gosec |
| gosec-g307 | 284 | 629 | gosec |
| gosec-g401 | 332 | 685 | gosec |
| gosec-g402 | 351 | 716 | gosec |
| gosec-g403 | 169 | 674 | gosec |
| gosec-g404 | 278 | 704 | gosec |
| gosec-g405 | 290 | 720 | gosec |
| gosec-g406 | 234 | 653 | gosec |
| gosec-g407 | 324 | 627 | gosec |
| gosec-g408 | 365 | 657 | gosec |
| gosec-g501 | 339 | 727 | gosec |
| gosec-g502 | 190 | 682 | gosec |
| gosec-g503 | 301 | 714 | gosec |
| gosec-g504 | 398 | 653 | gosec |
| gosec-g505 | 305 | 642 | gosec |
| gosec-g506 | 254 | 634 | gosec |
| gosec-g507 | 316 | 718 | gosec |
| gosec-g601 | 266 | 701 | gosec |
| gosec-g602 | 161 | 708 | gosec |
| gosec-g701 | 375 | 637 | gosec |
| gosec-g702 | 338 | 729 | gosec |
| gosec-g703 | 374 | 706 | gosec |
| gosec-g704 | 253 | 737 | gosec |
| gosec-g705 | 376 | 663 | gosec |
| gosec-g706 | 355 | 718 | gosec |
| gosec-g707 | 363 | 676 | gosec |
| gosec-g708 | 232 | 680 | gosec |
| gosec-g709 | 354 | 686 | gosec |

**gosec faster:** 59/60 fixtures  
**vulnetix faster:** 1/60 fixtures
