SHELL := /bin/bash

SERVICE_NAME = "default"
TEST_NAMES = "*"

ifeq ($(TEST_SERVER_MODE), true)
	# Exclude parallel tests
	TEST_EXCLUDE := --ignore tests/test_acm --ignore tests/test_amp --ignore tests/test_awslambda --ignore tests/test_batch --ignore tests/test_dynamodb --ignore tests/test_ec2 --ignore tests/test_s3/ --ignore tests/test_sqs
	# Parallel tests will be run separate
	PARALLEL_TESTS := ./tests/test_acm/ ./tests/test_acmpca/ ./tests/test_amp/ ./tests/test_awslambda ./tests/test_batch ./tests/test_dynamodb ./tests/test_ec2 ./tests/test_s3/ ./tests/test_sqs
else
	TEST_EXCLUDE := --ignore tests/test_batch --ignore tests/test_dynamodb --ignore tests/test_ec2 --ignore tests/test_s3/ --ignore tests/test_sqs
	PARALLEL_TESTS := ./tests/test_batch ./tests/test_dynamodb ./tests/test_ec2 tests/test_s3/ ./tests/test_sqs
endif

# Skip testing services that are not whitelisted for LocalStack
TEST_EXCLUDE += --ignore tests/test_amp
TEST_EXCLUDE += --ignore tests/test_apigatewaymanagementapi
TEST_EXCLUDE += --ignore tests/test_appconfig
TEST_EXCLUDE += --ignore tests/test_appmesh
TEST_EXCLUDE += --ignore tests/test_appsync
TEST_EXCLUDE += --ignore tests/test_athena
TEST_EXCLUDE += --ignore tests/test_awslambda
TEST_EXCLUDE += --ignore tests/test_awslambda_simple
TEST_EXCLUDE += --ignore tests/test_backup
TEST_EXCLUDE += --ignore tests/test_batch
TEST_EXCLUDE += --ignore tests/test_batch_simple
TEST_EXCLUDE += --ignore tests/test_bedrock
TEST_EXCLUDE += --ignore tests/test_bedrockagent
TEST_EXCLUDE += --ignore tests/test_budgets
TEST_EXCLUDE += --ignore tests/test_clouddirectory
TEST_EXCLUDE += --ignore tests/test_cloudformation
TEST_EXCLUDE += --ignore tests/test_cloudfront
TEST_EXCLUDE += --ignore tests/test_cloudhsmv2
TEST_EXCLUDE += --ignore tests/test_cloudtrail
TEST_EXCLUDE += --ignore tests/test_cognitoidp
TEST_EXCLUDE += --ignore tests/test_comprehend
TEST_EXCLUDE += --ignore tests/test_connect
TEST_EXCLUDE += --ignore tests/test_connectcampaigns
TEST_EXCLUDE += --ignore tests/test_databrew
TEST_EXCLUDE += --ignore tests/test_datapipeline
TEST_EXCLUDE += --ignore tests/test_datasync
TEST_EXCLUDE += --ignore tests/test_dax
TEST_EXCLUDE += --ignore tests/test_directconnect
TEST_EXCLUDE += --ignore tests/test_dms
TEST_EXCLUDE += --ignore tests/test_ds
TEST_EXCLUDE += --ignore tests/test_dsql
TEST_EXCLUDE += --ignore tests/test_dynamodb
TEST_EXCLUDE += --ignore tests/test_dynamodbstreams
TEST_EXCLUDE += --ignore tests/test_dynamodb_v20111205
TEST_EXCLUDE += --ignore tests/test_ebs
TEST_EXCLUDE += --ignore tests/test_ec2instanceconnect
TEST_EXCLUDE += --ignore tests/test_ecs
TEST_EXCLUDE += --ignore tests/test_efs
TEST_EXCLUDE += --ignore tests/test_eks
TEST_EXCLUDE += --ignore tests/test_elasticache
TEST_EXCLUDE += --ignore tests/test_elasticbeanstalk
TEST_EXCLUDE += --ignore tests/test_emrcontainers
TEST_EXCLUDE += --ignore tests/test_emrserverless
TEST_EXCLUDE += --ignore tests/test_es
TEST_EXCLUDE += --ignore tests/test_firehose
TEST_EXCLUDE += --ignore tests/test_forecast
TEST_EXCLUDE += --ignore tests/test_fsx
TEST_EXCLUDE += --ignore tests/test_glue
TEST_EXCLUDE += --ignore tests/test_greengrass
TEST_EXCLUDE += --ignore tests/test_guardduty
TEST_EXCLUDE += --ignore tests/test_inspector2
TEST_EXCLUDE += --ignore tests/test_ivs
TEST_EXCLUDE += --ignore tests/test_kafka
TEST_EXCLUDE += --ignore tests/test_kinesis
TEST_EXCLUDE += --ignore tests/test_kinesisanalyticsv2
TEST_EXCLUDE += --ignore tests/test_kinesisvideo
TEST_EXCLUDE += --ignore tests/test_kinesisvideoarchivedmedia
TEST_EXCLUDE += --ignore tests/test_kms
TEST_EXCLUDE += --ignore tests/test_lakeformation
TEST_EXCLUDE += --ignore tests/test_lexv2models
TEST_EXCLUDE += --ignore tests/test_macie
TEST_EXCLUDE += --ignore tests/test_mediaconnect
TEST_EXCLUDE += --ignore tests/test_medialive
TEST_EXCLUDE += --ignore tests/test_mediapackage
TEST_EXCLUDE += --ignore tests/test_mediapackagev2
TEST_EXCLUDE += --ignore tests/test_mediastore
TEST_EXCLUDE += --ignore tests/test_mediastoredata
TEST_EXCLUDE += --ignore tests/test_memorydb
TEST_EXCLUDE += --ignore tests/test_meteringmarketplace
TEST_EXCLUDE += --ignore tests/test_mq
TEST_EXCLUDE += --ignore tests/test_neptune
TEST_EXCLUDE += --ignore tests/test_networkfirewall
TEST_EXCLUDE += --ignore tests/test_networkmanager
TEST_EXCLUDE += --ignore tests/test_opensearch
TEST_EXCLUDE += --ignore tests/test_opensearchserverless
TEST_EXCLUDE += --ignore tests/test_organizations
TEST_EXCLUDE += --ignore tests/test_osis
TEST_EXCLUDE += --ignore tests/test_panorama
TEST_EXCLUDE += --ignore tests/test_personalize
TEST_EXCLUDE += --ignore tests/test_pipes
TEST_EXCLUDE += --ignore tests/test_polly
TEST_EXCLUDE += --ignore tests/test_quicksight
TEST_EXCLUDE += --ignore tests/test_rds
TEST_EXCLUDE += --ignore tests/test_rdsdata
TEST_EXCLUDE += --ignore tests/test_redshiftdata
TEST_EXCLUDE += --ignore tests/test_rekognition
TEST_EXCLUDE += --ignore tests/test_resiliencehub
TEST_EXCLUDE += --ignore tests/test_route53domains
TEST_EXCLUDE += --ignore tests/test_s3
TEST_EXCLUDE += --ignore tests/test_s3bucket_path
TEST_EXCLUDE += --ignore tests/test_s3tables
TEST_EXCLUDE += --ignore tests/test_s3vectors
TEST_EXCLUDE += --ignore tests/test_sagemakermetrics
TEST_EXCLUDE += --ignore tests/test_sagemakerruntime
TEST_EXCLUDE += --ignore tests/test_sdb
TEST_EXCLUDE += --ignore tests/test_securityhub
TEST_EXCLUDE += --ignore tests/test_servicecatalog
TEST_EXCLUDE += --ignore tests/test_servicecatalogappregistry
TEST_EXCLUDE += --ignore tests/test_servicediscovery
TEST_EXCLUDE += --ignore tests/test_servicequotas
TEST_EXCLUDE += --ignore tests/test_sesv2
TEST_EXCLUDE += --ignore tests/test_signer
TEST_EXCLUDE += --ignore tests/test_sns
TEST_EXCLUDE += --ignore tests/test_sqs
TEST_EXCLUDE += --ignore tests/test_stepfunctions
TEST_EXCLUDE += --ignore tests/test_synthetics
TEST_EXCLUDE += --ignore tests/test_timestreaminfluxdb
TEST_EXCLUDE += --ignore tests/test_timestreamquery
TEST_EXCLUDE += --ignore tests/test_timestreamwrite
TEST_EXCLUDE += --ignore tests/test_transfer
TEST_EXCLUDE += --ignore tests/test_vpclattice
TEST_EXCLUDE += --ignore tests/test_workspaces
TEST_EXCLUDE += --ignore tests/test_workspacesweb

