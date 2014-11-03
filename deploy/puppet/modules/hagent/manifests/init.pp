# vim: ft=puppet

class hagent::params {
    $uid = "997"
    $gid = "997"
}

class hagent (
    $uid = $hagent::params::uid,
    $gid = $hagent::params::gid
    ) inherits hagent::params {

    Group["hagent"] -> User["hagent"]

    group { "hagent":
        ensure  => present,
        gid     => $gid;
    }

    user { "hagent":
        home    => "/usr/local/hagent",
        shell   => "/bin/bash",
        uid     => $uid,
        gid     => $gid,
    }

    package { ["bash", "python", "python-flup"]:
            allow_virtual => false,
            ensure => installed,
    }

    File {
        ensure => "present",
        owner  => "hagent",
        group  => "hagent",
        mode   => "0640",
        require => Package["bash"],
    }

    # useful skeleton
    file {
        "/usr/local/hagent/.bashrc":
            source  =>  "/etc/skel/.bashrc";

        "/usr/local/hagent/.bash_profile":
            source  =>  "/etc/skel/.bash_profile";

        "/usr/local/hagent/.bash_logout":
            source  =>  "/etc/skel/.bash_logout";
    }

    file {
        ["/usr/local/hagent/lib", "/usr/local/hagent/sbin",
        "/usr/local/hagent/var", "/usr/local/hagent/etc", ]:
            ensure  => "directory",
            mode    => "0750";

        ["/usr/local/hagent/sbin/hagent", ]:
            mode    => "0750";

        "/usr/local/hagent/etc/hagent.conf":
            source  =>  "puppet:///modules/hagent/hagent.conf",
            notify  => Service["hagent"];

        "/usr/local/hagent/etc/logrotate.conf":
            source  =>  "puppet:///modules/hagent/hagent.logrotate";

        "/etc/sysconfig/hagent":
            source  =>  "puppet:///modules/hagent/hagent.sysconfig";

        "/etc/init.d/hagent":
            owner  => "root",
            group  => "root",
            mode    => "0755",
            source  =>  "puppet:///modules/hagent/hagent.initd",
            notify => Service["hagent"];
    }

    service {
         "hagent":
            enable    => "true",
            ensure    => "running",                                                                                                                                                   
            require   => File["/etc/init.d/hagent"];
     }
}
