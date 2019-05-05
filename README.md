<!--
name: README.md
description: This file contains important information for the repository.
author: while-true-do.io
contact: hello@while-true-do.io
license: BSD-3-Clause
-->

<!-- github shields -->
[![Github (tag)](https://img.shields.io/github/tag/while-true-do/ansible-role-srv_kvm.svg)](https://github.com/while-true-do/ansible-role-srv_kvm/tags)
[![Github (license)](https://img.shields.io/github/license/while-true-do/ansible-role-srv_kvm.svg)](https://github.com/while-true-do/ansible-role-srv_kvm/blob/master/LICENSE)
[![Github (issues)](https://img.shields.io/github/issues/while-true-do/ansible-role-srv_kvm.svg)](https://github.com/while-true-do/ansible-role-srv_kvm/issues)
[![Github (pull requests)](https://img.shields.io/github/issues-pr/while-true-do/ansible-role-srv_kvm.svg)](https://github.com/while-true-do/ansible-role-srv_kvm/pulls)
<!-- travis shields -->
[![Travis (com)](https://img.shields.io/travis/com/while-true-do/ansible-role-srv_kvm.svg)](https://travis-ci.com/while-true-do/ansible-role-srv_kvm)
<!-- ansible shields -->
[![Ansible (min. version)](https://img.shields.io/badge/dynamic/yaml.svg?label=Min.%20Ansible%20Version&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-srv_kvm%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.min_ansible_version&colorB=black)](https://galaxy.ansible.com/while_true_do/srv_kvm)
[![Ansible (platforms)](https://img.shields.io/badge/dynamic/yaml.svg?label=Supported%20OS&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-srv_kvm%2Fmaster%2Fmeta%2Fmain.yml&query=galaxy_info.platforms%5B*%5D.name&colorB=black)](https://galaxy.ansible.com/while_true_do/srv_kvm)
[![Ansible (tags)](https://img.shields.io/badge/dynamic/yaml.svg?label=Galaxy%20Tags&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-srv_kvm%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.galaxy_tags%5B*%5D&colorB=black)](https://galaxy.ansible.com/while_true_do/srv_kvm)

# Ansible Role: srv_kvm

An Ansible Role to install and configure a kvm host.

## Motivation

[KVM](https://www.linux-kvm.org/page/Main_Page) in combination with
[libvirt](https://libvirt.org/) is the major Linux hypervisor. Installing and
configuring KVM is a very common task for most operators and engineers.

## Description

This role configures a KVM hypervisor:

-   install qemu-kvm
-   install libvirt
-   install [ksm](https://www.linux-kvm.org/page/KSM) support and service
-   install [kvm nesting](https://www.linux-kvm.org/page/Nested_Guests) support

## Requirements

Used Modules:

-   [Ansible Package Module](https://docs.ansible.com/ansible/latest/modules/package_module.html)
-   [Ansible Service Module](https://docs.ansible.com/ansible/latest/modules/service_module.html)
-   [Ansible Template Module](https://docs.ansible.com/ansible/latest/modules/template_module.html)
-   [Ansible Command Module](https://docs.ansible.com/ansible/latest/modules/command_module.html)
-   [Ansible Reboot Module](https://docs.ansible.com/ansible/latest/modules/reboot_module.html)


## Installation

Install from [Ansible Galaxy](https://galaxy.ansible.com/while_true_do/srv_kvm)
```
ansible-galaxy install while_true_do.srv_kvm
```

Install from [Github](https://github.com/while-true-do/ansible-role-srv_kvm)
```
git clone https://github.com/while-true-do/ansible-role-srv_kvm.git while_true_do.srv_kvm
```

## Usage

### Role Variables

```
---
# defaults file for while_true_do.srv_kvm

wtd_srv_kvm_package:
  - qemu-kvm
  - libvirt
# State can be present|latest|absent
wtd_srv_kvm_package_state: "present"

wtd_srv_kvm_service: "libvirtd"
# State can be started|stopped
wtd_srv_kvm_service_state: "started"
# Enabled can be true|false
wtd_srv_kvm_service_enabled: true

# Nested virtualization
wtd_srv_kvm_nested_manage: true
# State can be present|absent
wtd_srv_kvm_nested_state: "present"

# Kernel Samepage Merging
wtd_srv_kvm_ksm_manage: true
# Packages included dynamically
wtd_srv_kvm_ksm_package:
  - ksmtuned
# State can be present|latest|absent
wtd_srv_kvm_ksm_package_state: "present"
wtd_srv_kvm_ksm_service:
  - ksm
  - ksmtuned
# State can be started|stopped
wtd_srv_kvm_ksm_service_state: "started"
wtd_srv_kvm_ksm_service_enabled: true
wtd_srv_kvm_ksm_conf:
# MONITOR_INTERVAL: 60
# SLEEP_MSEC: 10
# NPAGES_BOOST: 300
# NPAGES_DECAY: -50
# NPAGES_MIN: 64
# NPAGES_MAX: 1250
# THRES_COEF: 20
# THRES_CONST: 2048

# Auto Reboot when needed
wtd_srv_kvm_reboot_enable: true
wtd_srv_kvm_reboot_msg: "System is going down to apply kvm configuration."
wtd_srv_kvm_reboot_timeout: 3600
```

### Example Playbook

Running Ansible
[Roles](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html)
can be done in a
[playbook](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html).

#### Simple

```
---
- hosts: all
  roles:
    - role: while_true_do.srv_kvm
```

#### Advanced

Don't install ksm support and don't reboot after kvm nested configuration.

```
- hosts: all
  roles:
    - role: while_true_do.srv_kvm
      wtd_srv_kvm_ksm_manage: false
      wtd_srv_kvm_reboot_enable: false
```

## Testing

Most of the "generic" tests are located in the
[Test Library](https://github.com/while-true-do/test-library).

Ansible specific testing is done with
[Molecule](https://molecule.readthedocs.io/en/stable/).

Infrastructure testing is done with
[testinfra](https://testinfra.readthedocs.io/en/stable/).

Automated testing is done with [Travis CI](https://travis-ci.com/while-true-do).

## Contribute

Thank you so much for considering to contribute. We are very happy, when somebody
is joining the hard work. Please fell free to open
[Bugs, Feature Requests](https://github.com/while-true-do/ansible-role-srv_kvm/issues)
or [Pull Requests](https://github.com/while-true-do/ansible-role-srv_kvm/pulls) after
reading the [Contribution Guideline](https://github.com/while-true-do/doc-library/blob/master/docs/CONTRIBUTING.md).

See who has contributed already in the [kudos.txt](./kudos.txt).

## License

This work is licensed under a [BSD-3-Clause License](https://opensource.org/licenses/BSD-3-Clause).

## Contact

-   Site <https://while-true-do.io>
-   Twitter <https://twitter.com/wtd_news>
-   Code <https://github.com/while-true-do>
-   Mail [hello@while-true-do.io](mailto:hello@while-true-do.io)
-   IRC [freenode, #while-true-do](https://webchat.freenode.net/?channels=while-true-do)
-   Telegram <https://t.me/while_true_do>
