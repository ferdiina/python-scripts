#!/bin/sh
ps -ef| grep '/opt/streamsets/libexec'| grep -v grep |awk '{print $2}' |xargs kill -9