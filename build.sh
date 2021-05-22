#crear stactk
aws cloudformation create-stack --stack-name paul2 --template-body file://template.yml --endpoint-url http://localhost:4566

#eliminar stack
aws cloudformation delete-stack --stack-name 'paul2' --endpoint-url http://localhost:4566

# listar lambdas
aws lambda list-functions --endpoint-url http://localhost:4566

# create s3

aws s3api create-bucket --bucket my-lambda-functions --region us-east-1 --endpoint-url http://localhost:4566
aws s3api put-object --bucket my-lambda-functions --key PullMarketCode --region us-east-1  --body ./bin.zip --endpoint-url http://localhost:4566

#create artifct
  aws cloudformation package --template-file template.yml --s3-bucket mycode-plandaeta --output-template-file rpp-plandaeta.yml

#create stack 
  aws cloudformation deploy --no-fail-on-empty-changeset --template-file rpp-plandaeta.yml --stack-name development-paul --capabilities CAPABILITY_NAMED_IAM

