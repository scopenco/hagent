#Commercial HAgent API 1.0
The sections below provide a comprehensive listing of the REST/CLI resources exposed by Commercial version of HAgent.  
Questions related to the licensing or purchase of this decision can be discussed by email <andrey@scopenco.net>

[TOC]
##ACCOUNT (REST/CLI)
###Create account
__Description__: Create virtual account, used for assign resources.  
__Sample Output__:
```bash
# Create account a1000 with preset tarif1
GET /api/v1/?module=account&func=create&account=a1000&preset=tarif1
{
    "status": "ok",
    "status_msg": "Account a1000 created"
}
```
###Remove account
__Description__: Remove account with all assigned resources (domains, databases, etc.).  
__Sample Output__:
```bash
# Remove account a1000
GET /api/v1/?module=account&func=delete&account=a1000
{
    "status": "ok",
    "status_msg": "Account a1000 removed"
}
```
###Lock account
__Description__: Disable account with all assigned resources (domains, databases, etc.).  
__Sample Output__:
```bash
# Disable account a1000
GET /api/v1/?module=account&func=lock_on&account=a1000
{
    "status": "ok",
    "status_msg": "Account a1000 modified"
}
```
###Unlock account
__Description__: Enable account with all assigned resources (domains, databases, etc.).  
__Sample Output__:
```bash
# Enable account a1000
GET /api/v1/?module=account&func=lock_off&account=a1000
{
    "status": "ok",
    "status_msg": "Account a1000 modified"
}
```
###Change preset for account
__Description__: Change preset(tariff) for account.  
__Sample Output__:
```bash
# Change preset for account a1000 to tarif2
GET /api/v1/?module=account&func=preset&account=a1000&preset=tarif2
{
    "status": "ok",
    "status_msg": "Account a1000 modified"
}
```
##WWW (REST/CLI)
###Create http virtual host
__Description__: Create http virtual host and assign to account.  
__Notes__: Support disable restart httpd for multiple creation (&restart=0). It's possible to set PHP version (&fcgi=php53)  
__Sample Output__:
```bash
# Create virtual host for domain domain.com, ftp login a1000_1 with password test, assign to account a1000
GET /api/v1/?module=www&func=domain_add&account=a1000&login=a1000_1&passwd=test&domain=domain.com
{
    "status": "ok",
    "status_msg": "Domain domain.com created"
}
```
###Remove http virtual host
__Description__: Remove http virtual host with assigned resources (subdomains, aliases).  
__Notes__: Support disable restart httpd for multiple removing (&restart=0).  
__Sample Output__:
```bash
# Remove virtual host domain.com with assigned ftp account
GET /api/v1/?module=www&func=domain_del&domain=domain.com
{
    "status": "ok",
    "status_msg": "Domain domain.com removed"
}
```
###Lock http virtual host
__Description__: Disable http virtual host with assigned resources (subdomains, aliases).  
__Notes__: Support disable restart httpd for multiple locking (&restart=0).  
__Sample Output__:
```bash
# Disable virtual host domain.com, ftp account remain active.
GET /api/v1/?module=www&func=domain_lock_on&domain=domain.com
{
    "status": "ok",
    "status_msg": "Domain domain.com modified"
}
```
###Unlock http virtual host
__Description__: Enable http virtual host with assigned resources (subdomains, aliases).  
__Notes__: Support disable restart httpd for multiple unlocking (&restart=0).  
__Sample Output__:
```bash
# Enable virtual host domain.com
GET /api/v1/?module=www&module=www&func=domain_lock_off&domain=domain.com
{
    "status": "ok",
    "status_msg": "Domain domain.com modified"
}
```
###Enable awstats for virtual host
__Description__: Activate awstats statistics for virtual host.  
__Notes__: Support disable restart httpd for multiple tasks (&restart=0).  
__Sample Output__:
```bash
# Activate web statistics Awstats for domain domain.com
GET /api/v1/?module=www&func=domain_stats_on&stats=awstats&domain=domain.com
{
    "status": "ok",
    "status_msg": "Domain domain.com modified"
}
```
###Enable webalizer for virtual host
__Description__: Activate webalizer statistics for virtual host.  
__Notes__: Support disable restart httpd for multiple tasks (&restart=0).  
__Sample Output__:
```bash
# Activate web statistics Webalizer for domain domain.com
GET /api/v1/?module=www&func=domain_stats_on&stats=webalizer&domain=domain.com
{
    "status": "ok",
    "status_msg": "Domain domain.com modified"
}
```
###Disable web stats for virtual host
__Description__: Disable web statistics (awstats/webalizer) for virtual host.  
__Notes__: Support disable restart httpd for multiple tasks (&restart=0).  
__Sample Output__:
```bash
# Disable any web statistics for domain domain.com
GET /api/v1/?module=www&func=domain_stats_off&domain=domain.com
{
    "status": "ok",
    "status_msg": "Domain domain.com modified"
}
```
###Activate php fastcgi for virtual host
__Description__: Activate PHP FastCGI for virtual host.  
__Notes__: Support disable restart httpd for multiple tasks (&restart=0). Supported PHP versions 5.2 5.3 5.4 5.5.
__Sample Output__:
```bash
# Activate PHP FastCGI 5.5 for virtual host domain.com
GET /api/v1/?module=www&func=domain_fcgi_on&fcgi=php55&domain=domain.com
{
    "status": "ok",
    "status_msg": "Domain domain.com modified"
}
```
###Disable php fastcgi for virtual host
__Description__: Disable PHP FastCGI for virtual host.  
__Notes__: Support disable restart httpd for multiple tasks (&restart=0).  
__Sample Output__:
```bash
# Disable PHP for virtual host domain.com
GET /api/v1/?module=www&func=domain_fcgi_on&fcgi=php52&domain=domain.com
{
    "status": "ok",
    "status_msg": "Domain domain.com modified"
}
```
###Activate custom nginx config for virtual host
__Description__: Activate custom nginx config for virtual host.  
__Notes__: Support disable restart httpd for multiple tasks (&restart=0).  
__Sample Output__:
```bash
# Activate custom nginx config for virtual host domain.com
GET /api/v1/?module=www&func=domain_nginx_custom_on&domain=domain.com
{
    "status": "ok",
    "status_msg": "Domain domain.com modified"
}
```
###Disable custom nginx config for virtual host
__Description__: Disable custom nginx config for virtual host.  
__Notes__: Support disable restart httpd for multiple tasks (&restart=0).  
__Sample Output__:
```bash
# Disable custom nginx config and enable common config for virtual host domain.com
GET /api/v1/?module=www&func=domain_nginx_custom_off&domain=domain.com
{
    "status": "ok",
    "status_msg": "Domain domain.com modified"
}
```
###Change ftp password for virtual host
__Description__: Change ftp password for virtual host.  
__Notes__: Support disable restart httpd for multiple tasks (&restart=0).  
__Sample Output__:
```bash
# Change ftp password for virtual host domain.com to 'test2'
GET /api/v1/?module=www&func=domain_passwd&passwd=test2&domain=domain.com
{
    "status": "ok",
    "status_msg": "Domain domain.com modified"
}
```
###Activate SSL for virtual host
__Description__: Activate SSL for virtual host.  
__Notes__: Support disable restart httpd for multiple tasks (&restart=0).  
__Sample Output__:
```bash
# Activate ssl cert pair 'default' for virtual host domain.com
GET /api/v1/?module=www&func=domain_ssl_on&ssl=default&domain=domain.com
{
    "status": "ok",
    "status_msg": "Domain domain.com modified"
}
```
###Disable SSL for virtual host
__Description__: Disable SSL for virtual host.  
__Notes__: Support disable restart httpd for multiple tasks (&restart=0).  
__Sample Output__:
```bash
# Disable SSL for virtual host domain.com
GET /api/v1/?module=www&func=domain_ssl_off&domain=domain.com
{
    "status": "ok",
    "status_msg": "Domain domain.com modified"
}
```
###Activate dedicated IP address for virtual host
__Description__: Activate dedicated IP address for virtual host. IP address should be assigned to account before activation for virtual host.   
__Notes__: Support disable restart httpd for multiple tasks (&restart=0).  
__Sample Output__:
```bash
# Activate ip address 192.168.1.4 for virtual host domain.com
GET /api/v1/?module=www&func=domain_ip_on&ip=192.168.1.4&domain=domain.com
{
    "status": "ok",
    "status_msg": "Domain domain.com modified"
}
```
###Disable dedicated IP address for virtual host
__Description__: Disable dedicated IP address for virtual host.  
__Notes__: Support disable restart httpd for multiple tasks (&restart=0).  
__Sample Output__:
```bash
# Disable dedicated ip address for virtual host domain.com
GET /api/v1/?module=www&func=domain_ip_off&domain=domain.com
{
    "status": "ok",
    "status_msg": "Domain domain.com modified"
}
```
###Create www alias for virtual host
__Description__: Create www alias for virtual host. Realised as adding ServerAlias for Apache and server_name for Nginx.   
__Sample Output__:
```bash
# Create www alias alias1.domain.com for virtual host domain.com
GET /api/v1/?module=www&func=domain_alias_add&alias=alias1.domain.com&domain=domain.com
{
    "status": "ok",
    "status_msg": "DomainAlias alias1.domain.com created."
}
```
###Remove www alias for virtual host
__Description__: Remove www alias for virtual host.  
__Sample Output__:
```bash
# Remove www alias alias1.domain.com
GET /api/v1/?module=www&func=domain_alias_del&alias=alias1.domain.com
{
    "status": "ok",
    "status_msg": "DomainAlias alias1.domain.com removed."
}
```
###Create subdomain
__Description__: Create subdomain for virtual host. Subdomains are located in directory 'subdomain' in home dir of virtual host.  
__Notes__: Support disable restart httpd for multiple tasks (&restart=0).  
__Sample Output__:
```bash
# Create subdomain for virtual host domain.com
GET /api/v1/?module=www&func=subdomain_add&domain=domain.com&subdomain=sub1.domain.com
{
    "status": "ok",
    "status_msg": "SubDomain sub1.domain.com created"
}
```
###Remove subdomain
__Description__: Remove subdomain for virtual host.  
__Notes__: Support disable restart httpd for multiple tasks (&restart=0).  
__Sample Output__:
```bash
# Remove subdomain sub1.domain.com
GET /api/v1/?module=www&func=subdomain_del&subdomain=sub1.domain.com
{
    "status": "ok",
    "status_msg": "SubDomain sub1.domain.com removed"
}
```
###Lock subdomain
__Description__: Lock subdomain for virtual host.  
__Notes__: Support disable restart httpd for multiple tasks (&restart=0).  
__Sample Output__:
```bash
# Lock subdomain sub1.domain.com
GET /api/v1/?module=www&func=subdomain_lock_on&subdomain=sub1.domain.com
{
    "status": "ok",
    "status_msg": "SubDomain dom1.host1.dev.mchost.ru modified"
}
```
###Unlock subdomain
__Description__: Unlock subdomain for virtual host.  
__Notes__: Support disable restart httpd for multiple tasks (&restart=0).  
__Sample Output__:
```bash
# Unlock subdomain sub1.domain.com
GET /api/v1/?module=www&func=subdomain_lock_off&subdomain=sub1.domain.com
{
    "status": "ok",
    "status_msg": "SubDomain sub1.domain.com modified"
}
```
###Activate ftp for subdomain
__Description__: This fuction allow to create dedicated ftp account for subdomain. By default subdomain has the same ftp account like virtual host.  
__Sample Output__:
```bash
# Activate ftp account 'a1001' with password 'test' for subdomain sub1.domain.com
GET /api/v1/?module=www&func=subdomain_login_on&passwd=test&login=a1001&subdomain=sub1.domain.com
{
    "status": "ok",
    "status_msg": "SubDomain sub1.domain.com modified"
}
```
###Disable ftp for subdomain
__Description__: Disable dedicated ftp account for subdomain.  
__Sample Output__:
```bash
# Remove ftp account for subdomain sub1.domain.com
GET /api/v1/?module=www&func=subdomain_login_off&subdomain=sub1.domain.com
{
    "status": "ok",
    "status_msg": "SubDomain sub1.domain.com modified"
}
```
###Change ftp password for subdomain
__Description__: Change ftp password for subdomain.  
__Sample Output__:
```bash
# Change ftp password for subdomain sub1.domain.com to 'test2'
GET /api/v1/?module=www&func=subdomain_passwd&passwd=test2&subdomain=sub1.domain.com 
{
    "status": "ok",
    "status_msg": "SubDomain sub1.domain.com modified"
}
```
## WWW (CLI)
Next maintenance fuctions working only for CLI hagent.
###Activate web accoess to http logs for virtual host
__Description__: Activate web accoess to http logs for virtual host. Account can access to apache/nginx logs by http base auth.   
__Sample Output__:
```bash
# Activate web accoess to http logs for virtual host domain.com
bash bin/agent module=www func=domain_htpasswd domain=domain.com
{
    "status": "ok",
    "status_msg": "htpasswd for domain domain.com has been created"
}
```
###Activate http log rotation for virtual host
__Description__: Activate http (apache/nginx) log rotation for virtual host.   
__Sample Output__:
```bash
# Activate http log rotation for virtual host domain.com
bash bin/agent module=www func=domain_logrotate domain=domain.com
{
    "status": "ok",
    "status_msg": "configured logrotate for domain domain.com"
}
```
###Fix dirs permissions for home dir of virtual host without recursion
__Description__: Fuction will check dir structure and fix permissions in home dir of virtual host.   
__Sample Output__:
```bash
# Fix dirs permissions for virtual host domain.com
bash bin/agent module=www func=domain_chmody_rec_off domain=domain.com
{
    "status": "ok",
    "status_msg": "fixed permissions for domain domain.com with recursion off"
}
```
###Fix dirs permissions for home dir of virtual host with recursion
__Description__: Fuction will check dir structure and fix permissions in home dir of virtual host with recursion (long-time operation).   
__Sample Output__:
```bash
# Fix dir permissions for virtual host domain.com with recursion
bash bin/agent module=www func=domain_chmody_rec_off domain=domain.com
{
    "status": "ok",
    "status_msg": "fixed permissions for domain domain.com with recursion on"
}
```
###Fix dirs permissions for all virtual hosts without recursion
__Description__: Fuction will check dir structure and fix permissions in home dirs of all virtual hosts without recursion.   
__Sample Output__:
```bash
bash bin/agent module=www func=domain_chmody_all_rec_off
{
    "status": "ok",
    "status_msg": "fixed permissions for all domains with recursion off"
}
```
###Fix dirs permissions for all virtual hosts with recursion
__Description__: Fuction will check dir structure and fix permissions in home dirs of all virtual hosts with recursion.   
__Sample Output__:
```bash
bash bin/agent module=www func=domain_chmody_all_rec_on
{
    "status": "ok",
    "status_msg": "fixed permissions for all domains with recursion on"
}
```
###Regenerate http configs for virtual host
__Description__: Fuction regenerate nginx/apache configs for virtual host.   
__Notes__: Support disable restart httpd for multiple tasks (restart=0).  
__Sample Output__:
```bash
# Regenerate http configs for virtual host domain.com
bash bin/agent module=www func=domain_regen_web domain=domain.com
{
    "status": "ok",
    "status_msg": "regenerate httpd conf for domain domain.com complete."
}
```
###Regenerate http configs for all virtual hosts
__Description__: Fuction regenerate nginx/apache configs for all virtual hosts.   
__Notes__: Support disable restart httpd for multiple tasks (restart=0) and ignore errros (ignore=1)  
__Sample Output__:
```bash
bash bin/agent module=www func=domain_regen_web_all
{
    "status": "ok",
    "status_msg": "regenerate httpd conf for all domains complete."
}
```
###Fix dir permissions for subdomain without recursion
__Description__: Fuction will check dir structure and fix permissions in home dirs of subdomain without recursion.   
__Sample Output__:
```bash
# Fix dir permissions for subdomain without recursion
bash bin/agent module=www func=subdomain_chmody_rec_off subdomain=sub1.domain.com
{
    "status": "ok",
    "status_msg": "fixed permissions for subdomain sub1.domain.com with recursion off"
}
```
###Fix dir permissions for subdomain with recursion
__Description__: Fuction will check dir structure and fix permissions in home dirs of subdomain with recursion.   
__Sample Output__:
```bash
# Fix dir permissions for subdomain with recursion
bash bin/agent module=www func=subdomain_chmody_rec_on subdomain=sub1.domain.com
{
    "status": "ok",
    "status_msg": "fixed permissions for subdomain sub1.domain.com with recursion on"
}
```
###Update webstats for virtual host
__Description__: Update webstats (awstats/webalizer) for virtual host.   
__Sample Output__:
```bash
# Update webstats for virtual host domain.com
bash bin/agent module=www func=domain_stats_update domain=domain.com
{
    "status": "ok",
    "status_msg": "stats for domain.com has been updated"
}
```
###Update webstats for all virtual hosts
__Description__: Update webstats (awstats/webalizer) for all virtual hosts.   
__Sample Output__:
```bash
bash bin/agent module=www func=domain_stats_update_all
{
    "status": "ok",
    "status_msg": "stats for domain.com has been updated"
}
```
###Update webstats for all virtual hosts
__Description__: Update webstats (awstats/webalizer) for all virtual hosts.   
__Sample Output__:
```bash
# Update webstats for all virtual hosts
bash bin/agent module=www func=domain_stats_update_all
{
    "status": "ok",
    "status_msg": "ok"
}
```
### Restart Apache
__Description__: Restart web server Apache.   
__Sample Output__:
```bash
bash bin/agent module=www func=restart_apache
{
    "status": "ok",
    "status_msg": "ok"
}
```
### Restart Nginx
__Description__: Restart web server Nginx.   
__Sample Output__:
```bash
bash bin/agent module=www func=restart_nginx
{
    "status": "ok",
    "status_msg": "ok"
}
```
### Restart Nginx and Apache
__Description__: Restart both web servers.   
__Sample Output__:
```bash
bash bin/agent module=www func=restart
{
    "status": "ok",
    "status_msg": "ok"
}
```
### Reload Nginx and Apache
__Description__: Reload both web servers.   
__Sample Output__:
```bash
bash bin/agent module=www func=reload
{
    "status": "ok",
    "status_msg": "ok"
}
```
### Enable disk quota for virtual host
__Description__: Check and fix disk quota for virtual host.   
__Sample Output__:
```bash
# enable quita for domain.com
bash bin/agent module=www func=domain_quota_on domain=domain.com
{
    "status": "ok"
}
```
### kill account procs assigned to virtual host
__Description__: Check and kill system account procs.   
__Sample Output__:
```bash
# kill users procs of virtual host domain.com
bash bin/agent module=www func=domain_kill_proc domain=domain.com
{
    "status": "ok"
}
```
##IP (REST/CLI)
###Add ip address
__Description__: Add ip address to hagent db. IP must be pre-configured in the server.  
__Sample Output__:
```bash
# Add ip 192.168.1.1
GET /api/v1/?module=ip&func=create&ip=192.168.1.1
{
    "status": "ok",
    "status_msg": "Ip 192.168.1.1 created."
}
```
###Remove ip address
__Description__: Remove ip address from hagent db.  
__Sample Output__:
```bash
# Remove ip 192.168.1.1
GET /api/v1/?module=ip&func=delete&ip=192.168.1.1
{
    "status": "ok",
    "status_msg": "Ip 192.168.1.1 removed."
}
```
###Assign ip address to account
__Description__: Assign ip address to account.  
__Sample Output__:
```bash
# Assign ip address 192.168.1.1 to account a1000
GET /api/v1/?module=ip&func=assign&ip=192.168.1.1&account=a1000
{
    "status": "ok",
    "status_msg": "Ip 192.168.1.1 modified."
}
```
###Assign ip address to shared pool
__Description__: Make ip as shared for accounts.  
__Sample Output__:
```bash
# Make ip 192.168.1.1 as shared
GET /api/v1/?module=ip&func=assign&ip=192.168.1.1&account=shared
{
    "status": "ok",
    "status_msg": "Ip 192.168.1.1 modified."
}
```
###Unassign ip address for account
__Description__: Unassign ip address for account. If ip was assigned to any domains in account, all these domains will be reconfigured to shared ip.  
__Notes__: Support disable restart httpd (&restart=0).  
__Sample Output__:
```bash
# unassign ip 192.168.1.1 from account
GET /api/v1/?module=ip&func=free&ip=192.168.1.1
{
    "status": "ok",
    "status_msg": "Ip 192.168.1.1 modified."
}
```
##MYSQL (REST/CLI)
###Create database
__Description__: Create database.  
__Sample Output__:
```bash
# create database 'a1000_1' with login 'a1000_1' and password 'test'
GET /api/v1/?module=mysql&func=create&login=a1000_1&passwd=test&db=a1000_1&account=a1000
{
    "status": "ok",
    "status_msg": "MySQLDb a1000_1 created."
}
```
###Remove database
__Description__: Remove database.  
__Sample Output__:
```bash
# remove database 'a1000_1'
GET /api/v1/?module=mysql&func=delete&db=a1000_1
{
    "status": "ok",
    "status_msg": "MySQLDb a1000_1 removed."
}
```
###Change password to database
__Description__: Change password to database.  
__Sample Output__:
```bash
# change password 'newpass' to database 'a1000_1'
GET /api/v1/?module=mysql&func=passwd&db=a1000_1&passwd=newpass
{
    "status": "ok",
    "status_msg": "MySQLDb a1000_1 modified."
}
```
###Change login to database
__Description__: Change login to database.  
__Sample Output__:
```bash
# change login 'newlogin' to database 'a1000_1'
GET /api/v1/?module=mysql&func=login&db=a1000_1&login=newlogin
{
    "status": "ok",
    "status_msg": "MySQLDb a1000_1 modified."
}
```
###Lock access to database
__Description__: Lock access to database.  
__Sample Output__:
```bash
# lock access to database 'a1000_1'
GET /api/v1/?module=mysql&func=lock_on&db=a1000_1
{
    "status": "ok",
    "status_msg": "MySQLDb a1000_1 modified."
}
```
###Unlock access to database
__Description__: Unlock access to database.  
__Sample Output__:
```bash
# unlock access to database 'a1000_1'
GET /api/v1/?module=mysql&func=lock_off&db=a1000_1
{
    "status": "ok",
    "status_msg": "MySQLDb a1000_1 modified."
}
```
###Return raw database list
__Description__: Return 'show databases' sql request.  
__Sample Output__:
```bash
GET /api/v1/?module=mysql&func=raw_db_list
{
    "status": "ok",
    "status_msg": "ok",
    'databases': ['information_schema', 'a1000_1', 'a1000_2', 'mysql', 'performance_schema', 'test']}
}
```
###Return raw user statistics
__Description__: Return 'show user_statistics' sql request.  
__Sample Output__:
```bash
GET /api/v1/?module=mysql&func=raw_user_stats
{
    "status": "ok",
    "status_msg": "ok",
     'user_statistics': [['agent', 21, 0, 0, 0, 0, 1177, 0, 422, 74, 0, 24, 6, 4, 34, 0, 0, 0, 0, 0, 0, 0], ['a1000_1', 4, 0, 17, 0, 0, 250, 0, 0, 21, 0, 0, 5, 0, 3, 0, 0, 0, 0, 0, 0, 0]],
}
```
###Return raw user list
__Description__: Return 'SELECT * FROM mysql.user' sql request.  
__Sample Output__:
```bash
GET /api/v1/?module=mysql&func=raw_user_list
{
    "status": "ok",
    "status_msg": "ok",
    'users': [('127.0.0.1', 'root', '47685fe570438bcb', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', '', '', '', '', 0L, 0L, 0L, 0L, '', None)]
}
```
###Migrate all databases of account
__Description__: Migrate all databases assigned to account without removing on source server. Databases on destination server should be created before migration.  
__Sample Output__:
```bash
# migrate all databases of account a1000 to server 192.168.1.2
GET /api/v1/?module=mysql&func=migrate_account&account=a1000&server=192.168.1.2
{
    "status": "ok",
    "status_msg": "Migrated account a1000 to server 1192.168.1.2"
}
```
###Migrate database
__Description__: Migrate database without removing on source server. Database on destination server should be created before migration.  
__Sample Output__:
```bash
# migrate database 'a1000_1' to server 192.168.1.2
GET /api/v1/?module=mysql&func=migrate_database&db=a1000_1&server=192.168.1.2
{
    "status": "ok",
    "status_msg": "Migrated database a1000_1 to server 192.168.1.2"
}
```
##CRONTAB (REST/CLI)
###Create cron job
__Description__: Create cron job.  
__Sample Output__:
```bash
# create cron job 'a1000_12' (command 'echo 1') for virtual host domain.com,
# send output to mail@domain.com
GET /api/v1/?module=crontab&crontab=a1000_12&func=create&domain=domain.com&cmd=echo%201&m=1&h=2&dom=3&mon=4&dow=5&email=mail@domain.com
{
    "status": "ok",
    "status_msg": "Cron a1000_12 created."
}
```
###Remove cron job
__Description__: Remove cron job.  
__Sample Output__:
```bash
# remove cron job 'a1000_12' for virtual host domain.com
GET /api/v1/?module=crontab&func=delete&domain=domain.com&crontab=a1000_12
{
    "status": "ok",
    "status_msg": "Cron a1000_12 removed."
}
```
###Lock cron job
__Description__: Remove cron job, used in virtual host lock operation.  
__Sample Output__:
```bash
# lock cron job a1000_12
GET /api/v1/?module=crontab&func=lock_on&crontab=a1000_12
{
    "status": "ok",
    "status_msg": "Cron a1000_12 modified."
}
```
###Unlock cron job
__Description__: Create cron job, used in virtual host unlock operation.  
__Sample Output__:
```bash
# unlock cron job a1000_12
GET /api/v1/?module=crontab&func=lock_off&crontab=a1000_12
{
    "status": "ok",
    "status_msg": "Cron a1000_12 modified."
}
```
##STATISTICS (REST/CLI)
###Show disk usage for virtual host
__Description__: Show disk usage for virtual host.  
__Sample Output__:
```bash
# show disk usage for virtual host domain.com
GET /api/v1/?module=stats&func=domain_du_get&domain=domain.com
{
    "status": "ok",
    "bytes": 878590200
}
```
###Show disk usage for all virtual hosts
__Description__: Show disk usage for all virtual hosts.  
__Sample Output__:
```bash
GET /api/v1/?module=stats&func=domain_du_get_all
{
    "status": "ok",
    "shared": {"domain1.com": 278757, "domain2.com": 878468}}
}
```
###Show disk usage for mysql database
__Description__: Show disk usage for mysql database.  
__Sample Output__:
```bash
# show disk usage for mysql database a1000_2
GET /api/v1/?module=stats&func=mysql_du_get&db=a1000_2
{
    "status": "ok",
    "bytes": 878590200
}
```
###Show disk usage for all mysql databases
__Description__: Show disk usage for all mysql databases.  
__Sample Output__:
```bash
GET /api/v1/?module=stats&func=mysql_du_get_all
{
    "status": "ok",
    "mysql": {"testdb": 4161, "a1000_2": 17077, "a10000": 4161}
}
```
###Show disk usage for mail box
__Description__: Show disk usage for mail box.  
__Sample Output__:
```bash
# show disk usage for mail box user1@domain.com
GET /api/v1/?module=stats&func=xmail_du_get&email=user1@domain.com
{
    "status": "ok",
    "bytes": 878590200
}
```
###Show disk usage for all mail boxes
__Description__: Show disk usage for all mail boxes.  
__Sample Output__:
```bash
GET /api/v1/?module=stats&func=xmail_du_get_all
{
    "status": "ok",
    "mail": {"user3@domain11.com": 20595, "user2@domain11.com": 20585}
}
```
###Show disk usage for all resources on server
__Description__: Show disk usage for all resources (virtual_hosts/databases/mail_boxes) on server.  
__Sample Output__:
```bash
GET /api/v1/?module=stats&func=du_get_all
{
    "status": "ok",
    "shared": {"domain11.com": 2012333},
    "mail": {"user3@domain11.com": 20595, "user2@domain11.com": 20585},
    "mysql": {"a12213": 234443}
}
```
###Show traf usage for virtual host
__Description__: Show traffic usage (input/output) for virtual host.  
__Sample Output__:
```bash
# show traffic usage [input, output] for domain domain.com
GET /api/v1/?module=stats&func=domain_traf_get&domain=domain.com
{
    "status": "ok",
    "bytes": [4069, 55529]
}
```
###Show traf usage for all virtual hosts
__Description__: Show traffic usage (input/output) for all virtual hosts.  
__Sample Output__:
```bash
GET /api/v1/?module=stats&func=domain_traf_get_all
{
    "status": "ok",
    "shared": {"domain1.com": [4069, 55529], "domain2.com": [0, 0]}
}
```
###Show number of files for virtual host
__Description__: Show number of files owned by virtual host.  
__Sample Output__:
```bash
# Show number of files owned by domain.com
GET /api/v1/?module=stats&func=domain_nofiles_get&domain=domain.com
{
    "status": "ok",
    "nofiles": 5232
}
```
###Show number of files for all virtual hosts
__Description__: Show number of files owned by virtual hosts.  
__Sample Output__:
```bash
GET /api/v1/?module=stats&func=domain_nofiles_get_all
{
    "status": "ok",
    "nofiles": {"domain1.com": 4012, "domain2.com": 5332}
}
```
###Show LVE stats for all virtual hosts
__Description__: Show LVE (CloudLinux) stats of virtual hosts. Supported only for CloudLinux installation with CageFS enabled. Limits described in http://docs.cloudlinux.com/index.html?limits.html. Calculation is conducted by since the last time of the get command.   
__Sample Output__:
```bash
GET /api/v1/?module=stats&func=lve_get_all
{
    "status": "ok",
    "lvestats": {
        "a1000_1": {"EPf": 0, "aCPU": 0, "aNproc": 0, "NprocF": 0, "aEP": 0},
        "a93496_sc1": {"EPf": 0, "aCPU": 0, "aNproc": 0, "NprocF": 0, "aEP": 0}
    }
}
```
###Show mysql users CPU utilisation
__Description__: Show mysql users CPU utilisation. Calculation is conducted by since the last time of the get command.   
__Sample Output__:
```bash
# get users list with utilisation more then 5
GET /api/v1/?module=stats&func=mysql_cpu_get_all&limit=5
{
    "status": "ok",
    "total_cpu": 4112,
    "user_cpu_time": {
        "a30965_admin": 540,
        "a56263_vostok": 330
    }
}
```





