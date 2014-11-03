Hosting Agent (HAgent)
======

Framework for configuration and management of the hosting environment

Advantages:
- Powered RESTful API
- Supports a wide range of software
- Supports OS CentOS / CloudLinux

Install:
```bash
cd /usr/local
git clone https://github.com/scopenco/hagent.git
cd /usr/local/hagent/puppet
puppet apply --modulepath modules/ manifests/default.pp
```

Test:
```bash
GET http://localhost:8000/status
{"status": 0}
```
