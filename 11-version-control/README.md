
# Chapter 11: Version Control with Git

Welcome to Chapter 11! In this chapter, we dive into version control using Git, exploring its fundamental concepts, utilizing GitHub for remote repositories, and understanding the collaborative aspects of using Git in a team.

## Table of Contents

- [Introduction](#introduction)
- [Lesson Plan](#lesson-plan)
    - [Git Basics](#git-basics)
    - [GitHub and Remote Repositories](#github-and-remote-repositories)
    - [Collaborative Development with Git](#collaborative-development-with-git)
- [Mini-Example: Creating a Git Repository](#mini-example-creating-a-git-repository)
- [Project: Collaborative Document Editor](#project-collaborative-document-editor)
    - [Objective](#objective)
    - [Requirements](#requirements)
    - [Guidance](#guidance)
- [Quiz](#quiz)
- [Next Steps](#next-steps)
- [Additional Resources](#additional-resources)

## Introduction

Welcome to Chapter 11, where we will demystify the concepts of version control using Git and explore the collaborative world of GitHub. Version control is an indispensable tool in modern software development, facilitating a controlled environment for code changes. It ensures that you can gracefully navigate through different versions of your code, collaborate with others without overriding each other's work, and maintain a clean and traceable history of modifications.

In this chapter, we aim to introduce you to the essential concepts and skills related to Git and GitHub. We'll begin by understanding what version control is and why it is pivotal in managing project developments, especially when collaborating with others. Then, we will delve into the mechanics of Git - exploring how to initialize repositories, track files, create commits, and manage branches to introduce you to an organized way of handling your codebase.

Moreover, we will navigate through GitHub, a platform that brings developers together and hosts a vast array of projects from various domains. GitHub acts as a remote repository that not only backs up your code online but also provides a collaborative platform where developers from around the globe can contribute to projects.

Our journey will weave through the critical paths of collaboration - from cloning repositories and managing remote branches to understanding pull requests and resolving merge conflicts. The knowledge imbibed from this chapter will equip you with the proficiency to manage your projects using Git, collaborate on open-source projects on GitHub, and effectively work in a team where code changes are continuous and dynamic.

Get ready to dive into the world of efficient project management and collaborative development with Git and GitHub!


## Lesson Plan


### Git Basics

#### Introduction to Git

Git is a distributed version control system (VCS) that allows developers to track changes in their code during software development. It enables them to collaborate with others, manage changes to projects, and maintain a history of code modifications. Developed by Linus Torvalds in 2005, Git has become an essential tool for both individual developers and development teams, providing a systematic way to manage, version, and control access to code bases.

#### Setting Up Git

To start using Git, you must first install it and configure it on your system. The Git installation is straightforward and can be obtained from the [official Git website](https://git-scm.com/). Once installed, you can configure Git with your name and email address, which will be used to identify your commits.

```bash
git config --global user.name "Your Name"
git config --global user.email "yourname@example.com"
```

#### Basic Commands

- **`git init`**: This command initializes a new Git repository and begins tracking an existing directory. It adds a hidden subfolder within the existing directory that houses the internal data structure required for version control.

- **`git add`**: This command adds changes in the working directory to the staging area. It tells Git that you want to include updates to these files in the next commit.

- **`git commit`**: This command captures a snapshot of the project’s currently staged changes. Committed snapshots can be thought of as “safe” versions of a project—Git will never change them unless you explicitly ask it to.

- **`git status`**: This command shows the status of changes as untracked, modified, or staged.

- **`git log`**: This command shows the chronological commit history for a repository. This helps give context and history for a repository, and can also be used to explore the changes made by previous commits.

Here's a simple example to illustrate the basic Git workflow:

```bash
git init  # Initialize a new Git repo
git add filename  # Add a file to the staging area
git commit -m "Add initial version of file"  # Commit the file to the repository
```

#### Version Control and History

One of the key features of Git is the ability to track the history of changes to code. Each commit you make in Git stores a snapshot of the changes in your code, which you can revert to or use to explore the history of your project. The `git log` command allows you to view this history, while `git checkout [commit_hash]` lets you navigate to a previous state of the project.

#### Branching and Merging

Git allows you to create branches to work on different features or fixes in isolation. The `git branch` command is used to manage branches:

- **`git branch`**: Lists all local branches in the current repository.
- **`git branch [branch-name]`**: Creates a new branch.

`git merge` is used to combine various commits into a single history. Merging takes the contents of a source branch and integrates them with the target branch.

In the next sections, we'll explore how to work with remote repositories on GitHub and how to use Git for collaborative development. Be sure to practice the basics to become comfortable with the basic commands and workflows before moving on.



### GitHub and Remote Repositories

GitHub is an online platform that provides hosting for software development and a plethora of tools for version control using Git. It enables multiple people to work on projects at once, making it easier for teams to collaborate on project development seamlessly, regardless of where individual contributors are physically located.

#### Creating a Repository on GitHub

When you create a new project on GitHub, you are essentially creating a new repository. A repository (or "repo") is a storage space for your project, where all your project files are stored and the history of every file is tracked. Here’s how you can create a new repository on GitHub:

1. **Sign Up/Log In**: If you don’t have a GitHub account, you need to [create one](https://github.com/join). If you do, make sure you are logged in.
2. **New Repository**: Navigate to the [New repository](https://github.com/new) page, fill in your repository name, and provide a brief description. You also have the option to initialize this repository with a README file, but this is optional.
3. **Create Repository**: Click on “Create repository” and voilà, you have created your new repository.

#### Pushing to a Remote Repository

When you create a repository locally using Git and want to share it with others through GitHub, you need to push it to a remote repository. Here's a step-by-step guide to pushing your local repository to GitHub:

1. **Create a New Repository on GitHub**: Follow the steps mentioned above.
2. **Add Remote Repository**: Use the command `git remote add origin [repository-url]` to specify the new remote repository. You can find the `repository-url` on your GitHub repository page.
3. **Push the Repository**: Use `git push -u origin main` to push your local repository to GitHub.

### Note on Main Branch Name

Historically, the default branch name in Git has been "master". However, there has been a notable shift in the tech community towards more inclusive language. Thus, many projects and platforms, including GitHub, have started adopting "main" as the default branch name. This change is a part of a broader effort to remove language that might be perceived as racially charged or offensive. While you might still encounter repositories with a default branch named "master", especially in older projects, it's becoming increasingly common to see "main" used as the default branch name in newer projects and on various platforms.


#### Fetching, Pulling, and Cloning from a Remote Repository

- **Fetching**: When you want to get the data from your GitHub repository, you use `git fetch`. This command gets the updates from a remote repository into your local machine, but does not merge them with your work. It helps you to see what’s done by others before merging the changes with your work.
  
  Example: 
  ```bash
  git fetch origin
  ```
  
- **Pulling**: `git pull` is used to fetch the changes made in the remote repository and to merge those changes into your local repository. It is equivalent to running `git fetch` followed by `git merge`.
  
  Example: 
  ```bash
  git pull origin main
  ```
  
- **Cloning**: If you want to get a copy of an existing repository, you use `git clone [repository-url]`. This creates a local copy of the repository on your machine.
  
  Example: 
  ```bash
  git clone https://github.com/username/repository.git
  ```

#### Branching and Merging on GitHub

- **Creating a New Branch**: Use `git branch [branch-name]` to create a new branch. To switch to the new branch, use `git checkout [branch-name]`.
- **Merging Changes**: To merge changes from one branch to another, you switch to the branch you want to merge into and use `git merge [branch-name]` to merge the changes from the specified branch.

#### Pull Requests

Pull Requests (PRs) are a feature that allows developers to propose changes to a repository. After pushing your changes to a GitHub repository:

1. Navigate to the repository on GitHub and click on “Pull Request”.
2. Click on “New Pull Request” and choose the branch that has your updates.
3. Review the changes and click on “Create Pull Request”.
4. Fill in the title and description for the changes you made and then click on “Create Pull Request” again.

Pull requests allow for code review and discussion on the proposed changes before they are merged into the base branch of the repository.

#### Conclusion

Understanding GitHub and remote repositories is fundamental to modern collaborative software development. With knowledge of creating, pushing, fetching, and pulling repositories, alongside managing branches and handling pull requests, you can effectively contribute to projects and manage your own.

Keep in mind that this is a basic overview and there's much more to explore and learn in Git and GitHub, including resolving merge conflicts, revert and reset, stashing changes, and more. Ensure to dive deeper into each topic to enhance your knowledge and skills in using version control with Git and GitHub.


### Collaborative Development with Git

In a software development lifecycle, collaboration among developers is pivotal. Git provides powerful tools that facilitate collaborative development, allowing multiple developers to work on a project concurrently without interfering with each other's work. Let's delve into some concepts crucial for collaborative development using Git.

#### Branching in Git

In Git, a **branch** is essentially a pointer to a particular commit, but it represents a separate line of development. Branching allows developers to work in isolated environments within the Git repository, enabling them to work on different tasks concurrently without affecting the main line of development (often the `main` or `stable` branch).

```shell
git branch [branch_name]  # Creates a new branch
git checkout [branch_name]  # Switches to the specified branch
```

#### Merging Changes

**Merging** is the process of integrating changes from different branches. When you merge one branch into another, Git tries to automatically resolve the differences between the branches. If it can't, it will present a **merge conflict**.

```shell
git merge [branch_name]  # Merges the specified branch into the current branch
```

#### Merge Conflicts

A merge conflict arises when the changes in the branches being merged have conflicts in the same part of the file, and Git cannot determine which change should prevail. Developers must resolve these conflicts manually. Git marks the areas of the conflict in the file, and developers need to choose which code to keep.

```
<<<<<<< [current_branch]
    [Changes in the current branch]
=======
    [Changes in the other branch]
>>>>>>> [other_branch]
```

#### Pull Requests

A **Pull Request (PR)** is a feature of platforms like GitHub, GitLab, and Bitbucket. It allows developers to propose changes from a branch in their fork of the repository to a branch in the original repository. PRs contain the code differences, or **diffs**, between the branches, enabling easy code review.

1. **Fork the Repository**: Create a copy of the original repository to your GitHub account.
2. **Clone Your Fork**: Clone your forked repository to your local machine.
3. **Create a Branch**: Always create a new branch for your changes.
4. **Push Changes**: Make changes and push them to your GitHub repository.
5. **Open a Pull Request**: Go to the original repository and click on “New pull request”.

#### Code Reviews

Code reviews are an integral part of the collaborative development process. It involves developers reviewing each other's code, which is often facilitated through pull requests. Reviewing code helps ensure code quality, functionality, and maintainability.

- **Commenting**: Developers can comment on specific lines of code, propose changes, or ask for enhancements.
- **Approving**: If the changes are satisfactory, the reviewers approve the PR.
- **Merging**: After approval, the PR is merged into the target branch of the original repository.

#### Collaborative Workflows

There are various workflows that teams use for collaborative development in Git:

- **Feature Branch Workflow**: Every new feature is developed in a separate branch.
- **Gitflow Workflow**: It defines different branches for features, releases, and hotfixes.
- **Forking Workflow**: Developers fork the repository and work on their own fork, later creating PRs to contribute to the original repository.

Collaboration in Git, while powerful, does require meticulous management of branches, conscientious code reviews, and coordinated efforts among developers to ensure a smooth development process.

---



## Mini-Example: Creating a Git Repository

In this mini-example, we'll walk through the basic steps to create a new Git repository, make changes, and commit them. This hands-on example aims to provide a quick practical understanding of using Git.

### Step 1: Create a New Repository

First, let's create a new directory for our project and initialize a Git repository. Open your terminal or command prompt and execute the following commands:

```bash
mkdir MyFirstRepo
cd MyFirstRepo
git init
```

This creates a new folder named `MyFirstRepo` and initializes a new Git repository in it.

### Step 2: Make Changes

Next, create a new file in the repository and add some content to it. You might do this via your text editor or IDE, or through the command line as follows:

```bash
echo "Hello, Git!" > README.md
```

This creates a file named `README.md` and writes "Hello, Git!" to it.

### Step 3: Track Changes

Now, let's track our new file using Git. We'll add it to the staging area and then commit the changes:

```bash
git add README.md
git commit -m "Add README.md"
```

`git add` stages the changes for commit, and `git commit` saves the staged changes along with a commit message describing what was done.

### Step 4: View Commit History

Lastly, you can view the history of your commits using:

```bash
git log
```

This will display a list of all the commits made in the repository, showing the commit ID, author, date, and commit message.

Congratulations! You've just created a new Git repository, made changes, and recorded those changes using a commit. This forms the basis of version control, enabling you to manage and track the history of your project.


## Project: Collaborative Document Editor

### Objective

The primary goal of this project is to construct a collaborative document editor using Git and GitHub, which allows multiple users to contribute to a document in a controlled and structured manner. By harnessing the power of version control, you'll manage changes from multiple contributors, resolve conflicts, and evolve a document through collective inputs while maintaining its integrity and history.

### Requirements

- **Collaborative Environment**: Set up a GitHub repository that will serve as the collaborative environment for the document.
- **Document Evolution**: Ensure the document evolves through at least five versions, showcasing your understanding of commits and version history.
- **Conflict Management**: Intentionally create a scenario where a merge conflict occurs and resolve it.
- **Use of Branches**: Implement at least two feature branches and merge them back into the main branch upon completion.
- **Pull Requests and Code Review**: Utilize pull requests and perform a code review on at least one of them.

### Guidance

1. **Setting Up the Repository**:
   - Create a new repository on GitHub and clone it to your local machine.
   - Initialize your document. It could be a simple text file, markdown, or any format you are comfortable with.

2. **Contributing to the Document**:
   - Make changes to the document and commit them to the repository, ensuring that commit messages are clear and descriptive.
   - Push your changes to the GitHub repository and observe the evolution of the document through the commit history.

3. **Branching and Merging**:
   - Create a new branch for a specific feature or section of the document.
   - Make changes in this branch and once satisfied, merge it back into the main branch. Ensure you understand and can explain the merge process.

4. **Handling Conflicts**:
   - Create a scenario where you modify the same part of the document in two different branches and try to merge them to produce a conflict.
   - Resolve the conflict, commit the resolved version, and understand the implications on the commit history.

5. **Collaboration and Review**:
   - If possible, collaborate with a peer. You could ask them to clone your repository, create a new branch, make changes, and submit a pull request.
   - Review the pull request, make comments, and finally merge it into your main branch.

Remember: The key to success in this project lies in understanding the workflow and mechanics of Git and GitHub, rather than the content of the document you are creating. Ensure to follow best practices and use the various features of Git and GitHub as described in this chapter.

Feel free to explore the basic source code for a document editor provided in the chapter's `/code/` folder to get started! Once you have attempted to establish a collaborative development environment and made some progress, check out the detailed solution guide provided in the `/code/answer/` folder. This guide will walk you through an example setup, collaboration, development, and release process using Git and GitHub, offering insights that might be helpful for your project work.

## Quiz

Quizzes will be added at a later date.

## Next Steps

Congratulations on completing this chapter! In the next chapter, we will work on our final project of this series... [Go to Chapter 12](12-final-project/README.md).

## Additional Resources

- [Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials/)

---
Happy Coding! 🚀

[Back to Main](../README.md)