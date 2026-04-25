# Ruff Rule Evaluation Report
Generated: 2026-04-25
Ruff command: `ruff check --select ALL --preview`

## Summary

| Category | Count |
|---|---|
| PASS | 932 |
| PASS-VIA-ALIAS | 9 |
| CONVENTION-CONFLICT | 2 |
| REMOVED | 10 |
| UNTRIGGERABLE | 3 |
| MISS | 0 |
| NO_SAMPLE | 0 |
| **Total rules** | **956** |

## Coverage
`941 / 956 rules detected by ruff (98.4%)`
`943 / 956 rules have verified sample coverage (98.6%)`

All 956 rules have sample directories. Zero rules are unaccounted for.

## PASS — Rules detected directly (932)

<details><summary>Show all 932 passing rules</summary>

| Code | Name | Linter |
|---|---|---|
| A001 | builtin-variable-shadowing | flake8-builtins |
| A002 | builtin-argument-shadowing | flake8-builtins |
| A003 | builtin-attribute-shadowing | flake8-builtins |
| A004 | builtin-import-shadowing | flake8-builtins |
| A005 | stdlib-module-shadowing | flake8-builtins |
| A006 | builtin-lambda-argument-shadowing | flake8-builtins |
| AIR001 | airflow-variable-name-task-id-mismatch | Airflow |
| AIR002 | airflow-dag-no-schedule-argument | Airflow |
| AIR003 | airflow-variable-get-outside-task | Airflow |
| AIR004 | airflow-task-branch-as-short-circuit | Airflow |
| AIR201 | airflow-xcom-pull-in-template-string | Airflow |
| AIR301 | airflow3-removal | Airflow |
| AIR302 | airflow3-moved-to-provider | Airflow |
| AIR303 | airflow3-incompatible-function-signature | Airflow |
| AIR304 | airflow3-dag-dynamic-value | Airflow |
| AIR311 | airflow3-suggested-update | Airflow |
| AIR312 | airflow3-suggested-to-move-to-provider | Airflow |
| AIR321 | airflow31-moved | Airflow |
| ANN001 | missing-type-function-argument | flake8-annotations |
| ANN002 | missing-type-args | flake8-annotations |
| ANN003 | missing-type-kwargs | flake8-annotations |
| ANN201 | missing-return-type-undocumented-public-function | flake8-annotations |
| ANN202 | missing-return-type-private-function | flake8-annotations |
| ANN204 | missing-return-type-special-method | flake8-annotations |
| ANN205 | missing-return-type-static-method | flake8-annotations |
| ANN206 | missing-return-type-class-method | flake8-annotations |
| ANN401 | any-type | flake8-annotations |
| ARG001 | unused-function-argument | flake8-unused-arguments |
| ARG002 | unused-method-argument | flake8-unused-arguments |
| ARG003 | unused-class-method-argument | flake8-unused-arguments |
| ARG004 | unused-static-method-argument | flake8-unused-arguments |
| ARG005 | unused-lambda-argument | flake8-unused-arguments |
| ASYNC100 | cancel-scope-no-checkpoint | flake8-async |
| ASYNC105 | trio-sync-call | flake8-async |
| ASYNC109 | async-function-with-timeout | flake8-async |
| ASYNC110 | async-busy-wait | flake8-async |
| ASYNC115 | async-zero-sleep | flake8-async |
| ASYNC116 | long-sleep-not-forever | flake8-async |
| ASYNC210 | blocking-http-call-in-async-function | flake8-async |
| ASYNC212 | blocking-http-call-httpx-in-async-function | flake8-async |
| ASYNC220 | create-subprocess-in-async-function | flake8-async |
| ASYNC221 | run-process-in-async-function | flake8-async |
| ASYNC222 | wait-for-process-in-async-function | flake8-async |
| ASYNC230 | blocking-open-call-in-async-function | flake8-async |
| ASYNC240 | blocking-path-method-in-async-function | flake8-async |
| ASYNC250 | blocking-input-in-async-function | flake8-async |
| ASYNC251 | blocking-sleep-in-async-function | flake8-async |
| B002 | unary-prefix-increment-decrement | flake8-bugbear |
| B003 | assignment-to-os-environ | flake8-bugbear |
| B004 | unreliable-callable-check | flake8-bugbear |
| B005 | strip-with-multi-characters | flake8-bugbear |
| B006 | mutable-argument-default | flake8-bugbear |
| B007 | unused-loop-control-variable | flake8-bugbear |
| B008 | function-call-in-default-argument | flake8-bugbear |
| B009 | get-attr-with-constant | flake8-bugbear |
| B010 | set-attr-with-constant | flake8-bugbear |
| B011 | assert-false | flake8-bugbear |
| B012 | jump-statement-in-finally | flake8-bugbear |
| B013 | redundant-tuple-in-exception-handler | flake8-bugbear |
| B014 | duplicate-handler-exception | flake8-bugbear |
| B015 | useless-comparison | flake8-bugbear |
| B016 | raise-literal | flake8-bugbear |
| B017 | assert-raises-exception | flake8-bugbear |
| B018 | useless-expression | flake8-bugbear |
| B019 | cached-instance-method | flake8-bugbear |
| B020 | loop-variable-overrides-iterator | flake8-bugbear |
| B021 | f-string-docstring | flake8-bugbear |
| B022 | useless-contextlib-suppress | flake8-bugbear |
| B023 | function-uses-loop-variable | flake8-bugbear |
| B024 | abstract-base-class-without-abstract-method | flake8-bugbear |
| B025 | duplicate-try-block-exception | flake8-bugbear |
| B026 | star-arg-unpacking-after-keyword-arg | flake8-bugbear |
| B027 | empty-method-without-abstract-decorator | flake8-bugbear |
| B028 | no-explicit-stacklevel | flake8-bugbear |
| B029 | except-with-empty-tuple | flake8-bugbear |
| B030 | except-with-non-exception-classes | flake8-bugbear |
| B031 | reuse-of-groupby-generator | flake8-bugbear |
| B032 | unintentional-type-annotation | flake8-bugbear |
| B033 | duplicate-value | flake8-bugbear |
| B034 | re-sub-positional-args | flake8-bugbear |
| B035 | static-key-dict-comprehension | flake8-bugbear |
| B039 | mutable-contextvar-default | flake8-bugbear |
| B043 | del-attr-with-constant | flake8-bugbear |
| B901 | return-in-generator | flake8-bugbear |
| B903 | class-as-data-structure | flake8-bugbear |
| B904 | raise-without-from-inside-except | flake8-bugbear |
| B905 | zip-without-explicit-strict | flake8-bugbear |
| B909 | loop-iterator-mutation | flake8-bugbear |
| B911 | batched-without-explicit-strict | flake8-bugbear |
| B912 | map-without-explicit-strict | flake8-bugbear |
| BLE001 | blind-except | flake8-blind-except |
| C400 | unnecessary-generator-list | flake8-comprehensions |
| C401 | unnecessary-generator-set | flake8-comprehensions |
| C402 | unnecessary-generator-dict | flake8-comprehensions |
| C403 | unnecessary-list-comprehension-set | flake8-comprehensions |
| C404 | unnecessary-list-comprehension-dict | flake8-comprehensions |
| C405 | unnecessary-literal-set | flake8-comprehensions |
| C406 | unnecessary-literal-dict | flake8-comprehensions |
| C408 | unnecessary-collection-call | flake8-comprehensions |
| C409 | unnecessary-literal-within-tuple-call | flake8-comprehensions |
| C410 | unnecessary-literal-within-list-call | flake8-comprehensions |
| C411 | unnecessary-list-call | flake8-comprehensions |
| C413 | unnecessary-call-around-sorted | flake8-comprehensions |
| C414 | unnecessary-double-cast-or-process | flake8-comprehensions |
| C415 | unnecessary-subscript-reversal | flake8-comprehensions |
| C416 | unnecessary-comprehension | flake8-comprehensions |
| C417 | unnecessary-map | flake8-comprehensions |
| C418 | unnecessary-literal-within-dict-call | flake8-comprehensions |
| C419 | unnecessary-comprehension-in-call | flake8-comprehensions |
| C420 | unnecessary-dict-comprehension-for-iterable | flake8-comprehensions |
| C901 | complex-structure | mccabe |
| COM812 | missing-trailing-comma | flake8-commas |
| COM818 | trailing-comma-on-bare-tuple | flake8-commas |
| COM819 | prohibited-trailing-comma | flake8-commas |
| CPY001 | missing-copyright-notice | flake8-copyright |
| D100 | undocumented-public-module | pydocstyle |
| D101 | undocumented-public-class | pydocstyle |
| D102 | undocumented-public-method | pydocstyle |
| D103 | undocumented-public-function | pydocstyle |
| D104 | undocumented-public-package | pydocstyle |
| D105 | undocumented-magic-method | pydocstyle |
| D106 | undocumented-public-nested-class | pydocstyle |
| D107 | undocumented-public-init | pydocstyle |
| D200 | unnecessary-multiline-docstring | pydocstyle |
| D201 | blank-line-before-function | pydocstyle |
| D202 | blank-line-after-function | pydocstyle |
| D204 | incorrect-blank-line-after-class | pydocstyle |
| D205 | missing-blank-line-after-summary | pydocstyle |
| D206 | docstring-tab-indentation | pydocstyle |
| D207 | under-indentation | pydocstyle |
| D208 | over-indentation | pydocstyle |
| D209 | new-line-after-last-paragraph | pydocstyle |
| D210 | surrounding-whitespace | pydocstyle |
| D211 | blank-line-before-class | pydocstyle |
| D212 | multi-line-summary-first-line | pydocstyle |
| D214 | overindented-section | pydocstyle |
| D215 | overindented-section-underline | pydocstyle |
| D300 | triple-single-quotes | pydocstyle |
| D301 | escape-sequence-in-docstring | pydocstyle |
| D400 | missing-trailing-period | pydocstyle |
| D401 | non-imperative-mood | pydocstyle |
| D402 | signature-in-docstring | pydocstyle |
| D403 | first-word-uncapitalized | pydocstyle |
| D404 | docstring-starts-with-this | pydocstyle |
| D405 | non-capitalized-section-name | pydocstyle |
| D406 | missing-new-line-after-section-name | pydocstyle |
| D407 | missing-dashed-underline-after-section | pydocstyle |
| D408 | missing-section-underline-after-name | pydocstyle |
| D409 | mismatched-section-underline-length | pydocstyle |
| D410 | no-blank-line-after-section | pydocstyle |
| D411 | no-blank-line-before-section | pydocstyle |
| D412 | blank-lines-between-header-and-content | pydocstyle |
| D413 | missing-blank-line-after-last-section | pydocstyle |
| D414 | empty-docstring-section | pydocstyle |
| D415 | missing-terminal-punctuation | pydocstyle |
| D416 | missing-section-name-colon | pydocstyle |
| D417 | undocumented-param | pydocstyle |
| D418 | overload-with-docstring | pydocstyle |
| D419 | empty-docstring | pydocstyle |
| D420 | incorrect-section-order | pydocstyle |
| DJ001 | django-nullable-model-string-field | flake8-django |
| DJ003 | django-locals-in-render-function | flake8-django |
| DJ006 | django-exclude-with-model-form | flake8-django |
| DJ007 | django-all-with-model-form | flake8-django |
| DJ008 | django-model-without-dunder-str | flake8-django |
| DJ012 | django-unordered-body-content-in-model | flake8-django |
| DJ013 | django-non-leading-receiver-decorator | flake8-django |
| DOC102 | docstring-extraneous-parameter | pydoclint |
| DOC201 | docstring-missing-returns | pydoclint |
| DOC202 | docstring-extraneous-returns | pydoclint |
| DOC402 | docstring-missing-yields | pydoclint |
| DOC403 | docstring-extraneous-yields | pydoclint |
| DOC501 | docstring-missing-exception | pydoclint |
| DOC502 | docstring-extraneous-exception | pydoclint |
| DTZ001 | call-datetime-without-tzinfo | flake8-datetimez |
| DTZ002 | call-datetime-today | flake8-datetimez |
| DTZ003 | call-datetime-utcnow | flake8-datetimez |
| DTZ004 | call-datetime-utcfromtimestamp | flake8-datetimez |
| DTZ005 | call-datetime-now-without-tzinfo | flake8-datetimez |
| DTZ006 | call-datetime-fromtimestamp | flake8-datetimez |
| DTZ007 | call-datetime-strptime-without-zone | flake8-datetimez |
| DTZ011 | call-date-today | flake8-datetimez |
| DTZ012 | call-date-fromtimestamp | flake8-datetimez |
| DTZ901 | datetime-min-max | flake8-datetimez |
| E101 | mixed-spaces-and-tabs | pycodestyle |
| E111 | indentation-with-invalid-multiple | pycodestyle |
| E112 | no-indented-block | pycodestyle |
| E113 | unexpected-indentation | pycodestyle |
| E114 | indentation-with-invalid-multiple-comment | pycodestyle |
| E115 | no-indented-block-comment | pycodestyle |
| E116 | unexpected-indentation-comment | pycodestyle |
| E117 | over-indented | pycodestyle |
| E201 | whitespace-after-open-bracket | pycodestyle |
| E202 | whitespace-before-close-bracket | pycodestyle |
| E203 | whitespace-before-punctuation | pycodestyle |
| E204 | whitespace-after-decorator | pycodestyle |
| E211 | whitespace-before-parameters | pycodestyle |
| E221 | multiple-spaces-before-operator | pycodestyle |
| E222 | multiple-spaces-after-operator | pycodestyle |
| E223 | tab-before-operator | pycodestyle |
| E224 | tab-after-operator | pycodestyle |
| E225 | missing-whitespace-around-operator | pycodestyle |
| E226 | missing-whitespace-around-arithmetic-operator | pycodestyle |
| E227 | missing-whitespace-around-bitwise-or-shift-operator | pycodestyle |
| E228 | missing-whitespace-around-modulo-operator | pycodestyle |
| E231 | missing-whitespace | pycodestyle |
| E241 | multiple-spaces-after-comma | pycodestyle |
| E242 | tab-after-comma | pycodestyle |
| E251 | unexpected-spaces-around-keyword-parameter-equals | pycodestyle |
| E252 | missing-whitespace-around-parameter-equals | pycodestyle |
| E261 | too-few-spaces-before-inline-comment | pycodestyle |
| E262 | no-space-after-inline-comment | pycodestyle |
| E265 | no-space-after-block-comment | pycodestyle |
| E266 | multiple-leading-hashes-for-block-comment | pycodestyle |
| E271 | multiple-spaces-after-keyword | pycodestyle |
| E272 | multiple-spaces-before-keyword | pycodestyle |
| E273 | tab-after-keyword | pycodestyle |
| E274 | tab-before-keyword | pycodestyle |
| E275 | missing-whitespace-after-keyword | pycodestyle |
| E301 | blank-line-between-methods | pycodestyle |
| E302 | blank-lines-top-level | pycodestyle |
| E303 | too-many-blank-lines | pycodestyle |
| E304 | blank-line-after-decorator | pycodestyle |
| E305 | blank-lines-after-function-or-class | pycodestyle |
| E306 | blank-lines-before-nested-definition | pycodestyle |
| E401 | multiple-imports-on-one-line | pycodestyle |
| E402 | module-import-not-at-top-of-file | pycodestyle |
| E501 | line-too-long | pycodestyle |
| E502 | redundant-backslash | pycodestyle |
| E701 | multiple-statements-on-one-line-colon | pycodestyle |
| E702 | multiple-statements-on-one-line-semicolon | pycodestyle |
| E703 | useless-semicolon | pycodestyle |
| E711 | none-comparison | pycodestyle |
| E712 | true-false-comparison | pycodestyle |
| E713 | not-in-test | pycodestyle |
| E714 | not-is-test | pycodestyle |
| E721 | type-comparison | pycodestyle |
| E722 | bare-except | pycodestyle |
| E731 | lambda-assignment | pycodestyle |
| E741 | ambiguous-variable-name | pycodestyle |
| E742 | ambiguous-class-name | pycodestyle |
| E743 | ambiguous-function-name | pycodestyle |
| EM101 | raw-string-in-exception | flake8-errmsg |
| EM102 | f-string-in-exception | flake8-errmsg |
| EM103 | dot-format-in-exception | flake8-errmsg |
| ERA001 | commented-out-code | eradicate |
| EXE001 | shebang-not-executable | flake8-executable |
| EXE002 | shebang-missing-executable-file | flake8-executable |
| EXE003 | shebang-missing-python | flake8-executable |
| EXE004 | shebang-leading-whitespace | flake8-executable |
| EXE005 | shebang-not-first-line | flake8-executable |
| F401 | unused-import | Pyflakes |
| F402 | import-shadowed-by-loop-var | Pyflakes |
| F403 | undefined-local-with-import-star | Pyflakes |
| F404 | late-future-import | Pyflakes |
| F405 | undefined-local-with-import-star-usage | Pyflakes |
| F406 | undefined-local-with-nested-import-star-usage | Pyflakes |
| F407 | future-feature-not-defined | Pyflakes |
| F501 | percent-format-invalid-format | Pyflakes |
| F502 | percent-format-expected-mapping | Pyflakes |
| F503 | percent-format-expected-sequence | Pyflakes |
| F504 | percent-format-extra-named-arguments | Pyflakes |
| F505 | percent-format-missing-argument | Pyflakes |
| F506 | percent-format-mixed-positional-and-named | Pyflakes |
| F507 | percent-format-positional-count-mismatch | Pyflakes |
| F508 | percent-format-star-requires-sequence | Pyflakes |
| F509 | percent-format-unsupported-format-character | Pyflakes |
| F521 | string-dot-format-invalid-format | Pyflakes |
| F522 | string-dot-format-extra-named-arguments | Pyflakes |
| F523 | string-dot-format-extra-positional-arguments | Pyflakes |
| F524 | string-dot-format-missing-arguments | Pyflakes |
| F525 | string-dot-format-mixing-automatic | Pyflakes |
| F541 | f-string-missing-placeholders | Pyflakes |
| F601 | multi-value-repeated-key-literal | Pyflakes |
| F602 | multi-value-repeated-key-variable | Pyflakes |
| F622 | multiple-starred-expressions | Pyflakes |
| F631 | assert-tuple | Pyflakes |
| F632 | is-literal | Pyflakes |
| F633 | invalid-print-syntax | Pyflakes |
| F634 | if-tuple | Pyflakes |
| F701 | break-outside-loop | Pyflakes |
| F702 | continue-outside-loop | Pyflakes |
| F704 | yield-outside-function | Pyflakes |
| F706 | return-outside-function | Pyflakes |
| F707 | default-except-not-last | Pyflakes |
| F722 | forward-annotation-syntax-error | Pyflakes |
| F811 | redefined-while-unused | Pyflakes |
| F821 | undefined-name | Pyflakes |
| F822 | undefined-export | Pyflakes |
| F823 | undefined-local | Pyflakes |
| F841 | unused-variable | Pyflakes |
| F842 | unused-annotation | Pyflakes |
| F901 | raise-not-implemented | Pyflakes |
| FA100 | future-rewritable-type-annotation | flake8-future-annotations |
| FA102 | future-required-type-annotation | flake8-future-annotations |
| FAST001 | fast-api-redundant-response-model | FastAPI |
| FAST002 | fast-api-non-annotated-dependency | FastAPI |
| FAST003 | fast-api-unused-path-parameter | FastAPI |
| FBT001 | boolean-type-hint-positional-argument | flake8-boolean-trap |
| FBT002 | boolean-default-value-positional-argument | flake8-boolean-trap |
| FBT003 | boolean-positional-value-in-call | flake8-boolean-trap |
| FIX001 | line-contains-fixme | flake8-fixme |
| FIX002 | line-contains-todo | flake8-fixme |
| FIX003 | line-contains-xxx | flake8-fixme |
| FIX004 | line-contains-hack | flake8-fixme |
| FLY002 | static-join-to-f-string | flynt |
| FURB101 | read-whole-file | refurb |
| FURB103 | write-whole-file | refurb |
| FURB105 | print-empty-string | refurb |
| FURB110 | if-exp-instead-of-or-operator | refurb |
| FURB113 | repeated-append | refurb |
| FURB116 | f-string-number-format | refurb |
| FURB118 | reimplemented-operator | refurb |
| FURB122 | for-loop-writes | refurb |
| FURB129 | readlines-in-for | refurb |
| FURB131 | delete-full-slice | refurb |
| FURB132 | check-and-remove-from-set | refurb |
| FURB136 | if-expr-min-max | refurb |
| FURB140 | reimplemented-starmap | refurb |
| FURB142 | for-loop-set-mutations | refurb |
| FURB145 | slice-copy | refurb |
| FURB148 | unnecessary-enumerate | refurb |
| FURB152 | math-constant | refurb |
| FURB154 | repeated-global | refurb |
| FURB156 | hardcoded-string-charset | refurb |
| FURB157 | verbose-decimal-constructor | refurb |
| FURB161 | bit-count | refurb |
| FURB162 | fromisoformat-replace-z | refurb |
| FURB163 | redundant-log-base | refurb |
| FURB164 | unnecessary-from-float | refurb |
| FURB166 | int-on-sliced-str | refurb |
| FURB167 | regex-flag-alias | refurb |
| FURB168 | isinstance-type-none | refurb |
| FURB169 | type-none-comparison | refurb |
| FURB171 | single-item-membership-test | refurb |
| FURB177 | implicit-cwd | refurb |
| FURB180 | meta-class-abc-meta | refurb |
| FURB181 | hashlib-digest-hex | refurb |
| FURB187 | list-reverse-copy | refurb |
| FURB188 | slice-to-remove-prefix-or-suffix | refurb |
| FURB189 | subclass-builtin | refurb |
| FURB192 | sorted-min-max | refurb |
| G001 | logging-string-format | flake8-logging-format |
| G002 | logging-percent-format | flake8-logging-format |
| G003 | logging-string-concat | flake8-logging-format |
| G004 | logging-f-string | flake8-logging-format |
| G010 | logging-warn | flake8-logging-format |
| G101 | logging-extra-attr-clash | flake8-logging-format |
| G201 | logging-exc-info | flake8-logging-format |
| G202 | logging-redundant-exc-info | flake8-logging-format |
| I001 | unsorted-imports | isort |
| I002 | missing-required-import | isort |
| ICN001 | unconventional-import-alias | flake8-import-conventions |
| ICN002 | banned-import-alias | flake8-import-conventions |
| ICN003 | banned-import-from | flake8-import-conventions |
| INP001 | implicit-namespace-package | flake8-no-pep420 |
| INT001 | f-string-in-get-text-func-call | flake8-gettext |
| INT002 | format-in-get-text-func-call | flake8-gettext |
| INT003 | printf-in-get-text-func-call | flake8-gettext |
| ISC001 | single-line-implicit-string-concatenation | flake8-implicit-str-concat |
| ISC002 | multi-line-implicit-string-concatenation | flake8-implicit-str-concat |
| ISC003 | explicit-string-concatenation | flake8-implicit-str-concat |
| ISC004 | implicit-string-concatenation-in-collection-literal | flake8-implicit-str-concat |
| LOG001 | direct-logger-instantiation | flake8-logging |
| LOG002 | invalid-get-logger-argument | flake8-logging |
| LOG004 | log-exception-outside-except-handler | flake8-logging |
| LOG007 | exception-without-exc-info | flake8-logging |
| LOG009 | undocumented-warn | flake8-logging |
| LOG014 | exc-info-outside-except-handler | flake8-logging |
| LOG015 | root-logger-call | flake8-logging |
| N801 | invalid-class-name | pep8-naming |
| N802 | invalid-function-name | pep8-naming |
| N803 | invalid-argument-name | pep8-naming |
| N804 | invalid-first-argument-name-for-class-method | pep8-naming |
| N805 | invalid-first-argument-name-for-method | pep8-naming |
| N806 | non-lowercase-variable-in-function | pep8-naming |
| N807 | dunder-function-name | pep8-naming |
| N811 | constant-imported-as-non-constant | pep8-naming |
| N812 | lowercase-imported-as-non-lowercase | pep8-naming |
| N813 | camelcase-imported-as-lowercase | pep8-naming |
| N814 | camelcase-imported-as-constant | pep8-naming |
| N815 | mixed-case-variable-in-class-scope | pep8-naming |
| N816 | mixed-case-variable-in-global-scope | pep8-naming |
| N817 | camelcase-imported-as-acronym | pep8-naming |
| N818 | error-suffix-on-exception-name | pep8-naming |
| N999 | invalid-module-name | pep8-naming |
| NPY001 | numpy-deprecated-type-alias | NumPy-specific rules |
| NPY002 | numpy-legacy-random | NumPy-specific rules |
| NPY003 | numpy-deprecated-function | NumPy-specific rules |
| NPY201 | numpy2-deprecation | NumPy-specific rules |
| PD002 | pandas-use-of-inplace-argument | pandas-vet |
| PD003 | pandas-use-of-dot-is-null | pandas-vet |
| PD004 | pandas-use-of-dot-not-null | pandas-vet |
| PD007 | pandas-use-of-dot-ix | pandas-vet |
| PD008 | pandas-use-of-dot-at | pandas-vet |
| PD009 | pandas-use-of-dot-iat | pandas-vet |
| PD010 | pandas-use-of-dot-pivot-or-unstack | pandas-vet |
| PD011 | pandas-use-of-dot-values | pandas-vet |
| PD012 | pandas-use-of-dot-read-table | pandas-vet |
| PD013 | pandas-use-of-dot-stack | pandas-vet |
| PD015 | pandas-use-of-pd-merge | pandas-vet |
| PD101 | pandas-nunique-constant-series-check | pandas-vet |
| PERF101 | unnecessary-list-cast | Perflint |
| PERF102 | incorrect-dict-iterator | Perflint |
| PERF203 | try-except-in-loop | Perflint |
| PERF401 | manual-list-comprehension | Perflint |
| PERF402 | manual-list-copy | Perflint |
| PERF403 | manual-dict-comprehension | Perflint |
| PGH003 | blanket-type-ignore | pygrep-hooks |
| PGH004 | blanket-noqa | pygrep-hooks |
| PGH005 | invalid-mock-access | pygrep-hooks |
| PIE790 | unnecessary-placeholder | flake8-pie |
| PIE794 | duplicate-class-field-definition | flake8-pie |
| PIE796 | non-unique-enums | flake8-pie |
| PIE800 | unnecessary-spread | flake8-pie |
| PIE804 | unnecessary-dict-kwargs | flake8-pie |
| PIE807 | reimplemented-container-builtin | flake8-pie |
| PIE808 | unnecessary-range-start | flake8-pie |
| PIE810 | multiple-starts-ends-with | flake8-pie |
| PLC0105 | type-name-incorrect-variance | Pylint |
| PLC0131 | type-bivariance | Pylint |
| PLC0132 | type-param-name-mismatch | Pylint |
| PLC0205 | single-string-slots | Pylint |
| PLC0206 | dict-index-missing-items | Pylint |
| PLC0207 | missing-maxsplit-arg | Pylint |
| PLC0208 | iteration-over-set | Pylint |
| PLC0414 | useless-import-alias | Pylint |
| PLC0415 | import-outside-top-level | Pylint |
| PLC1802 | len-test | Pylint |
| PLC1901 | compare-to-empty-string | Pylint |
| PLC2401 | non-ascii-name | Pylint |
| PLC2403 | non-ascii-import-name | Pylint |
| PLC2701 | import-private-name | Pylint |
| PLC2801 | unnecessary-dunder-call | Pylint |
| PLC3002 | unnecessary-direct-lambda-call | Pylint |
| PLE0100 | yield-in-init | Pylint |
| PLE0101 | return-in-init | Pylint |
| PLE0115 | nonlocal-and-global | Pylint |
| PLE0116 | continue-in-finally | Pylint |
| PLE0117 | nonlocal-without-binding | Pylint |
| PLE0118 | load-before-global-declaration | Pylint |
| PLE0237 | non-slot-assignment | Pylint |
| PLE0241 | duplicate-bases | Pylint |
| PLE0302 | unexpected-special-method-signature | Pylint |
| PLE0303 | invalid-length-return-type | Pylint |
| PLE0304 | invalid-bool-return-type | Pylint |
| PLE0305 | invalid-index-return-type | Pylint |
| PLE0307 | invalid-str-return-type | Pylint |
| PLE0308 | invalid-bytes-return-type | Pylint |
| PLE0309 | invalid-hash-return-type | Pylint |
| PLE0604 | invalid-all-object | Pylint |
| PLE0605 | invalid-all-format | Pylint |
| PLE0643 | potential-index-error | Pylint |
| PLE0704 | misplaced-bare-raise | Pylint |
| PLE1132 | repeated-keyword-argument | Pylint |
| PLE1141 | dict-iter-missing-items | Pylint |
| PLE1142 | await-outside-async | Pylint |
| PLE1205 | logging-too-many-args | Pylint |
| PLE1206 | logging-too-few-args | Pylint |
| PLE1300 | bad-string-format-character | Pylint |
| PLE1307 | bad-string-format-type | Pylint |
| PLE1310 | bad-str-strip-call | Pylint |
| PLE1507 | invalid-envvar-value | Pylint |
| PLE1519 | singledispatch-method | Pylint |
| PLE1520 | singledispatchmethod-function | Pylint |
| PLE1700 | yield-from-in-async-function | Pylint |
| PLE2502 | bidirectional-unicode | Pylint |
| PLE2510 | invalid-character-backspace | Pylint |
| PLE2512 | invalid-character-sub | Pylint |
| PLE2513 | invalid-character-esc | Pylint |
| PLE2514 | invalid-character-nul | Pylint |
| PLE2515 | invalid-character-zero-width-space | Pylint |
| PLE4703 | modified-iterating-set | Pylint |
| PLR0124 | comparison-with-itself | Pylint |
| PLR0133 | comparison-of-constant | Pylint |
| PLR0202 | no-classmethod-decorator | Pylint |
| PLR0203 | no-staticmethod-decorator | Pylint |
| PLR0206 | property-with-parameters | Pylint |
| PLR0402 | manual-from-import | Pylint |
| PLR0904 | too-many-public-methods | Pylint |
| PLR0911 | too-many-return-statements | Pylint |
| PLR0912 | too-many-branches | Pylint |
| PLR0913 | too-many-arguments | Pylint |
| PLR0914 | too-many-locals | Pylint |
| PLR0915 | too-many-statements | Pylint |
| PLR0916 | too-many-boolean-expressions | Pylint |
| PLR0917 | too-many-positional-arguments | Pylint |
| PLR1702 | too-many-nested-blocks | Pylint |
| PLR1704 | redefined-argument-from-local | Pylint |
| PLR1708 | stop-iteration-return | Pylint |
| PLR1711 | useless-return | Pylint |
| PLR1712 | swap-with-temporary-variable | Pylint |
| PLR1714 | repeated-equality-comparison | Pylint |
| PLR1716 | boolean-chained-comparison | Pylint |
| PLR1722 | sys-exit-alias | Pylint |
| PLR1730 | if-stmt-min-max | Pylint |
| PLR1733 | unnecessary-dict-index-lookup | Pylint |
| PLR1736 | unnecessary-list-index-lookup | Pylint |
| PLR2004 | magic-value-comparison | Pylint |
| PLR2044 | empty-comment | Pylint |
| PLR5501 | collapsible-else-if | Pylint |
| PLR6104 | non-augmented-assignment | Pylint |
| PLR6201 | literal-membership | Pylint |
| PLR6301 | no-self-use | Pylint |
| PLW0108 | unnecessary-lambda | Pylint |
| PLW0120 | useless-else-on-loop | Pylint |
| PLW0127 | self-assigning-variable | Pylint |
| PLW0128 | redeclared-assigned-name | Pylint |
| PLW0129 | assert-on-string-literal | Pylint |
| PLW0131 | named-expr-without-context | Pylint |
| PLW0133 | useless-exception-statement | Pylint |
| PLW0177 | nan-comparison | Pylint |
| PLW0211 | bad-staticmethod-argument | Pylint |
| PLW0244 | redefined-slots-in-subclass | Pylint |
| PLW0245 | super-without-brackets | Pylint |
| PLW0406 | import-self | Pylint |
| PLW0602 | global-variable-not-assigned | Pylint |
| PLW0603 | global-statement | Pylint |
| PLW0604 | global-at-module-level | Pylint |
| PLW0642 | self-or-cls-assignment | Pylint |
| PLW0711 | binary-op-exception | Pylint |
| PLW1501 | bad-open-mode | Pylint |
| PLW1507 | shallow-copy-environ | Pylint |
| PLW1508 | invalid-envvar-default | Pylint |
| PLW1509 | subprocess-popen-preexec-fn | Pylint |
| PLW1510 | subprocess-run-without-check | Pylint |
| PLW1514 | unspecified-encoding | Pylint |
| PLW1641 | eq-without-hash | Pylint |
| PLW2101 | useless-with-lock | Pylint |
| PLW2901 | redefined-loop-name | Pylint |
| PLW3201 | bad-dunder-method-name | Pylint |
| PLW3301 | nested-min-max | Pylint |
| PT001 | pytest-fixture-incorrect-parentheses-style | flake8-pytest-style |
| PT002 | pytest-fixture-positional-args | flake8-pytest-style |
| PT003 | pytest-extraneous-scope-function | flake8-pytest-style |
| PT006 | pytest-parametrize-names-wrong-type | flake8-pytest-style |
| PT007 | pytest-parametrize-values-wrong-type | flake8-pytest-style |
| PT008 | pytest-patch-with-lambda | flake8-pytest-style |
| PT009 | pytest-unittest-assertion | flake8-pytest-style |
| PT010 | pytest-raises-without-exception | flake8-pytest-style |
| PT011 | pytest-raises-too-broad | flake8-pytest-style |
| PT012 | pytest-raises-with-multiple-statements | flake8-pytest-style |
| PT013 | pytest-incorrect-pytest-import | flake8-pytest-style |
| PT014 | pytest-duplicate-parametrize-test-cases | flake8-pytest-style |
| PT015 | pytest-assert-always-false | flake8-pytest-style |
| PT016 | pytest-fail-without-message | flake8-pytest-style |
| PT017 | pytest-assert-in-except | flake8-pytest-style |
| PT018 | pytest-composite-assertion | flake8-pytest-style |
| PT019 | pytest-fixture-param-without-value | flake8-pytest-style |
| PT020 | pytest-deprecated-yield-fixture | flake8-pytest-style |
| PT021 | pytest-fixture-finalizer-callback | flake8-pytest-style |
| PT022 | pytest-useless-yield-fixture | flake8-pytest-style |
| PT023 | pytest-incorrect-mark-parentheses-style | flake8-pytest-style |
| PT024 | pytest-unnecessary-asyncio-mark-on-fixture | flake8-pytest-style |
| PT025 | pytest-erroneous-use-fixtures-on-fixture | flake8-pytest-style |
| PT026 | pytest-use-fixtures-without-parameters | flake8-pytest-style |
| PT027 | pytest-unittest-raises-assertion | flake8-pytest-style |
| PT028 | pytest-parameter-with-default-argument | flake8-pytest-style |
| PT029 | pytest-warns-without-warning | flake8-pytest-style |
| PT030 | pytest-warns-too-broad | flake8-pytest-style |
| PT031 | pytest-warns-with-multiple-statements | flake8-pytest-style |
| PTH100 | os-path-abspath | flake8-use-pathlib |
| PTH101 | os-chmod | flake8-use-pathlib |
| PTH102 | os-mkdir | flake8-use-pathlib |
| PTH103 | os-makedirs | flake8-use-pathlib |
| PTH104 | os-rename | flake8-use-pathlib |
| PTH105 | os-replace | flake8-use-pathlib |
| PTH106 | os-rmdir | flake8-use-pathlib |
| PTH107 | os-remove | flake8-use-pathlib |
| PTH108 | os-unlink | flake8-use-pathlib |
| PTH109 | os-getcwd | flake8-use-pathlib |
| PTH110 | os-path-exists | flake8-use-pathlib |
| PTH111 | os-path-expanduser | flake8-use-pathlib |
| PTH112 | os-path-isdir | flake8-use-pathlib |
| PTH113 | os-path-isfile | flake8-use-pathlib |
| PTH114 | os-path-islink | flake8-use-pathlib |
| PTH115 | os-readlink | flake8-use-pathlib |
| PTH116 | os-stat | flake8-use-pathlib |
| PTH117 | os-path-isabs | flake8-use-pathlib |
| PTH118 | os-path-join | flake8-use-pathlib |
| PTH119 | os-path-basename | flake8-use-pathlib |
| PTH120 | os-path-dirname | flake8-use-pathlib |
| PTH121 | os-path-samefile | flake8-use-pathlib |
| PTH122 | os-path-splitext | flake8-use-pathlib |
| PTH123 | builtin-open | flake8-use-pathlib |
| PTH124 | py-path | flake8-use-pathlib |
| PTH201 | path-constructor-current-directory | flake8-use-pathlib |
| PTH202 | os-path-getsize | flake8-use-pathlib |
| PTH203 | os-path-getatime | flake8-use-pathlib |
| PTH204 | os-path-getmtime | flake8-use-pathlib |
| PTH205 | os-path-getctime | flake8-use-pathlib |
| PTH206 | os-sep-split | flake8-use-pathlib |
| PTH207 | glob | flake8-use-pathlib |
| PTH208 | os-listdir | flake8-use-pathlib |
| PTH210 | invalid-pathlib-with-suffix | flake8-use-pathlib |
| PTH211 | os-symlink | flake8-use-pathlib |
| PYI001 | unprefixed-type-param | flake8-pyi |
| PYI002 | complex-if-statement-in-stub | flake8-pyi |
| PYI003 | unrecognized-version-info-check | flake8-pyi |
| PYI004 | patch-version-comparison | flake8-pyi |
| PYI005 | wrong-tuple-length-version-comparison | flake8-pyi |
| PYI006 | bad-version-info-comparison | flake8-pyi |
| PYI007 | unrecognized-platform-check | flake8-pyi |
| PYI008 | unrecognized-platform-name | flake8-pyi |
| PYI009 | pass-statement-stub-body | flake8-pyi |
| PYI010 | non-empty-stub-body | flake8-pyi |
| PYI011 | typed-argument-default-in-stub | flake8-pyi |
| PYI012 | pass-in-class-body | flake8-pyi |
| PYI013 | ellipsis-in-non-empty-class-body | flake8-pyi |
| PYI014 | argument-default-in-stub | flake8-pyi |
| PYI015 | assignment-default-in-stub | flake8-pyi |
| PYI016 | duplicate-union-member | flake8-pyi |
| PYI017 | complex-assignment-in-stub | flake8-pyi |
| PYI018 | unused-private-type-var | flake8-pyi |
| PYI019 | custom-type-var-for-self | flake8-pyi |
| PYI020 | quoted-annotation-in-stub | flake8-pyi |
| PYI021 | docstring-in-stub | flake8-pyi |
| PYI024 | collections-named-tuple | flake8-pyi |
| PYI025 | unaliased-collections-abc-set-import | flake8-pyi |
| PYI026 | type-alias-without-annotation | flake8-pyi |
| PYI029 | str-or-repr-defined-in-stub | flake8-pyi |
| PYI030 | unnecessary-literal-union | flake8-pyi |
| PYI032 | any-eq-ne-annotation | flake8-pyi |
| PYI033 | type-comment-in-stub | flake8-pyi |
| PYI034 | non-self-return-type | flake8-pyi |
| PYI035 | unassigned-special-variable-in-stub | flake8-pyi |
| PYI036 | bad-exit-annotation | flake8-pyi |
| PYI041 | redundant-numeric-union | flake8-pyi |
| PYI042 | snake-case-type-alias | flake8-pyi |
| PYI043 | t-suffixed-type-alias | flake8-pyi |
| PYI044 | future-annotations-in-stub | flake8-pyi |
| PYI045 | iter-method-return-iterable | flake8-pyi |
| PYI046 | unused-private-protocol | flake8-pyi |
| PYI047 | unused-private-type-alias | flake8-pyi |
| PYI048 | stub-body-multiple-statements | flake8-pyi |
| PYI049 | unused-private-typed-dict | flake8-pyi |
| PYI050 | no-return-argument-annotation-in-stub | flake8-pyi |
| PYI051 | redundant-literal-union | flake8-pyi |
| PYI052 | unannotated-assignment-in-stub | flake8-pyi |
| PYI053 | string-or-bytes-too-long | flake8-pyi |
| PYI054 | numeric-literal-too-long | flake8-pyi |
| PYI055 | unnecessary-type-union | flake8-pyi |
| PYI056 | unsupported-method-call-on-all | flake8-pyi |
| PYI057 | byte-string-usage | flake8-pyi |
| PYI058 | generator-return-from-iter-method | flake8-pyi |
| PYI059 | generic-not-last-base-class | flake8-pyi |
| PYI061 | redundant-none-literal | flake8-pyi |
| PYI062 | duplicate-literal-member | flake8-pyi |
| PYI063 | pep484-style-positional-only-parameter | flake8-pyi |
| PYI064 | redundant-final-literal | flake8-pyi |
| PYI066 | bad-version-info-order | flake8-pyi |
| Q000 | bad-quotes-inline-string | flake8-quotes |
| Q001 | bad-quotes-multiline-string | flake8-quotes |
| Q002 | bad-quotes-docstring | flake8-quotes |
| Q003 | avoidable-escaped-quote | flake8-quotes |
| Q004 | unnecessary-escaped-quote | flake8-quotes |
| RET501 | unnecessary-return-none | flake8-return |
| RET502 | implicit-return-value | flake8-return |
| RET503 | implicit-return | flake8-return |
| RET504 | unnecessary-assign | flake8-return |
| RET505 | superfluous-else-return | flake8-return |
| RET506 | superfluous-else-raise | flake8-return |
| RET507 | superfluous-else-continue | flake8-return |
| RET508 | superfluous-else-break | flake8-return |
| RSE102 | unnecessary-paren-on-raise-exception | flake8-raise |
| RUF001 | ambiguous-unicode-character-string | Ruff-specific rules |
| RUF002 | ambiguous-unicode-character-docstring | Ruff-specific rules |
| RUF003 | ambiguous-unicode-character-comment | Ruff-specific rules |
| RUF005 | collection-literal-concatenation | Ruff-specific rules |
| RUF006 | asyncio-dangling-task | Ruff-specific rules |
| RUF007 | zip-instead-of-pairwise | Ruff-specific rules |
| RUF008 | mutable-dataclass-default | Ruff-specific rules |
| RUF009 | function-call-in-dataclass-default-argument | Ruff-specific rules |
| RUF010 | explicit-f-string-type-conversion | Ruff-specific rules |
| RUF012 | mutable-class-default | Ruff-specific rules |
| RUF013 | implicit-optional | Ruff-specific rules |
| RUF015 | unnecessary-iterable-allocation-for-first-element | Ruff-specific rules |
| RUF016 | invalid-index-type | Ruff-specific rules |
| RUF017 | quadratic-list-summation | Ruff-specific rules |
| RUF018 | assignment-in-assert | Ruff-specific rules |
| RUF019 | unnecessary-key-check | Ruff-specific rules |
| RUF020 | never-union | Ruff-specific rules |
| RUF021 | parenthesize-chained-operators | Ruff-specific rules |
| RUF022 | unsorted-dunder-all | Ruff-specific rules |
| RUF023 | unsorted-dunder-slots | Ruff-specific rules |
| RUF024 | mutable-fromkeys-value | Ruff-specific rules |
| RUF026 | default-factory-kwarg | Ruff-specific rules |
| RUF027 | missing-f-string-syntax | Ruff-specific rules |
| RUF028 | invalid-formatter-suppression-comment | Ruff-specific rules |
| RUF029 | unused-async | Ruff-specific rules |
| RUF030 | assert-with-print-message | Ruff-specific rules |
| RUF031 | incorrectly-parenthesized-tuple-in-subscript | Ruff-specific rules |
| RUF032 | decimal-from-float-literal | Ruff-specific rules |
| RUF033 | post-init-default | Ruff-specific rules |
| RUF034 | useless-if-else | Ruff-specific rules |
| RUF036 | none-not-at-end-of-union | Ruff-specific rules |
| RUF037 | unnecessary-empty-iterable-within-deque-call | Ruff-specific rules |
| RUF038 | redundant-bool-literal | Ruff-specific rules |
| RUF039 | unraw-re-pattern | Ruff-specific rules |
| RUF040 | invalid-assert-message-literal-argument | Ruff-specific rules |
| RUF041 | unnecessary-nested-literal | Ruff-specific rules |
| RUF043 | pytest-raises-ambiguous-pattern | Ruff-specific rules |
| RUF045 | implicit-class-var-in-dataclass | Ruff-specific rules |
| RUF046 | unnecessary-cast-to-int | Ruff-specific rules |
| RUF047 | needless-else | Ruff-specific rules |
| RUF048 | map-int-version-parsing | Ruff-specific rules |
| RUF049 | dataclass-enum | Ruff-specific rules |
| RUF050 | unnecessary-if | Ruff-specific rules |
| RUF051 | if-key-in-dict-del | Ruff-specific rules |
| RUF052 | used-dummy-variable | Ruff-specific rules |
| RUF053 | class-with-mixed-type-vars | Ruff-specific rules |
| RUF054 | indented-form-feed | Ruff-specific rules |
| RUF055 | unnecessary-regular-expression | Ruff-specific rules |
| RUF056 | falsy-dict-get-fallback | Ruff-specific rules |
| RUF057 | unnecessary-round | Ruff-specific rules |
| RUF058 | starmap-zip | Ruff-specific rules |
| RUF059 | unused-unpacked-variable | Ruff-specific rules |
| RUF060 | in-empty-collection | Ruff-specific rules |
| RUF061 | legacy-form-pytest-raises | Ruff-specific rules |
| RUF063 | access-annotations-from-class-dict | Ruff-specific rules |
| RUF064 | non-octal-permissions | Ruff-specific rules |
| RUF065 | logging-eager-conversion | Ruff-specific rules |
| RUF066 | property-without-return | Ruff-specific rules |
| RUF067 | non-empty-init-module | Ruff-specific rules |
| RUF068 | duplicate-entry-in-dunder-all | Ruff-specific rules |
| RUF069 | float-equality-comparison | Ruff-specific rules |
| RUF070 | unnecessary-assign-before-yield | Ruff-specific rules |
| RUF071 | os-path-commonprefix | Ruff-specific rules |
| RUF072 | useless-finally | Ruff-specific rules |
| RUF073 | f-string-percent-format | Ruff-specific rules |
| RUF100 | unused-noqa | Ruff-specific rules |
| RUF101 | redirected-noqa | Ruff-specific rules |
| RUF102 | invalid-rule-code | Ruff-specific rules |
| RUF103 | invalid-suppression-comment | Ruff-specific rules |
| RUF104 | unmatched-suppression-comment | Ruff-specific rules |
| RUF200 | invalid-pyproject-toml | Ruff-specific rules |
| S101 | assert | flake8-bandit |
| S102 | exec-builtin | flake8-bandit |
| S103 | bad-file-permissions | flake8-bandit |
| S104 | hardcoded-bind-all-interfaces | flake8-bandit |
| S105 | hardcoded-password-string | flake8-bandit |
| S106 | hardcoded-password-func-arg | flake8-bandit |
| S107 | hardcoded-password-default | flake8-bandit |
| S108 | hardcoded-temp-file | flake8-bandit |
| S110 | try-except-pass | flake8-bandit |
| S112 | try-except-continue | flake8-bandit |
| S113 | request-without-timeout | flake8-bandit |
| S201 | flask-debug-true | flake8-bandit |
| S202 | tarfile-unsafe-members | flake8-bandit |
| S301 | suspicious-pickle-usage | flake8-bandit |
| S302 | suspicious-marshal-usage | flake8-bandit |
| S303 | suspicious-insecure-hash-usage | flake8-bandit |
| S304 | suspicious-insecure-cipher-usage | flake8-bandit |
| S305 | suspicious-insecure-cipher-mode-usage | flake8-bandit |
| S306 | suspicious-mktemp-usage | flake8-bandit |
| S307 | suspicious-eval-usage | flake8-bandit |
| S308 | suspicious-mark-safe-usage | flake8-bandit |
| S310 | suspicious-url-open-usage | flake8-bandit |
| S311 | suspicious-non-cryptographic-random-usage | flake8-bandit |
| S312 | suspicious-telnet-usage | flake8-bandit |
| S313 | suspicious-xmlc-element-tree-usage | flake8-bandit |
| S314 | suspicious-xml-element-tree-usage | flake8-bandit |
| S315 | suspicious-xml-expat-reader-usage | flake8-bandit |
| S316 | suspicious-xml-expat-builder-usage | flake8-bandit |
| S317 | suspicious-xml-sax-usage | flake8-bandit |
| S318 | suspicious-xml-mini-dom-usage | flake8-bandit |
| S319 | suspicious-xml-pull-dom-usage | flake8-bandit |
| S321 | suspicious-ftp-lib-usage | flake8-bandit |
| S323 | suspicious-unverified-context-usage | flake8-bandit |
| S324 | hashlib-insecure-hash-function | flake8-bandit |
| S401 | suspicious-telnetlib-import | flake8-bandit |
| S402 | suspicious-ftplib-import | flake8-bandit |
| S403 | suspicious-pickle-import | flake8-bandit |
| S404 | suspicious-subprocess-import | flake8-bandit |
| S405 | suspicious-xml-etree-import | flake8-bandit |
| S406 | suspicious-xml-sax-import | flake8-bandit |
| S407 | suspicious-xml-expat-import | flake8-bandit |
| S408 | suspicious-xml-minidom-import | flake8-bandit |
| S409 | suspicious-xml-pulldom-import | flake8-bandit |
| S411 | suspicious-xmlrpc-import | flake8-bandit |
| S412 | suspicious-httpoxy-import | flake8-bandit |
| S413 | suspicious-pycrypto-import | flake8-bandit |
| S415 | suspicious-pyghmi-import | flake8-bandit |
| S501 | request-with-no-cert-validation | flake8-bandit |
| S502 | ssl-insecure-version | flake8-bandit |
| S503 | ssl-with-bad-defaults | flake8-bandit |
| S504 | ssl-with-no-version | flake8-bandit |
| S505 | weak-cryptographic-key | flake8-bandit |
| S506 | unsafe-yaml-load | flake8-bandit |
| S507 | ssh-no-host-key-verification | flake8-bandit |
| S508 | snmp-insecure-version | flake8-bandit |
| S509 | snmp-weak-cryptography | flake8-bandit |
| S602 | subprocess-popen-with-shell-equals-true | flake8-bandit |
| S603 | subprocess-without-shell-equals-true | flake8-bandit |
| S604 | call-with-shell-equals-true | flake8-bandit |
| S605 | start-process-with-a-shell | flake8-bandit |
| S606 | start-process-with-no-shell | flake8-bandit |
| S607 | start-process-with-partial-path | flake8-bandit |
| S608 | hardcoded-sql-expression | flake8-bandit |
| S609 | unix-command-wildcard-injection | flake8-bandit |
| S610 | django-extra | flake8-bandit |
| S611 | django-raw-sql | flake8-bandit |
| S612 | logging-config-insecure-listen | flake8-bandit |
| S701 | jinja2-autoescape-false | flake8-bandit |
| S702 | mako-templates | flake8-bandit |
| S704 | unsafe-markup-use | flake8-bandit |
| SIM101 | duplicate-isinstance-call | flake8-simplify |
| SIM102 | collapsible-if | flake8-simplify |
| SIM103 | needless-bool | flake8-simplify |
| SIM105 | suppressible-exception | flake8-simplify |
| SIM107 | return-in-try-except-finally | flake8-simplify |
| SIM108 | if-else-block-instead-of-if-exp | flake8-simplify |
| SIM110 | reimplemented-builtin | flake8-simplify |
| SIM112 | uncapitalized-environment-variables | flake8-simplify |
| SIM113 | enumerate-for-loop | flake8-simplify |
| SIM114 | if-with-same-arms | flake8-simplify |
| SIM115 | open-file-with-context-handler | flake8-simplify |
| SIM116 | if-else-block-instead-of-dict-lookup | flake8-simplify |
| SIM117 | multiple-with-statements | flake8-simplify |
| SIM118 | in-dict-keys | flake8-simplify |
| SIM201 | negate-equal-op | flake8-simplify |
| SIM202 | negate-not-equal-op | flake8-simplify |
| SIM208 | double-negation | flake8-simplify |
| SIM210 | if-expr-with-true-false | flake8-simplify |
| SIM211 | if-expr-with-false-true | flake8-simplify |
| SIM212 | if-expr-with-twisted-arms | flake8-simplify |
| SIM220 | expr-and-not-expr | flake8-simplify |
| SIM221 | expr-or-not-expr | flake8-simplify |
| SIM222 | expr-or-true | flake8-simplify |
| SIM223 | expr-and-false | flake8-simplify |
| SIM300 | yoda-conditions | flake8-simplify |
| SIM401 | if-else-block-instead-of-dict-get | flake8-simplify |
| SIM905 | split-static-string | flake8-simplify |
| SIM910 | dict-get-with-none-default | flake8-simplify |
| SIM911 | zip-dict-keys-and-values | flake8-simplify |
| SLF001 | private-member-access | flake8-self |
| SLOT000 | no-slots-in-str-subclass | flake8-slots |
| SLOT001 | no-slots-in-tuple-subclass | flake8-slots |
| SLOT002 | no-slots-in-namedtuple-subclass | flake8-slots |
| T100 | debugger | flake8-debugger |
| T201 | print | flake8-print |
| T203 | p-print | flake8-print |
| TC001 | typing-only-first-party-import | flake8-type-checking |
| TC002 | typing-only-third-party-import | flake8-type-checking |
| TC003 | typing-only-standard-library-import | flake8-type-checking |
| TC004 | runtime-import-in-type-checking-block | flake8-type-checking |
| TC005 | empty-type-checking-block | flake8-type-checking |
| TC006 | runtime-cast-value | flake8-type-checking |
| TC008 | quoted-type-alias | flake8-type-checking |
| TC010 | runtime-string-union | flake8-type-checking |
| TD001 | invalid-todo-tag | flake8-todos |
| TD002 | missing-todo-author | flake8-todos |
| TD003 | missing-todo-link | flake8-todos |
| TD004 | missing-todo-colon | flake8-todos |
| TD005 | missing-todo-description | flake8-todos |
| TD006 | invalid-todo-capitalization | flake8-todos |
| TD007 | missing-space-after-todo-colon | flake8-todos |
| TID251 | banned-api | flake8-tidy-imports |
| TID252 | relative-imports | flake8-tidy-imports |
| TID253 | banned-module-level-imports | flake8-tidy-imports |
| TID254 | lazy-import-mismatch | flake8-tidy-imports |
| TRY002 | raise-vanilla-class | tryceratops |
| TRY003 | raise-vanilla-args | tryceratops |
| TRY004 | type-check-without-type-error | tryceratops |
| TRY201 | verbose-raise | tryceratops |
| TRY203 | useless-try-except | tryceratops |
| TRY300 | try-consider-else | tryceratops |
| TRY301 | raise-within-try | tryceratops |
| TRY400 | error-instead-of-exception | tryceratops |
| TRY401 | verbose-log-message | tryceratops |
| UP001 | useless-metaclass-type | pyupgrade |
| UP003 | type-of-primitive | pyupgrade |
| UP004 | useless-object-inheritance | pyupgrade |
| UP005 | deprecated-unittest-alias | pyupgrade |
| UP006 | non-pep585-annotation | pyupgrade |
| UP007 | non-pep604-annotation-union | pyupgrade |
| UP008 | super-call-with-parameters | pyupgrade |
| UP009 | utf8-encoding-declaration | pyupgrade |
| UP010 | unnecessary-future-import | pyupgrade |
| UP011 | lru-cache-without-parameters | pyupgrade |
| UP012 | unnecessary-encode-utf8 | pyupgrade |
| UP013 | convert-typed-dict-functional-to-class | pyupgrade |
| UP014 | convert-named-tuple-functional-to-class | pyupgrade |
| UP015 | redundant-open-modes | pyupgrade |
| UP017 | datetime-timezone-utc | pyupgrade |
| UP018 | native-literals | pyupgrade |
| UP019 | typing-text-str-alias | pyupgrade |
| UP020 | open-alias | pyupgrade |
| UP021 | replace-universal-newlines | pyupgrade |
| UP022 | replace-stdout-stderr | pyupgrade |
| UP023 | deprecated-c-element-tree | pyupgrade |
| UP024 | os-error-alias | pyupgrade |
| UP025 | unicode-kind-prefix | pyupgrade |
| UP026 | deprecated-mock-import | pyupgrade |
| UP028 | yield-in-for-loop | pyupgrade |
| UP029 | unnecessary-builtin-import | pyupgrade |
| UP030 | format-literals | pyupgrade |
| UP031 | printf-string-formatting | pyupgrade |
| UP032 | f-string | pyupgrade |
| UP033 | lru-cache-with-maxsize-none | pyupgrade |
| UP034 | extraneous-parentheses | pyupgrade |
| UP035 | deprecated-import | pyupgrade |
| UP036 | outdated-version-block | pyupgrade |
| UP037 | quoted-annotation | pyupgrade |
| UP039 | unnecessary-class-parentheses | pyupgrade |
| UP040 | non-pep695-type-alias | pyupgrade |
| UP041 | timeout-error-alias | pyupgrade |
| UP042 | replace-str-enum | pyupgrade |
| UP043 | unnecessary-default-type-args | pyupgrade |
| UP044 | non-pep646-unpack | pyupgrade |
| UP045 | non-pep604-annotation-optional | pyupgrade |
| UP046 | non-pep695-generic-class | pyupgrade |
| UP047 | non-pep695-generic-function | pyupgrade |
| UP049 | private-type-parameter | pyupgrade |
| UP050 | useless-class-metaclass-type | pyupgrade |
| W191 | tab-indentation | pycodestyle |
| W291 | trailing-whitespace | pycodestyle |
| W292 | missing-newline-at-end-of-file | pycodestyle |
| W293 | blank-line-with-whitespace | pycodestyle |
| W391 | too-many-newlines-at-end-of-file | pycodestyle |
| W505 | doc-line-too-long | pycodestyle |
| W605 | invalid-escape-sequence | pycodestyle |
| YTT101 | sys-version-slice3 | flake8-2020 |
| YTT102 | sys-version2 | flake8-2020 |
| YTT103 | sys-version-cmp-str3 | flake8-2020 |
| YTT201 | sys-version-info0-eq3 | flake8-2020 |
| YTT202 | six-py3 | flake8-2020 |
| YTT203 | sys-version-info1-cmp-int | flake8-2020 |
| YTT204 | sys-version-info-minor-cmp-int | flake8-2020 |
| YTT301 | sys-version0 | flake8-2020 |
| YTT302 | sys-version-cmp-str10 | flake8-2020 |
| YTT303 | sys-version-slice1 | flake8-2020 |