init:
	@pip install -e .
	@pip install -r requirements-dev.txt

lint:
	@echo "Running ruff..."
	ruff check moto tests
	ruff format --check moto tests
	@echo "Running MyPy..."
	mypy --install-types --non-interactive

format:
	ruff format moto/ tests/
	ruff check --fix moto/ tests/

test-only:
	rm -f .coverage
	rm -rf cover
	pytest -sv -rs --cov=moto --cov-report xml ./tests/ $(TEST_EXCLUDE)
	# https://github.com/aws/aws-xray-sdk-python/issues/196 - Run these tests separately without Coverage enabled
	pytest -sv -rs ./tests/test_xray
	# Run tests that require a clean slate
	pytest -sv --cov=moto --cov-report xml --cov-append ./tests/ -m requires_clean_slate
	# Run parallel tests - except those that require a clean slate
	MOTO_CALL_RESET_API=false pytest -sv --cov=moto --cov-report xml --cov-append -n 4 $(PARALLEL_TESTS) --dist loadscope -m "not requires_clean_slate"

test: lint test-only

terraformtests:
	@echo "Make sure that the MotoServer is already running on port 4566 (moto_server -p 4566)"
	@echo "USAGE: make terraformtests SERVICE_NAME=acm TEST_NAMES=TestAccACMCertificate"
	@echo ""
	cd tests/terraformtests && bin/run_go_test $(SERVICE_NAME) "$(TEST_NAMES)"

publish:
	python -m build
	twine upload dist/*

test_server:
	@TEST_SERVER_MODE=true pytest -sv --cov=moto --cov-report xml ./tests/

aws_managed_policies:
	scripts/update_managed_policies.py

implementation_coverage:
	./scripts/implementation_coverage.py
	git commit IMPLEMENTATION_COVERAGE.md -m "Updating implementation coverage" || true

cloudformation_coverage:
	./scripts/cloudformation_coverage.py
	git commit CLOUDFORMATION_COVERAGE.md -m "Updating CloudFormation coverage" || true

coverage: implementation_coverage cloudformation_coverage

scaffold:
	@pip install -r requirements-dev.txt > /dev/null
	exec python scripts/scaffold.py

int_test:
	@./scripts/int_test.sh
