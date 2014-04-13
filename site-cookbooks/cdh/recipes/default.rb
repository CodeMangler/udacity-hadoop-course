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

template '/etc/hadoop/conf/core-site.xml' do
  source 'core-site.xml.erb'
end

template '/etc/hadoop/conf/hdfs-site.xml' do
  source 'hdfs-site.xml.erb'
end

template '/etc/hadoop/conf/mapred-site.xml' do
  source 'mapred-site.xml.erb'
end

template '/usr/local/bin/hs' do
  source 'hs.erb'
end

template '/usr/local/bin/hsc' do
  source 'hsc.erb'
end

directory '/var/lib/hadoop-hdfs/cache/hdfs/dfs/name' do
 owner 'hdfs'
 group 'hadoop'
 mode 00744
 action :create
 recursive true
end

['/usr/local/bin/hs', '/usr/local/bin/hsc'].each do |file_name|
  file file_name do
    mode 00755
  end
end

%w(hadoop-0.20-mapreduce-jobtracker hadoop-0.20-mapreduce-tasktracker hadoop-hdfs-datanode hadoop-mapreduce-historyserver hadoop-yarn-nodemanager hadoop-yarn-resourcemanager).each do |service_name|
  service service_name do
   supports restart: true, start: true, stop: true, status: true
   action [:enable, :start]
  end
end

script "format namenode" do
 interpreter "bash"
 user "hdfs"
 code <<-SCRIPT
hdfs namenode -format -force
 SCRIPT
end

service 'hadoop-hdfs-namenode' do
 supports restart: true, start: true, stop: true, status: true
 action [:enable, :start]
end

script 'create HDFS home directory for the vagrant user' do
  interpreter "bash"
  user "vagrant"
  code <<-SCRIPT
hadoop fs -mkdir -p /user/vagrant
  SCRIPT
end
