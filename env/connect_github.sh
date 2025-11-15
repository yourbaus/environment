#!/bin/bash

# Check that user is an argument
if [ -z "$1" ]; then
    echo "Usage: connect_github <user>"
    return 1
fi
USER=$1

#file were all users stored 
users_path=$(awk -F'"' '/"users_path"/ {print $4}' ~/.leklab/leklab.json)
USER_LIST=$(eval echo "$users_path")

#extract the credentials from a file
CREDENTIALS=$( awk -F ', ' -v user=$USER '$1==user {print $0}' $USER_LIST)
if [ -z "$CREDENTIALS" ]; then
    echo "user $USER was not found in $USER_LIST"
    return 1
fi

#extract the credentials 
IFS=', ' read -r USER SSH_KEY USERNAME USEREMAIL <<< "$CREDENTIALS"

#Connecting to SSH and setting credits
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/$SSH_KEY

if [ $? -ne 0 ]; then
    echo "Failed to add SSH key"
    return 1
else
    git config --global user.name $USERNAME
    git config --global user.email $USEREMAIL
    echo "Set credentials for $USER"
fi