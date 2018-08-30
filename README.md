# splatoon2_notificater

### Automatically deployed components to AWS
* [AWS Lambda](https://aws.amazon.com/lambda/)


## Installation Guide
First, please clone this repository to your development environment.
```
$ git clone https://github.com/yfujit/splatoon2_notificater.git
```

### [Slack](https://slack.com/)

Slack is one of the most popular chat tools. splatoon2_notificater notify team members to use Slack Incoming Webhook.

#### Incoming Webhook
Incoming Webhooks are a simple way to post messages from external sources into Slack. Please show Official page.

#### Configure webhookurl.yml
Create config/credentials.yml and configure WEBHOOK_URL and IKSM_SESSION.
```
$ cp config/credentials.yml.sample config/credentials.yml

$ vi config/credentials.yml
WEBHOOK_URL: SET_YOUR_SLACK_INCOMING_WEBHOOK_URL #Please Change
IKSM_SESSION: SET_YOUR_IKSM_SESSION #Please Change
```


### [Serverless](https://serverless.com/)
Serverless is toolkit for deploying and operating serverless architectures.

1. Install Serverless Globally
    ```
    $ npm install -g serverless
    ```
2. Check Serverless command
    ```
    $ serverless -h
    ```

## How to use
Conguraturation! With just this command your Splatoon life is better than before.
```
$ sls deploy --region {AWS Regions}
```
Default Parameters

* region : ap-northeast-1

#### example
```
$ sls deploy --region us-east-1
```
