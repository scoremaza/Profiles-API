# Profiles Rest API
 
 Here we have the Profile-API 
 
 With this source code you will be required to create an environment to run your instance on your local machine or server. Having that in mind Vagrant is the selection chosen to allow building in an consistent manor across platforms. VirtualBox is required for Vagrant to work so you can download VirtualBox on [Virtualbox](https://www.virtualbox.org/wiki/Downloads "VirtualBox") site. Install the software for your operating system first. To build the external OS in your platform download [Vagrant](https://www.vagrantup.com/downloads "Vagrant"). After installing Vagrant you can then move to the Terminal or Command Window and write this line. 
 
 vagrant init ubuntu/bionic64


Here we are creating a file with instructions to activate and create your workspace for your operating system. In this file you will see comment out code take the time to highlight the code and erase them. Highlight the VagrantFile in your pull to copy all the content and place it in the newly created Vagrantfile. Next you will have to take this command and place it into your Command Window or Terminal. 
```
vagrant up
```
After you create the instance of your Operating System with your Vagrantfile completed write this in your terminal or Command Window 
```
vagrant ssh
```
Here you are viewing the terminal of your newly create version of Ubuntu this will also have a folder create to be linked to your current directory on your local computer.  