Vagrant.configure("2") do |config|
config.vm.box = "debian/bookworm64"
config.vm.network "forwarded port", guest: 5000, host: 8080
config.vm.provision "shell", inline: <<-SHELL
        sudo apt update
        sudo apt install git nano vim python-is-python3 python3-venv python3-pip
        python -m venv flask_venv
        source flask_venv/bin/activate
        pip install Flask
SHELL

config.vm.provision "file", source: "hello.py", destination: "/home/vagrant/hello.py"
end
