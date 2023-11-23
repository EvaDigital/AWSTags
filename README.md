# Setting Up Development Environment

Follow these steps to set up your development environment on Windows. Make sure to install the necessary tools for a seamless development experience

## Installing Node.js and npm:
### Node.js
Download the Node.js installer from the [official website](https://nodejs.org/en)

Run the installer and follow the installation instructions.

### Check the installation
Open the command prompt and run the following commands:
```
node -v
npm -v
```
Verify that Node.js and npm are installed successfully.

### Python
Download the Python installer from the [official website](https://www.python.org/)

Run the installer and select the "Add Python to PATH" option during installation.

**The Python Installation Wizard will open. Ensure that you check the box that says "Add Python to PATH" during the installation**

### Check the installation
Open the command prompt and run the following commands:
```
python --version
pip --version
```
Confirm the successful installation of Python and pip.

Now, your development environment is ready for action.

# Deployment Guide!

## 1. Clone the project

## 2. Install AWS CLI
macOS and Linux: Install AWS CLI using package management tools. For example, on macOS, you can use Homebrew:
```
$ brew install awscli
``` 
if you are a Windows platform, you need follow this link and install from [AWS Official Site](https://aws.amazon.com/ru/cli/)

## 3. Configuring AWS CLI
After installing AWS CLI, run:
```
$ aws configure
```

## 4. Installing AWS CDK
Install AWS CDK using package management tools:
```
$ npm install -g aws-cdk
```

## 5. Create a virtualenv
```
$ python3 -m venv env
```
After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source env/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% env\Scripts\activate.bat
```

## 6. Install dependencies
Once the virtualenv is activated, you can install the required dependencies:
```
$ pip install -r requirements.txt
```

## 7. Synthesize the CloudFormation
At this point you can now synthesize the CloudFormation template for this code.
```
$ cdk synth
```

## 8. Deploy the project
```
$ cdk deploy
```
Upon successful deployment, you will receive outputs, and among them, you'll find a link to your deployed application. For example:
```
Outputs:
LambdaStack.TagsApiEndpointE7600750 = https://1ll1qaon91.execute-api.eu-central-1.amazonaws.com/prod/
```

This link, such as https://1ll1qaon91.execute-api.eu-central-1.amazonaws.com/prod/, is the endpoint for your AWS CDK application. Users can access your application through this URL.

## 9. Accessing the Deployed Website:
To access your deployed website, append index/login to the provided endpoint URL. For example:
```
https://1ll1qaon91.execute-api.eu-central-1.amazonaws.com/prod/index/login
```
By adding /index/login to the endpoint, you can navigate to the login page of your website. Adjust the path as needed based on your application's routing structure.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

