# vim: ft=puppet
# $Author: ascopenco $
# Maintainer: ascopenco@mchost.ru
# Description: lighttpd module

class lighttpd::params {
    $owner = "lighttpd"
    $group = "lighttpd"
}

class lighttpd (
    $owner = $lighttpd::params::owner,
    $group = $lighttpd::params::group,
    ) inherits lighttpd::params {

    package { ["lighttpd", "lighttpd-fastcgi"]:
            allow_virtual => false,
            ensure => installed,
    }

    File {
        ensure => "present",
        owner  => $owner,
        group  => $group,
        mode   => "0640",
        require => Package["lighttpd-fastcgi"],
    }

    file {
        ["/var/log/lighttpd", "/etc/lighttpd"]:
            ensure => "directory",
            mode => "0750";

        "/etc/lighttpd/lighttpd.conf":
            source => "puppet:///modules/lighttpd/lighttpd.conf",
            notify => Service["lighttpd"];
    }

    service {
        "lighttpd":
            ensure      => running,
            enable      => true,
            hasstatus   => true,
            require     => Package["lighttpd"];
    }
}
