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
