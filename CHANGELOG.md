# Changelog

## 3.4.1 - 2022-03-22

### Fixed

* Issue with `lazy_storage_diff`

## 3.4.0 - 2022-03-22

### Fixed

* `run_code` does not merge lazy storage diffs correctly

### Changed

* Default protocol is Ithaca
* Sandbox node version is updated to v12

## 3.3.6 - 2022-03-10

### Fixed

* Logging configuration is not overwritten by pytezos

### Added

* Installation hints for M1 (credits to @konchunas)

## 3.3.5 - 2022-02-28

### Fixed

* Metadata big map can be located in a nested structure, not necessarily on the top-level (as per TZIP-16)

## 3.3.4 - 2021-12-23

### Fixed

* New testnet faucet is handled properly (the json format has slightly changed)
* Incorrect wrapping of static methods while injecting jupyter docs (py3.10)
* Unable to call intermediate entrypoints from the contract interfaceE
* Sandboxed node wasn't exposed at localhost causing connection issues on MacOS and Windows
* Big map key of nested or/pair type wasn't handled correctly

### Changed

* `Key.verify` returns `True` if the signature is valid (it was `None` before)

## 3.3.3 - 2021-12-14

### Fixed

* Always try to fetch the latest storage in off-chain or on-chain views
* Fixed case with `GET` instruction returning `None` with wrong type (key type instead of value type)

## 3.3.2 - 2021-12-12

### Added

* explicit handling of the 401 to return a more meaningful response [@kaellis]

### Fixed

* Regression in offline view behavior for storage with bigmaps

## 3.3.1 - 2021-12-01

### Added

* Ability to patch VIEW results when using `interpret()` or `onchain_view()`

### Fixed

* Results returned from the callback views are now fully-annotated (based on the callback contract type)

## 3.3.0 - 2021-11-26

### Added

* Changelog 😅
* Support for on-chain views:
  - Multiple `view` sections are correctly parsed/unparsed
  - in REPL `VIEW` instruction works both with self-recursive calls and on-chain contracts (if shell is attached)
  - `ContractInterface` provides a seamless interface to views (works pretty much the same as with off-chain views)
* Partial support for global constants:
  - added new operation kind `register_global_constant`
  - `ExecutionContext` allows to register constants as well
  - `ContractInterface` resolves all the constants using the context upon creation
  - Since there is no RPC for retrieving on-chain global constants proper resolving cannot be implemented
  - It is not possible to use constants in transaction parameters and origination script with high-level entities
* Minimal support for timelock feature:
  - `chest`, `chest_key`, and `CHEST` primitives are supported in parser, but not in the REPL
  - There are currenty no way to construct a timelock

### Changed

* Hangzhou (PtHangz2) RPC endpoint (`hangzhou` is the default shell now), sandbox image (`v11.0-1`)

### Fixed

* `pytezos sandbox` CLI command now works properly and provides almost flextesa-like experience at lesser cost
* Operation branch was calculated incorrectly based on the TTL (before `head~{60-ttl}`, after `head~{120-ttl}`)
