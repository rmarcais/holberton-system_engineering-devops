# Installs puppet_lint

package { 'puppet-lint':
name => 'puppet-lint'
ensure   => '2.5.0',
provider => 'gem',
}
