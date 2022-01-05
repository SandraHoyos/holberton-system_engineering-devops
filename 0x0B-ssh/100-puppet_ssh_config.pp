# using Puppet to make changes

file_line { 'sudo_rule':
      ensure => 'present',
      path   => '/etc/ssh/ssh_config',
      line   => 'IdentityFile ~/.ssh/school',
    }

file_line { 'sudo_rule_nopw':
      ensure => 'present',
      path   => '/etc/ssh/ssh_config',
      line   => 'PasswordAuthentication no',
    }
