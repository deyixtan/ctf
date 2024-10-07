# Level 06 - Meownitoring

![](./assets/level-6-chall-desc.png)

## Solution

Extracting the attached `meownitoring.zip` gives us a `notes.md` file and several archives containing CloudTrail logs.

Here is the content of the `notes.md` file:

```md
# Workplan

Setup monitoring and logs analysis process for PALINDROME.
Compare products (we have 1 beta testing rights, need to source for others)

## Product 1: Meownitoring (Beta Test)

`https://d231g4hz442ywp.cloudfront.net`

1. Any sensitive info in logs / monitoring?
2. How secure is the setup?
3. Usefulness of dashboard? Buggy?
```

Accessing the given link, we see the following:

![](./assets/level-6-chall-website.png)

The website appears to be quite limited in features. Let's go ahead and register an account, then sign in to explore additional features.

![](./assets/level-6-registration.png)

After authenticating, we can observe a few functionalities: a dashboard that displays ingested logs, an option to export CloudTrail logs, an onboarding guide, and the ability to modify the ARN.

![](./assets/level-6-logged-in.png)

![](./assets/level-6-onboarding-guide.png)

![](./assets/level-6-modify-arn.png)

The export functionality doesn’t seem to work initially, so the next approach is to modify the ARN. By simply viewing any of the logs in the attached file, I quickly come across `arn:aws:iam::637423240666:user/dev`. When I attempt to modify the ARN with this value, I get an error on the dashboard. However, after this, the export functionality becomes available, providing an additional set of logs

After extracting the exported logs, I searched for all unique ARNs within them in an attempt to modify the ARN to each one. This can be done with the following command:

```sh
grep -hro 'arn:[a-zA-Z0-9_/-]*:[a-zA-Z0-9_/-]*:[a-zA-Z0-9_/-]*:[a-zA-Z0-9_/-]*:[a-zA-Z0-9_/-]*' ./637423240666 | uniq | sort | uniq
```

Output:

```
arn:aws:cloudtrail:ap-southeast-1:637423240666:trail/accountlogs
arn:aws:dataprotection::aws:data-identifier/AwsSecretKey
arn:aws:dynamodb:ap-southeast-1:637423240666:table/accounts
arn:aws:ec2:ap-southeast-1:637423240666:subnet/subnet-02c32bbc46e9cd52a
arn:aws:ec2:ap-southeast-1:637423240666:subnet/subnet-09057627c1459eaa8
arn:aws:execute-api:::
arn:aws:iam::533267020068:root
arn:aws:iam::637423240666:policy/debug_policy
arn:aws:iam::637423240666:policy/iam_policy_for_cloudtrail_role
arn:aws:iam::637423240666:policy/iam_policy_for_compiler_role
arn:aws:iam::637423240666:policy/iam-policy-for-meownitoring-role
arn:aws:iam::637423240666:policy/iam-policy-for-meownitoring-role-test
arn:aws:iam::637423240666:policy/iam_policy_for_processor_role
arn:aws:iam::637423240666:role/compiler_lambda_role
arn:aws:iam::637423240666:role/meownitoring-lambda-role
arn:aws:iam::637423240666:role/mewonitoring-lambda-test
arn:aws:iam::637423240666:role/processor_lambda_role
arn:aws:iam::637423240666:user/debug
arn:aws:iam::637423240666:user/deployer
arn:aws:iam::637423240666:user/dev
arn:aws:iam::aws:policy/AmazonAPIGatewayAdministrator
arn:aws:iam::aws:policy/CloudWatchLogsFullAccess
arn:aws:lambda:ap-southeast-1:637423240666:function
arn:aws:lambda:ap-southeast-1::runtime
arn:aws:logs:ap-southeast-1:637423240666:log-group
arn:aws:s3:::meownitoring2024trailbucket
arn:aws:s3:::meownitoringtmpbucket
arn:aws:sts::637423240666:assumed-role/meownitoring-lambda-role/logsloader
```

After trying all the ARNs from the previous command output, the only one that allowed me to modify the ARN without errors on the dashboard was `arn:aws:iam::637423240666:role/mewonitoring-lambda-test`. A subset of the ingested logs was then successfully retrieved and displayed on the dashboard.

![](./assets/level-6-some-logs.png)

What caught my attention was the third entry, which included the `aws_secret_access_key: e+4awZv0dnDaFeIbuvKkccqhjuNOr9iUb+gx/TMe`.

From here, I can try to find the correct access key in the logs and use it along with the secret key to access resources like S3 buckets. Running the command below reveals two unique buckets:

```sh
grep -hro 'arn:[a-zA-Z0-9_/-]*:[a-zA-Z0-9_/-]*:[a-zA-Z0-9_/-]*:[a-zA-Z0-9_/-]*:[a-zA-Z0-9_/-]*' ./637423240666 | uniq | sort | grep bucket | uniq
```

Output:

```
arn:aws:s3:::meownitoring2024trailbucket
arn:aws:s3:::meownitoringtmpbucket
```

In the dashboard logs, the word "debug" appears next to the secret key, which may be a hint. After manually searching through the logs, I found a `CreateAccessKey` event that creates an access key for the user `debug`. This could be the access key needed, along with the secret key, to access resources.

![](./assets/level-6-debug-access-key.png)

We can install the AWS CLI and attempt to access the resource:

```
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

We can configure the AWS CLI to interact with the resources. The following configuration was used (via `aws configure`):

```
AWS Access Key ID [None]: AKIAZI2LCYXNH62RXRH7
AWS Secret Access Key [None]: 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
Default region name [None]: ap-southeast-1
Default output format [None]:
```

I tried to list both S3 buckets (`meownitoring2024trailbucket`, `meownitoringtmpbucket`) and it worked:

![](./assets/level-6-meownitoring2024trailbucket.png)

![](./assets/level-6-meownitoringtmpbucket.png)

We can download the resources to our local machine using the following commands:

```sh
aws s3 sync s3://meownitoring2024trailbucket/ meownitoring2024trailbucket
aws s3 sync s3://meownitoringtmpbucket/ meownitoringtmpbucket
```

In the `meownitoringtmpbucket` directory, we find the first part of the flag in `flag1.txt`:

![](./assets/level-6-flag-part1.png)

Flag Part 1: `TISC{m@ny_inf0_frOm_l0gs_`

In `meownitoring2024trailbucket` there were more logs to be discovered. After searching for some time, I noticed a `CreateRoute` event which shows the creation of a new route in an API Gatway:

![](./assets/level-6-create-route-event.png)

From the [Amazon API Gateway Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-call-api.html), we can learn how to make a request to the API Gateway:

![](./assets/level-6-interact-api-gateway.png)

By making a request to the API Gateway using the information gathered so far, we can execute the following command, which returns the second part of the flag:

```sh
curl -X POST https://pxzfkfmjo7.execute-api.ap-southeast-1.amazonaws.com/5587y0s9d5aed/68fd47b8bf291eeea36480872f5ce29f0edb
```

![](./assets/level-6-flag-part2.png)

Flag Part 2: `&_me-0-wn1t0r1nNnG\\//[>^n^<]\\//}`

The flag is `TISC{m@ny_inf0_frOm_l0gs_&_me-0-wn1t0r1nNnG\\//[>^n^<]\\//}`.
