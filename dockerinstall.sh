#!/bin/bash

# Exit on error
set -e

# Function to check if Docker is installed
check_docker_installed() {
    if command -v docker &> /dev/null; then
        echo "Docker is already installed. Version: $(docker --version)"
        exit 0
    fi
}

# Run the check
check_docker_installed

# Add Docker's official GPG key
echo "Updating package list and installing prerequisites..."
sudo apt-get update
sudo apt-get install -y ca-certificates curl

echo "Setting up Docker GPG key..."
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources
echo "Adding Docker repository..."
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

echo "Updating package list again..."
sudo apt-get update

# Install Docker packages
echo "Installing Docker packages..."
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Add current user to docker group
echo "Adding user '$USER' to docker group..."
sudo usermod -aG docker $USER

echo "Docker installation completed. You may need to log out and log back in for group changes to take effect."
