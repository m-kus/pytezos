# CONTRIBUTING

## Maintainer guide

### Adding support for a new protocol

1. Check out the `baking-bad/sandboxed-node` repo. There should be "Update Octez binaries to X.Y" PR created automatically by `octez_version.yml` GitHub Action. Make sure everything works and merge it.
2. When something is merged to the `master` branch, another pipeline `tag.yml` will be triggered. It tags the current commit with `vX.Y.Z` and force pushes it. **BUG**: This pipeline currently fails with 403 for some reason. You need to pull the `master` and execute `make release` to run the process manually.
3. Now back to the PyTezos. Update `pytezos.sandbox.node.DOCKER_IMAGE` constant to the new image.
4. Set `pytezos.sandbox.node.LATEST` constant to the current protocol hash.
5. Update `sandbox_params` and `protocol_params` using values from Tezos source code and TzKT-hosted node RPC respectively.
6. Run `make docs` with `NODE_RPC_URL` environment variable set to the private full node to update references.
7. Read Release Notes for the new protocol and make necessary changes to the code.
8. Check if `make all` is green and `pytezos sandbox` works. Optionally, `michelson-kernel run` to check if the Jupyter kernel is fine.

### Releasing a new version

1. Checkout to `aux/X.Y.Z` branch. Update the version number in `pyproject.toml`.
2. Run `make before_release` to perform the pre-release routine.
3. Update `CHANGELOG.md` following the existing format.
4. After merging the PR, tag `X.Y.Z` on `master` and push to the origin.
5. For *.0 releases make sure that notifications are sent to Telegram, Slack and, manually, Discord.
