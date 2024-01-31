# To run this docker file is simple and straight forward

### Step 1

git clone https://github.com/Simphiwe-303/Cap.git

cd Cap

### Step 2

Make sure you have docker and that it is running

docker build --tag **_name_** .

NB! **_name_** -> name your docker image with any name you like e.g myWebSite
NB! Please also note the full stop at the end of the command, the full stop must be there.

## When done with installations

docker run --publish 8000:8000 **_name_**
