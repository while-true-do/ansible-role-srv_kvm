import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_kvm_package(host):
    pkg = host.package('qemu-kvm')
    assert pkg.is_installed


def test_libvirt_package(host):
    pkg = host.package('libvirt')
    assert pkg.is_installed


def test_libvirt_service(host):
    srv = host.service('libvirtd')
    assert srv.is_running
    assert srv.is_enabled


def test_ksm_service(host):
    vrt = host.ansible("setup")["ansible_facts"]["ansible_virtualization_type"]
    if vrt != 'docker':
        srv = host.service('ksm')
        assert srv.is_running
        assert srv.is_enabled


def test_ksmtuned_service(host):
    vrt = host.ansible("setup")["ansible_facts"]["ansible_virtualization_type"]
    if vrt != 'docker':
        srv = host.service('ksmtuned')
        assert srv.is_running
        assert srv.is_enabled
