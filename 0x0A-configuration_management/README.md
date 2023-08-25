Puppet Mode is a major mode for [GNU Emacs](https://www.gnu.org/software/emacs/) 24 which adds support for the [Puppet](http://docs.puppetlabs.com/) language. Puppet is a system provisioning and configuration tool by Puppetlabs Inc. This mode supports Puppet 3 and later. Puppet 2 is not explicitly supported anymore, but should mostly work.

### ***Common Resource Types:***

- **package**: Manages software packages.
- **service**: Manages system services.
- **user**: Manages user accounts.
- **group**: Manages groups.
- **filebucket**: Manages file backups.
- **cron**: Manages cron jobs.
- **exec**: Executes commands on the system.
- **template**: Generates files from templates and data.
- **yumrepo**: Manages YUM repository configurations.
- **apt::source**: Manages APT repository configurations.

### ***Common Attributes:***

- **ensure**: Specifies whether a resource should be present or absent.
- **require**: Establishes a dependency relationship between resources.
- **before**: Specifies that one resource should be applied before another.
- **notify**: Triggers another resource to refresh if the current resource changes.
- **subscribe**: Causes a resource to refresh if another resource changes.
- **source**: Specifies the source file or content for a resource.
- **target**: Specifies the destination path for a file resource.
- **command**: Specifies the command to run for an exec resource.
- **creates**: Specifies a file that, if present, indicates that the exec resource doesn't need to run.
- **unless**: Specifies a command to run, and if it returns non-zero, the exec resource will run.
- **onlyif**: Specifies a command to run, and if it returns zero, the exec resource will run.

***execute a command with puppet :*** 

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9800db55-cee4-42ef-bac2-d8b986c3c50c/Untitled.png)

***install a package with puppet :***

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/18044a2e-b317-4d92-ba04-1bee9f5225e4/Untitled.png)

***example :*** 

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/aac3b76d-797b-4861-b93b-a9aa2429d498/Untitled.png)

***creating a file with puppet*** 

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a0006be8-3f8e-4516-bd34-f495077f8c0b/Untitled.png)