##STATISTICS (CLI)
###Calculate disk usage for virtual host
__Description__: Calculate disk usage for virtual host.  
__Sample Output__:
```bash
# calculate disk usage for virtual host domain.com
bash bin/agent module=stats func=domain_du_calc domain=domain.com
{
    "status": "ok",
    "bytes": 239010
}
```
###Calculate disk usage for all virtual hosts
__Description__: Calculate disk usage for all virtual hosts.  
__Sample Output__:
```bash
bash bin/agent module=stats func=domain_du_calc_all
{
    "status": "ok"
}
```
###Calculate disk usage for mysql database
__Description__: Calculate disk usage for mysql database.  
__Sample Output__:
```bash
# calculate disk usage for mysql database a1000_2
bash bin/agent module=stats func=mysql_du_calc db=a1000_2
{
    "status": "ok",
    "bytes": 239010
}
```
###Calculate disk usage for all mysql databases
__Description__: Calculate disk usage for all mysql databases.  
__Sample Output__:
```bash
bash bin/agent module=stats func=mysql_du_calc_all
{
    "status": "ok"
}
```
###Calculate disk usage for mail box
__Description__: Calculate disk usage for mail box.  
__Sample Output__:
```bash
# calculate disk usage for mail box user1@domain.com
bash bin/agent module=stats func=xmail_du_calc email=user1@domain.com
{
    "status": "ok",
    "bytes": 239010
}
```
###Calculate disk usage for all mail boxes
__Description__: Calculate disk usage for mail boxes.  
__Sample Output__:
```bash
bash bin/agent module=stats func=xmail_du_calc_all
{
    "status": "ok",
}
```
###Calculate traffic usage for virtual host
__Description__: Calculate traffic usage for virtual host.  
__Sample Output__:
```bash
# calculate traffic usage for virtual host domain.com
bash bin/agent module=stats func=domain_traf_calc domain=domain.com
{
    "status": "ok",
    "bytes": [271, 1667]
}
```
###Calculate traffic usage for all virtual hosts
__Description__: Calculate traffic usage for all virtual hosts.  
__Sample Output__:
```bash
bash bin/agent module=stats func=domain_traf_calc_all
{
    "status": "ok"
}
```
###Calculate number of files for virtual host
__Description__: Calculate number of files for virtual host.  
__Sample Output__:
```bash
# calculate number of files for virtual host domain.com
bash bin/agent module=stats func=domain_nofiles_calc domain=domain.com
{
    "status": "ok",
    "nofiles": 522122
}
```
###Calculate number of files for all virtual hosts
__Description__: Calculate number of files for all virtual hosts.  
__Sample Output__:
```bash
bash bin/agent module=stats func=domain_nofiles_calc_all
{
    "status": "ok"
}
```
##BACKUP (REST/CLI)
###Show all backups
__Description__: Show all(web/mysql/mail) backups for server.  
__Sample Output__:
```bash
GET /api/v1/?module=backup&func=get_data
{
    "status": "ok",
    "backup": {
        "shared": {
            "domain1.com": ['2013.05.28.14.16', '2013.05.28.14.16'],
            "domain2.com": ['2013.06.11.13.38', '2013.02.24.17.55']
        },
        "mail": {},
        "mysql": {}
    }
}
```
###Show virtual host backups
__Description__: Show virtual host backups for server.  
__Notes__: To show extend backup information use (&extend=1).  
__Sample Output__:
```bash
# show backup for domain domain.com
GET /api/v1/?module=backup&func=domain_list&domain=domain.com
{
    "status": "ok",
    "backup": {
        ["2013.06.11.13.38", "2013.02.24.17.55"]
    }
}
```
###Show mysql backups
__Description__: Show mysql backups for server.  
__Notes__: To show extend backup information use (&extend=1).  
__Sample Output__:
```bash
# show backup for database a1000_2
GET /api/v1/?module=backup&func=mysql_list&db=a1000_2
{
    "status": "ok",
    "backup": {
        ["2013.09.11.13.31", "2013.09.24.18.55"]
    }
}
```
###Show mail backups
__Description__: Show mail backups for server.  
__Notes__: To show extend backup information use (&extend=1).  
__Sample Output__:
```bash
# show backup for mail domain domain.com
GET /api/v1/?module=backup&func=maildomain_list&maildomain=domain.com
{
    "status": "ok",
    "backup": {
        ["2014.10.13.13.02", "2014.10.13.18.01"]
    }
}
```
###Restore virtual host backup
__Description__: Restore virtual host backup.  
__Notes__: Use key (private=1) to restore files to separate directory private. Use key (&path=mypath) to restore files to directory 'mypath'  
__Sample Output__:
```bash
# restore path 'httpdocs' to directory 'private' from backup for date 2013.06.11,  domain domain1.com
GET /api/v1/?func=domain_restore&domain=domain1.com&date=2013.06.11.13.38&path=httpdocs&private=1
{
    "status": "ok",
    "status_msg": "restored backup for domain domain1.com at 2013.06.11.13.38"
 }
```
###Restore mysql backup
__Description__: Restore mysql database backup.  
__Sample Output__:
```bash
# restore database a1000_2 from data 2013.06.23.14.43
GET /api/v1/?module=backup&func=mysql_restore&db=a1000_2&date=2013.06.23.14.43
{
    "status": "ok",
    "status_msg": "restored backup for database a1000_2 at 2013.06.23.14.43"
 }
```
###Restore mail domain backup
__Description__: Restore backup for mail domain with all mail boxes.  
__Sample Output__:
```bash
# restore mail domain domain.com from data 2013.06.23.14.43
GET /api/v1/?module=backup&func=maildomain_restore*maildomain=domain.com&date=2013.06.23.14.16
{
    "status": "ok",
    "status_msg": "restored backup for domain.com at 2013.06.23.14.16"
 }
```
###Restore mail box backup
__Description__: Restore backup for mail box.  
__Sample Output__:
```bash
# restore mail box user1@domain.com from data 2013.06.23.14.43
GET /api/v1/?module=backup&func=mailuser_restore&email=user1@domain.com&date=2013.06.23.14.16
{
    "status": "ok",
    "status_msg": "restored backup for user1@domain.com at 2013.06.23.14.16
 }
```
##CLAMAV (REST/CLI)
###Show virus list for virtual host
__Description__: Show list of viruses found in files for virtual host.  
__Sample Output__:
```bash
# show list of viruses for domain domain1.com
GET /api/v1/?module=backup&module=clamav&func=get_domain&domain=domain1.com
{
    "status": "ok",
    "clamscan": {
        "domain1.com": ["var/www/vhosts/domain1.com/httpdocs/test/w19433511n.php: Trojan.PHP-43 FOUND", "/var/www/vhosts/domain1.com/httpdocs/test/w17558617n.php: Trojan.PHP-43 FOUND" ]
    }
}
```
###Show virus list for all virtual hosts
__Description__: Show list of viruses found in files for all virtual hosts.  
__Sample Output__:
```bash
GET /api/v1/?module=backup&module=clamav&func=get_all
{
    "status": "ok",
    "clamscan": {
        "domain1.com": ["var/www/vhosts/domain1.com/httpdocs/test/w19433511n.php: Trojan.PHP-43 FOUND", "/var/www/vhosts/domain1.com/httpdocs/test/w17558617n.php: Trojan.PHP-43 FOUND" ],
        "domain2.com": []
    }
}
```






