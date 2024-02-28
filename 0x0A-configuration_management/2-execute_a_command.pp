#!/usr/bin/env bash
#kill process

exec {'pkill':
command => 'pkill killmenow',
path    => ['bin','/usr/bin'],
}
