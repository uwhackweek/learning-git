# Learning Git Version Control System

Repository for learning git and github collaboratively.

---

This repository can be used to practice git [forking workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow) within github.

Here are the steps:

1. Fork the repository. (There's a fork button on top right of the window on a desktop browser.)![Fork button](https://user-images.githubusercontent.com/17802172/116761105-95b42b00-a9cb-11eb-8332-37b68b432406.png)
2. Clone the repository locally. 
    
    ```
    git clone https://github.com/uwhackweek/learning-git.git
    ```
    
3. Add your forked repository as a remote source.

    ```
    git remote add fork https://github.com/github-user/learning-git.git
    ```

4. Make a new branch.

    ```
    git checkout -b new_branch
    ```

4. Make changes within the new branch. (NOTE: you *MUST* create a folder within **`contributions`** folder with your github handle as the folder name, and then you can add **`.md`** or **`.txt`** file(s) to practice git with. No other file types or folders are allowed outside your designated folder.)

5. Commit the changes.

    ```
    git add .
    git commit -m "My new files"
    ```

6. Push the changes to your forked repository.

    ```
    git push fork new_branch
    ```

7. Create a pull request from your new branch in forked repository by going to github **Pull requests > New pull request**.

---
### Resources

- [Git cheat sheet](https://training.github.com/downloads/github-git-cheat-sheet.pdf)
    
