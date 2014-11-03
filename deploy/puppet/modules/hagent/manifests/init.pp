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
        ensure => present,
        owner  => "hagent",
        group  => "hagent",
        mode   => "0640",
        require => Package["bash"],
    }

    file {
        "/usr/local/hagent/.bashrc":
            source  =>  "/etc/skel/.bashrc";

        "/usr/local/hagent/.bash_profile":
            source  =>  "/etc/skel/.bash_profile";

        "/usr/local/hagent/.bash_logout":
            source  =>  "/etc/skel/.bash_logout";
    }

    file {
        "/etc/init.d/hagent":
            owner  => "root",
            group  => "root",
            mode   => "0755",
            source  =>  "/usr/local/hagent/init.d/hagent";
    }
}
