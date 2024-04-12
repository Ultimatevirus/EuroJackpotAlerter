# EuroJackpotAlerter
Simple program I made to send me an email when the EuroJackpot reaches 120 mil. It runs in a container, so you're free to deploy it either to the cloud or on site

Note that security is lacking concerning the email authentication.

>[!CAUTION]
>**_ONLY_ USE A THROWAWAY ACCOUNT!**


## Setting it up
First replace the placeholder values in config.json with the information you want to use.

Once config.json is cofigured don't forget to write the body of the email by editing mailbody.txt


## Building the docker image
To build the docker image, open a CLI in the folder directory.There all you have to do is run docker build 

>[!Tip]
> For help see Docker documentation: https://docs.docker.com/reference/cli/docker/image/build

## Deployment
You can run the container locally, however I recomend uploading it to the cloud as the container stops automatically after the script done running. Either way you'll need a trigger to make the container start periodically.

Eventually I'll add some code so it's self triggering.

