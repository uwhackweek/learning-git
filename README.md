# Learning Git Version Control System

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://jarednielsen.com/learn-git-fork-pull-request/)

---

Repository for learning git and GitHub collaboratively.

There are many ways to contribute to a project and two of those are higlighted below.
We encourage participants to practice either one during an event and many open source
projects have similar guides to contribute.

The two flows are:
* Contributing directly with a branch
* Contributing through a fork

## Git workflows

### Which one to choose?
The way you can contribute and choose one of the above flows depends on your access
privileges to a repository. You can use both flows, if you are part of the organization
that owns the repository. This is the case when you participate in the hackweek and
we added you to the GitHub organizaion. Once you are not part of the organization or
if you want to contribute to a repository that is on someone else's personal account,
then you need to use a fork.

### Terminology
Before we dive into the workflows, here some essential terms and links to definitions:
* [Branch](https://docs.github.com/en/github/getting-started-with-github/quickstart/github-glossary#branch)
* [Clone](https://docs.github.com/en/github/getting-started-with-github/quickstart/github-glossary#clone)
* [Fork](https://docs.github.com/en/github/getting-started-with-github/quickstart/github-glossary#fork)
* [Pull Request or short PR](https://docs.github.com/en/github/getting-started-with-github/quickstart/github-glossary#pull-request)
* [Push](https://docs.github.com/en/github/getting-started-with-github/quickstart/github-glossary#push)

## Contributing through a fork

An in-depth description for the forking workflow can
[be found here](https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow)

Here are the steps:

1. Fork the repository. This can be done using the top right button on
   github.com on
    ```
    https://github.com/uwhackweek/learning-git
    ```

   ![Fork button](https://user-images.githubusercontent.com/17802172/116761105-95b42b00-a9cb-11eb-8332-37b68b432406.png)

   Choose your user account in the dialog and it will create
   a [fork](https://docs.github.com/en/github/getting-started-with-github/quickstart/github-glossary#fork)
   under your GitHub user account.

1. Go to your user page on github.com, get the URL, and clone the repository
   locally.
   
   For this, you can use a button on the GitHub user interface to copy the URL.

   ![clone url](images/clone.png)

   The below command has `<your-user-name>` as a sample placeholder. This
   should be replaced by your actual GitHub username.

    ```shell
    git clone https://github.com/<your-user-name>/learning-git.git
    ```

1. Once inside the newly cloned repository, add `UWhackweek` as the original source
   for your forked repository 
   
   This is step is considered adding a 
   [remote](https://docs.github.com/en/github/getting-started-with-github/quickstart/github-glossary#remote)
   to a repository.

   ```shell
    # Change to the directory
    cd learning-git
    # Add a new remote with the name 'UWhackweek' as the original fork source
    git remote add UWhackweek https://github.com/uwhackweek/learning-git.git
    ```

1. Verify that the remote was added successfully 
   
   List all remotes

   ```shell
   git remote -v
   ```

   The remote with the name `origin` is the default chosen name by git when you
   cloned the repository. This will always point to the URL of the one used in
   the `clone` command. 
   
   In our case it is:

   ```shell
   UWhackweek	https://github.com/uwhackweek/learning-git.git (fetch)
   UWhackweek	https://github.com/uwhackweek/learning-git.git (push)
   origin	https://github.com/<your-user-name>/learning-git.git (fetch)
   origin	https://github.com/<your-user-name>/learning-git.git (push)
   ```

1. Make a new branch

   ```shell
   # The '-b' is indicating a new branch with the name `new_branch`
   # It will also change to that.
   git checkout -b new_branch
   ```

   Output:
   ```shell
   Switched to a new branch 'new_branch'
   ```

1. Verify you are on the new branch

    ```shell
    # Show all branches of the repository, the current active has the `*`
    git branch
    ```

   Output:
    ```shell
    main
    * new_branch
    ```

1. Make changes within the new branch

   With this practice repository, you have to create a folder within
   **`contributions`** folder with your github username as the folder name. Use
   a new markdwon file (`.md`) or text file (`.txt`) file to practice git with.
   No other file types or folders are allowed outside your designated folder
   with this practice run.

1. Commit the changes

   ```shell
   # Add the new files
   git add .
   # Commit the changes
   git commit -m "My new files"
   ```

1. Push the changes to your forked repository

   ```shell
   git push origin new_branch
   ```

1. Create a pull request from your new branch
   
   Go to your user page on github.com. There, you will see a banner to create
   the pull request.
   
   ![pull request](images/pull-request.png)

1. Go to the pull request tab on the UW Hackweek website and celebrate!
   
   ```shell
    https://github.com/uwhackweek/learning-git/pulls
    ```

### Keeping up to date with changes to the source (origin)

By forking the repository, you created a snapshot at that point in time of
the `learning-git` repository. To get any changes from  the UW Hackweek repository 
copied into your version, you need to issue a pull command.

Here the steps:

1. Inside your forked repository
   
   The first command queries for all changes to the `main` branch on UW Hackweek.
   You added the `UWhackweek` remote in step number 3 above.
   ```shell
   git fetch UWhackweek
   ```
   Sample output:
   ```shell
   remote: Enumerating objects: 1, done.
   remote: Counting objects: 100% (1/1), done.
   remote: Total 1 (delta 0), reused 0 (delta 0), pack-reused 0
   Unpacking objects: 100% (1/1), 623 bytes | 623.00 KiB/s, done.
   From github.com:uwhackweek/learning-git
      03a9288..64e856e  main       -> UWhackweek/main

   ```

1. Go back to the `main` branch in your fork
   
   ```shell
   git checkout main
   ```

1. Transfer all the changes
   
   This will transfer all the changes since your fork command from the UW Hackweek
   main branch to your version of the main branch, making it up to date.

   ```shell
   git pull UWhackweek main
   ```

   Sample output:
   ```shell
   From github.com:uwhackweek/learning-git
   * branch            main       -> FETCH_HEAD
   Successfully mreged and updated refs/heads/main.
   ```

## Contributing through a branch

The following explains the steps to [contribute directly to a repository using
a branch](https://docs.github.com/en/github/getting-started-with-github/quickstart/github-flow).

In a nutshell, here the flow:

1. Clone the repository on your local computer

   :bangbang: **NOTE** This is different from the above as you are cloning the original
   repository and not your fork.

   Command:
   ```shell
   git clone https://github.com/uwhackweek/learning-git
   ```

1. Create a branch

   Choose a unique name that is not already taken in the repository and helps
   other collaborators to identify your work. In this case we are adding a branch
   with name 'feature_xyz'

   ```shell
   # The '-b' is indicating a new branch with the name `feature_xyz`
   # It will also change to that.
   git co -b feature_xyz
   ```

   Sample output:
   ```shell
   Switched to a new branch 'feature_xyz'
   ```

1. Verify you are on the new branch

    ```shell
    # Show all branches of the repository, the current active has the `*`
    git branch
    ```

   Output:
    ```shell
    main
    * feature_xyz
    ```

1. Make changes within the new branch

   With this practice repository, you have to create a folder within
   **`contributions`** folder with your GitHub username as the folder name. Use
   a new markdwon file (`.md`) or text file (`.txt`) file to practice git with.
   No other file types or folders are allowed outside your designated folder
   with this practice run.

1. Commit the changes

   ```shell
   # Add the new files
   git add .
   # Commit the changes
   git commit -m "My new files"
   ```

1. Push the changes to your forked repository

   ```shell
   git push origin feature_xyz
   ```

1. Create a pull request from your new branch

   Go to the repository page on github.com. There, you will see a banner to create
   the pull request.

   ![pull request](images/pull-request-branch.png)

1. Go to the pull request tab and celebrate!

   ```shell
    https://github.com/uwhackweek/learning-git/pulls
    ```

1. Clean up and delete the branch locally and on the website.

   Once your pull request is merged to the `main` branch, it is a good practice
   to delete the created branch. This has to be done in two places, once on
   the pull request page on github.com and the other on your local repository.

   For github.com, see the official documentation on
   [how to delete a branch](https://docs.github.com/en/github/administering-a-repository/managing-branches-in-your-repository/deleting-and-restoring-branches-in-a-pull-request#deleting-a-branch-used-for-a-pull-request)
   after it has been merged. In this practice repository, we have setup a rule
   that will take care of this step for you.

   Locally, however, you must still do this yourself and here the steps you
   need to execute within your local repository:

   ```shell
   # Go back to the `main` branch
   git checkout main
   # Get the latest changes that include your pull request
   git pull
   # Delete the branch. Here, our practice run branch `feature_xyz`
   # The -d flag is a safety option that only allows fully merged branches
   # to be deleted.
   git branch -d feature_xyz
   ```
---

## Resources

- [Git cheat sheet](https://training.github.com/downloads/github-git-cheat-sheet.pdf)
    
