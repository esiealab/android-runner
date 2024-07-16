# Contributing to the Android Runner Framework

Thank you for your interest in using the Android Runner framework. Android Runner has been built up in iterative steps by bachelor's, master's, PhD students and professors. Our goal is to make performance and energy consumption research on Android devices more accessible and robust. The framework provides many tools and plugins to make this possible.

## Table of Contents
- [Environment](#environment)
- [Making Changes to Your Forked Repository](#making-changes-to-your-forked-repository)
    - [Commits](#commits)
    - [Plugins](#plugins)
- [Submitting a Pull Request](#submitting-a-pull-request)
- [Communication](#communication)
- [Debugging Tips](#debugging-tips)

## Before You Begin
It's important for us to make sure that any updates to the framework add value and that the updates adhere to the original goals of the framework.  Before spending a lot of time making substantial changes, please raise an `issue` on Github so we're made aware of the changes you'd like to implement.  We'll provide feedback to inform you whether we think it's viable.

## Environment
- Your forked repository will come with one branch, called `master`.
- Create additional branches for experiments and/or development with `git branch branch_name`.
- To update your forked repo with parent repo, `git checkout master` and type `git fetch upstream` followed by `git rebase upstream/master` so your local work is put on top of any changes made to the parent repo. 
    - Note, this may mean you'll have to stash whatever you were working on.  In this case, `git stash save "message"` before `git checkout master`.
- Once `master` has been updated, checkout the other branches to update with `git merge master`.
- Then, `git stash pop stash@{#}` to continue working on changes.

## Making Changes to Your Forked Repository
### Commits
Any commits should contain logically similar changes.  Commit messages (`git commit -m "[text]"`) should be informative but also concise.  Good commits make changes easier to review later.  To limit the number of commits, use `git rebase` to squash the commits down to a more reasonable number.

### Plugins
If you're editing an existing plugin or adding a new one, there's an automated test called **plugintest** in `examples` that will ensure the plugin adheres to the requirements of the framework.  To execute it, type: `python3 android-runner android-runner/examples/plugintest/config.json`.

## Submitting a Pull Request
Pull requests should be made from secondary branches (ie, not `master`).  Also make sure the branch is not behind in commits compared to master.  Any changes that need to be made while a pull request is still pending review should be made on a third branch to prevent polluting the pull request with other changes if they're not relevant.  

When a pull request is submitted, a number of automated tests are performed on the **TravisCI** platform and with **SonarCloud**.  TravisCI runs coverage analysis to confirm that all major components in the framework have associated unit tests in tests/unit/.  In other words, **you'll need to add unit tests for new methods, plugins or other functionality improvements**.  For an expedited review process, run **pytest** in your local environment before submitting a pull request.  You can execute these tests in the android-runner directory with: `py.test [options] tests/unit`. It's also possible to run py.test with a specific module in tests/unit/.   Don't forget to **remove debugging statements** before submitting.

To execute the test suite make sure you have installed `coverage`, `pytest` and `mock` either globally or in your virtual environment. You can then run (assuming Python3):
```sh
python -m coverage run -m py.test tests/unit/
```
To then check the code coverage and report missing lines run:
```sh
python -m coverage report -m
```
## Communication
The best way to communicate with the Android Runner team is through:
- Opening a GitHub issue
- Slack
- Canvas

## Debugging Tips
[pdb](https://docs.python.org/3/library/pdb.html) is a good library to import if you experience issues that may be hard to resolve with print statements.  

