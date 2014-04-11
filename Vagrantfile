Vagrant.configure('2') do |config|
  config.vm.box = 'centos6.4'
  config.vm.box_url = 'http://developer.nrel.gov/downloads/vagrant-boxes/CentOS-6.4-x86_64-v20130309.box'
  config.vm.synced_folder '.', '/home/vagrant/cdh'

  config.vm.define :cdh do |cdh|
    public_ip = "10.201.112.42"

    cdh.vm.network :private_network, ip: public_ip
    cdh.vm.hostname = "cdh.local"

    cdh.vm.provider :virtualbox do |vb|
      vb.name = "cdh"
      vb.customize ["modifyvm", :id, "--memory", 1024]
    end

    cdh.vm.provision :chef_solo do |chef|
      chef.cookbooks_path = "cookbooks"
      chef.add_recipe "yum"
      chef.add_recipe "java"
      chef.add_recipe "cdh"

      chef.log_level = :debug

      chef.json = {
      }
    end
  end
end
