## Cookbook Name:: freeswitch
## Recipe:: default
##

## Build requirements
package 'git-core'
package 'rpm-build'

template '/etc/yum.repos.d/cdh5.repo' do
  source 'cdh5.repo.erb'
end

%w(hadoop-yarn-resourcemanager hadoop-hdfs-namenode hadoop-yarn-nodemanager hadoop-hdfs-datanode hadoop-mapreduce hadoop-mapreduce-historyserver hadoop-yarn-proxyserver hadoop-client).each do |pkg|
  package pkg do
    action :upgrade
  end  
end

%w(hadoop-0.20-mapreduce-jobtracker hadoop-0.20-mapreduce-tasktracker hadoop-hdfs-datanode).each do |pkg|
  package pkg do
    action :upgrade
  end  
end
