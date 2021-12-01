# Changelog

## 3.3.1 - [unreleased]

### Fixed

* Results returned from the callback views are now fully-annotated (based on the callback contract type)

## 3.3.0 - 2021-11-26

### Added

* Changelog 😅
* Support for on-chain views:
  - Multiple `view` sections are correctly parsed/unparsed
  - in REPL `VIEW` instruction works both with self-recursive calls and on-chain contracts (if shell is attached)
  - `ContractInterface` provides a seamless interface to views (works pretty much the same as with off-chain views)
  - Ability to patch VIEW results when using `interpret()` or `onchain_view()`
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