##CLAMAV (CLI)
###Check virtual host for viruses
__Description__: Check virtual host for viruses. ClamAV used for checking.  
__Sample Output__:
```bash
# check domain1.com
bash bin/agent module=clamav func=scan_domain domain=domain1.com
{
    "status": "ok",
     "clamscan": 3
}
```
###Check all virtual hosts for viruses
__Description__: Check all virtual hosts for viruses. ClamAV used for checking.  
__Sample Output__:
```bash
bash bin/agent module=clamav func=scan_all
{
    "status": "ok"
}
```




##BACKUP (CLI)
###Collect backup stats from local file system
__Description__: Generate local backup list  /home/backup/backup.json on backup server, used by web/mysql/mail servers for backup list generation.  
__Sample Output__:
```bash
bash bin/agent module=backup func=collect_raw_data
{
    "status": "ok"
}
```
###Collect backup stats from backup server
__Description__: Generate local backup list based on stats from remote backup server.  
__Sample Output__:
```bash
bash bin/agent module=backup func=collect_data
{
    "status": "ok"
}
```






##ERROR RESPONSES
In case of an error, HAgent will return an error response in JSON format. The response contains status code and error message.  
For example, a badly formatted API call would return response below:
```json
{
    "status": "err",
    "status_msg": "uri has wrong format"
}
```
