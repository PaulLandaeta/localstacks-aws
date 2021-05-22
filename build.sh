aws --endpoint-url=http://localhost:4566 cloudformation deploy \
    --no-fail-on-empty-changeset \
    --template-file template.yml \
    --stack-name paul \