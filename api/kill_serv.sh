#/bin/bash
pid_to_kill=$(netstat -anp | grep $1 | awk '{print $7}' | grep -o -P ".*?(?=\/)")
kill -9 $pid_to_kill