</details>

## PASS-VIA-ALIAS — Rules detected under canonical code (9)

These rules exist in ruff under old codes, but ruff outputs findings using the new canonical code.
The sample in `ruff-OLDCODE/` correctly triggers the rule's behavior.

| Old Code | Canonical Code | Rule Name |
|---|---|---|
| PGH001 | S307 | suspicious-eval-usage (eval) |
| PGH002 | G010 | logging-warn (deprecated-log-warn) |
| PLR1701 | SIM101 | duplicate-isinstance-call |
| PLR1706 | RUF021 | redundant-or-operator (and-or-ternary) |
| RUF011 | B035 | static-key-dict-comprehension |
| RUF035 | S704 | suspicious-markup-include |
| SIM109 | PLR1714 | repeated-equality-comparison |
| TC007 | TC004 | banned-annotations-in-type-checking-blocks |
| TRY200 | B904 | raise-without-from-inside-except |

## CONVENTION-CONFLICT — Mutually exclusive docstring conventions (2)

These rules fire correctly when selected individually (`--select D203`), but are suppressed by
their conflicting counterparts when running `--select ALL` (ruff enforces one convention globally).

| Code | Name | Conflict |
|---|---|---|
| D203 | incorrect-blank-line-before-class | Conflicts with D211 |
| D213 | multi-line-summary-second-line | Conflicts with D212 |

## REMOVED — Rules removed from current ruff (10)

These rules were removed from ruff and can no longer be selected. Sample files are retained for reference.

| Code | Name | Linter |
|---|---|---|
| ANN101 | missing-type-self | flake8-annotations |
| ANN102 | missing-type-cls | flake8-annotations |
| E999 | syntax-error | pycodestyle |
| PD901 | pandas-df-variable-name | pandas-vet |
| PT004 | pytest-missing-fixture-name-underscore | flake8-pytest-style |
| PT005 | pytest-incorrect-fixture-name-underscore | flake8-pytest-style |
| S320 | suspicious-xmle-tree-usage | flake8-bandit |
| S410 | suspicious-lxml-import | flake8-bandit |
| UP027 | unpacked-list-comprehension | pyupgrade |
| UP038 | non-pep604-isinstance | pyupgrade |

## UNTRIGGERABLE — Cannot fire by file content (3)

| Code | Name | Reason |
|---|---|---|
| E902 | io-error | OS-level read error, not triggerable by file content |
| F621 | expressions-in-star-assignment | Causes Python SyntaxError before ruff can analyze the file |
| S601 | paramiko-call | Requires `paramiko` package installed |
