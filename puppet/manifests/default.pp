# vim: ft=puppet
# Author: Andrey Scopenco <andrey@scopenco.net>
# puppet apply --modulepath modules/ manifests/default.pp

node default {

    Exec {
        path            => [ "/bin/", "/sbin/" , "/usr/bin/", "/usr/sbin/" ],
        logoutput       => "on_failure"
    }

    class { "hagent": uid => "991", gid => "991" }
    class { "lighttpd": owner => "hagent", group => "hagent" }
}
