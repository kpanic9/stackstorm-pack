# stackstorm_training


## Install Pack

Login to StackStorm server via ssh  
```
export ST2_AUTH_TOKEN=`st2 auth -t <st2-username>`  
git clone git@github.com:kpanic9/stackstorm_training.git  
cd stackstorm_training/  
st2 pack install file://$PWD  
```


