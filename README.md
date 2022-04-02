# Node-RED Cowboybike Strava sync
First of all a big thanks to [Samuel Dumont](https://github.com/samueldumont/) who gave me a start for this project.

## Setup
The first step is to create a folder where you will store all your files.
 * On Linux it will look something like this __/home/pi/CowboyMauro/__
 * On Windows it will look something like this C:\Users\mauro\Documents\CowboyMauro\

After you created this folder, download all the files and extract them in here.

![image](https://user-images.githubusercontent.com/46003176/161393712-e87d9de2-92b7-4e2e-91f5-5fa33cdb341c.png)

(You can delete the README.md)

### Cowboy Part
In the __Cowboy-Info.json__ file write down your Cowboy email and password.

### Strava Part
Create a Strava application.
This is how you do it:

https://user-images.githubusercontent.com/46003176/161383875-9528904f-6027-4826-9a69-1d9618ea18e4.mp4

In the __Strava-Info.json__ file write down your Strava client_id and your client_secret from the application you just created.

Open your browser and go to this URL: https://www.strava.com/oauth/authorize?client_id=YOURCLIENTID&redirect_uri=http://localhost&response_type=code&approval_prompt=auto&scope=activity:write,read

__DONT FORGET TO CHANGE THE CLIENT ID__

Click Authorize.

![image](https://user-images.githubusercontent.com/46003176/161384592-377337da-6a03-466c-b2d3-605bfdcaca6a.png)

Copy __YOUR__ code in the search balk

![image](https://user-images.githubusercontent.com/46003176/161384660-e580fc74-d53e-4f46-b6e8-32309ac733de.png)

Open [Postman](https://www.postman.com/downloads/), create a post request to https://www.strava.com/api/v3/oauth/token with these params:
| Key | Value |
| ------------- | ------------- |
| client_id  | ReplaceWithYourClientID  |
| client_secret  | ReplaceWithYourClientSecret  |
| code  | ReplaceWithYourCode  |
| grant_type  | authorization_code  |

![image](https://user-images.githubusercontent.com/46003176/161385188-bb01875d-ce48-4ee3-9a46-fb59233713c3.png)

Click the big blue __SEND__ button.

Click Save Response, Save to a file:

![Postman](https://user-images.githubusercontent.com/46003176/161385572-731ffc96-75fd-4534-9014-60ccfdb22589.png)

Put it in your folder as __Strava-Token.json__

### Python Part
Make sure that you have Python 3 installed.

Also make sure that these libraries are installed:

* Lxml
* Python_dateutil
* Requests

### Last but not least, the Node-RED Part

To import the Node-RED files, you just do this:

https://user-images.githubusercontent.com/46003176/161389972-d1cc66bb-9d04-4fb8-9d55-1147ee974093.mp4

All you need to do now is for every block that says: CHANGE FILE LOCATION, open that block and change __/home/pi/CowboyMauro__ to the path from the folder that you created at the beginning from this manual.

### Screenshots

![Screenshot_20220402-192420_Strava](https://user-images.githubusercontent.com/46003176/161394333-b766edd4-161c-4605-9669-79a305581d38.jpg)

![image](https://user-images.githubusercontent.com/46003176/161394084-37f7db0f-0165-4d81-a9b9-56859debf06b.png)
