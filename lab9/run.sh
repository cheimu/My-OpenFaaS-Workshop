# !/bin/bash

for i in {0..10000};
do
   echo -n "Post $i" | faas-cli invoke go-echo && echo;
done;