![Holberton France Logo](https://images.squarespace-cdn.com/content/v1/60bf70d860f31b4f60455443/1625061110826-904UGWRZ9PX81YWARXMT/HolbertonFRANCEFichier+16.png?format=1500w)

# 0x1A. Application server

![DIAGRAM](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/9/c7d1ed0a2e10d1b4e9b3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220606%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220606T135936Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=83de492c3a12f214e57c4d015b2a85e8d1908d6d5eb12f038320a20ff73c32df)

## Background Context

Your web infrastructure is already serving web pages via ```Nginx``` that you installed in your first web stack project. While a web server can also serve dynamic content, this task is usually given to an application server. In this project you will add this piece to your infrastructure, plug it to your ```Nginx``` and make is serve your Airbnb clone project.

## Requirements
### General
- A ```README.md``` file, at the root of the folder of the project, is mandatory
- Everything Python-related must be done using ```python3```
- All config files must have comments
### Bash Scripts
- All your files will be interpreted on Ubuntu 16.04 LTS
- All your files should end with a new line
- All your Bash script files must be executable
- Your Bash script must pass ```Shellcheck``` (version ```0.3.7-5~ubuntu16.04.1``` via ```apt-get```) without any error
- The first line of all your Bash scripts should be exactly ```#!/usr/bin/env bash```
- The second line of all your Bash scripts should be a comment explaining what is the script doing
