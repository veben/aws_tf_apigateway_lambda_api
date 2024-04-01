# Readme

<img src="apigateway_lambda_api.drawio.svg" alt="apigateway_lambda_api.drawio.svg" style="width:500px;height:auto;">

## 1. 📝 Preparation
- Follow [installations](https://github.com/veben/aws_terraform_snippets/blob/main/readme.md)
- Choose **Cloud hosting** and follow "Installing" and "Initialization" steps

## 2. 🪂 Deploying
- Define `TF_VAR_client_id` and `TF_VAR_client_secret` env vars with `client_id` and `client_secret` values:
- Deploy the infrastructure
```sh
terraform init; terraform plan; terraform apply --auto-approve
```

> If you have not defined env vars, `client_id` and `client_secret` are prompted

## 3. 🧪 Test the pattern
- Log to the AWS console
- Go to **API Gateway** and test manually

## 4. 🚿 Cleaning
```sh
tf destroy
```
