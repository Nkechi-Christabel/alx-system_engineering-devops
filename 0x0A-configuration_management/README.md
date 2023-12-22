# Configuration management

<img src="https://cdnblog.filecloud.com/blog/wp-content/uploads/2014/08/CMTs1.jpg" alt="configuration management" width="100%" height="auto">

## About
Configuration Management is the process of maintaining systems, such as computer hardware and software, in a desired state. Configuration Management (CM) is also a method of ensuring that systems perform in a manner consistent with expectations over time.

Configuration management tools, like Puppet, provide a way to automate this process, reducing the need for manual intervention and minimizing the potential for errors.

Puppet is a configuration management tool that allows you to define your infrastructure as code. This means that you can write code to describe how your infrastructure should be configured, and Puppet will automatically enforce that configuration across all the systems it manages.

Puppet uses a client-server architecture, where a Puppet master server controls a fleet of Puppet agents running on managed nodes. The Puppet master server holds the configuration data, while the Puppet agents apply the configurations to the nodes they manage.

## Project Requirements

- All your files will be interpreted on `Ubuntu 20.04 LTS`
- All your files should end with a new line
- A __README.md__ file at the root of the folder of the project is mandatory
- Your Puppet manifests must pass `puppet-lint version 2.1.1` without any errors
- Your Puppet manifests must run without error
- Your Puppet manifests first line __must be a comment__ explaining what the Puppet manifest is about
- Your Puppet manifests files must end with the extension __.pp__

## Resources

__Read or Watch__
1. [Introduction to configuration management](https://www.digitalocean.com/community/tutorials/an-introduction-to-configuration-management)
2. [Puppet Resource file type](https://www.puppet.com/docs/puppet/5.5/types/file.html)
3. [Puppet's declarative language: Modelling instead of scripting](https://www.puppet.com/blog)
4. [Puppet-lint](http://puppet-lint.com/)
5. [Puppet emacs mode](https://github.com/voxpupuli/puppet-mode)

## Note on versioning
Your Ubuntu 20.04 VM should have Puppet 5.5 preinstalled.

### Install ```puppet```

```
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
```
You do not need to attempt to upgrade versions. This project is simply a set of tasks to familiarize you with the basic level syntax which is virtually identical in newer versions of Puppet.

[Puppet 5 docs](https://www.puppet.com/docs/puppet/5.5/puppet_index.html)

### Install puppet-lint
```
$ gem install puppet-lint
```
