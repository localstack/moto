# Moto - Mock AWS Services

Fork of [`moto`](https://github.com/spulec/moto) with changes and adaptations for [LocalStack](https://github.com/localstack/localstack).

Please refer to the upstream repo for more details.

## Releasing

This fork is maintained as a separate pypi package, [moto-ext](https://pypi.org/project/moto-ext). To release a new version, follow these steps:

```
# make sure to have git remotes defined for both repos: 
$ git remote -v
localstack	git@github.com:localstack/moto.git (fetch)
localstack	git@github.com:localstack/moto.git (push)
upstream	git@github.com:spulec/moto.git (fetch)
upstream	git@github.com:spulec/moto.git (push)

# fetch fresh upstream "master" branch
$ git fetch upstream master

# branch "localstack" is the default branch of this repo
$ git checkout localstack
$ git rebase upstream/master  # resolve merge conflicts, if any...
# (force-)push latest changes to the remote repo
$ git push -f localstack localstack

# update __version__, then publish to pypi
$ vi moto/__init__.py
...
$ rm -rf dist/ build/
$ make publish
...
```

## Internal Release Notes

In this section we can keep track of notes and pointers, mostly for internal coordination of moto-ext releases for LocalStack.

* **Note 2022-06-22**: We are currently blocked to perform a full upgrade to latest upstream `master` (due to conflicting changes with multi-account support), hence the following commits (contributed by LS team, in reverse chronological order) from upstream `master` have been cherry-picked and added to the `localstack` branch (and moto-ext release):
```
e99e8a883c1000079509e92eb0bfd4969fb84486
c2b1950698d7c231b17ea2ae9d7bd0afc2169b99
48186924ae2dbee165b2d02ea0978b3cfeea59b1
b66e04ffd52b4cfdd95d22cd7253bc78dd70f595
631e887b5ee154de6711db8f30522de3d51c4356
1698c52740c6429c1acfdf3f040a817afc2ff73f
67cda6d7d6f42118ccd7e2170e7ff0a1f92fa6a6
b96eafb3c3e4c2e40c4ca62a3b555a51296cc6e3
34a98d2c205ed311a867083b3ee17c18fb8ebb48
68b93c3b86b0280eb387f4cb7ba47edd575c3375
```
The corresponding commit hashes on the `localstack` branch are as follows:
```
28ba9e5c923423a95e2172a08d0de876d65e9321
46a35a23a682c8d3fe74166e92a650288a861e67
e7338e048b4970632fdd4c0352ce4c258be7c270
ea755bebb9bb4c9075640880bc38fd5c959bb757
2d5d2140e06ddf237128ba4fd63afd18d64f1ee0
38405ebba75ba296423cf164c593d52c09904764
c37378c8c2dd469385c701f539611df0d2b0a9df
185169bf29bff7b17ec32a3864b65785bcd80355
8702038953a9025b5535115e422e40da7326451f
8b328272ed8038e3e335526dd061e91f031db2a2
```
Next time we rebase onto latest upstream `master`, we can likely get those commits removed from the `localstack` branch again!
