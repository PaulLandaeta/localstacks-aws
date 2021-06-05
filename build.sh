#create artifct
  aws cloudformation package --template-file template.yml --s3-bucket mycode-plandaeta --output-template-file jc-dev.yml

#create stack 
  aws cloudformation deploy --no-fail-on-empty-changeset --template-file jc-dev.yml --stack-name development --capabilities CAPABILITY_NAMED_IAM

