# Docker-AI
Integrating AI services with docker container

# Install the docker in to Ubuntu server

clone the repo and install the docker with sh script

$sh dockerinstall.sh



# Prerequisites for Your Ubuntu VM
1. Update Your System

First, it's always best practice to update your system's package list and upgrade all installed packages to their latest versions.

Bash

# Update the package list
sudo apt update

# Upgrade the installed packages
sudo apt upgrade -y
2. Install Python and Pip

Ubuntu usually comes with Python pre-installed, but you'll need pip (the Python package installer) and venv (for creating isolated Python environments, which is highly recommended).

Bash

# Install pip and venv for Python 3
sudo apt install -y python3-pip python3-venv
3. Install Docker

This is the most important step. You need to install Docker to build and run your container.

Bash

# Install prerequisite packages
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common

# Add Docker's official GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Add the Docker repository to APT sources
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Update the package database with the Docker packages
sudo apt update

# Install the latest version of Docker
sudo apt install -y docker-ce docker-ce-cli containerd.io
Post-Installation Step (Highly Recommended):

To avoid having to type sudo every time you run a Docker command, add your user to the docker group.

Bash

sudo usermod -aG docker $USER
IMPORTANT: You will need to log out and log back in for this change to take effect.

4. Get Your Project Files

You need to have all the project files on your Ubuntu VM. This includes:

create_model.py

app.py

requirements.txt

Dockerfile

test_with_gemini.py

requirements-test.txt

You can get them onto the VM by either using git clone if they are in a repository, using scp (secure copy) from another machine, or simply creating the files manually with a terminal editor like nano.

For example, to create a file with nano:

Bash

nano create_model.py
Then, paste the code into the editor and press Ctrl+X, then Y, then Enter to save and exit.

Once you have completed these steps, your Ubuntu VM will be fully prepared. You can then proceed with the testing guide I provided earlier, starting with generating the model file.