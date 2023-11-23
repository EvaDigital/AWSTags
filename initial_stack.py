
import aws_cdk as core
import aws_cdk.aws_lambda as _lambda
import aws_cdk.aws_apigateway as apigateway
import aws_cdk.aws_iam as iam
from constructs import Construct



class LambdaStack(core.Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        lambda_role = iam.Role(
            self, "LambdaRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[iam.ManagedPolicy.from_aws_managed_policy_name("AdministratorAccess")]
        )

        get_tags_lambda = _lambda.Function(
            self, "GetTagsLambda",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="get_tags_function.lambda_handler",
            code=_lambda.Code.from_asset("lambda_functions/"),
            role=lambda_role
        )

        tag_policy = iam.PolicyStatement(
            actions=[
                "tag:GetResources"
            ],
            resources=["*"]
        )
        get_tags_lambda.role.attach_inline_policy(iam.Policy(self, "TagPolicy", statements=[tag_policy]))


        update_tags_lambda = _lambda.Function(
            self, "UpdateTagsLambda",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="update_tags_function.lambda_handler",
            code=_lambda.Code.from_asset("lambda_functions/"),
            role=lambda_role
        )

        update_tag_policy = iam.PolicyStatement(
            actions=[
                "tag:TagResources",
                "lambda:TagResource",
                "ec2:CreateTags",
                "ec2:DeleteTags",
                "s3:PutBucketTagging",
                "s3:DeleteBucketTagging",
                "rds:AddTagsToResource",
                "rds:RemoveTagsFromResource",
                "sqs:TagQueue",
                "sqs:UntagQueue",
                "sns:TagResource",
                "sns:UntagResource",
                "elasticloadbalancing:AddTags",
                "elasticloadbalancing:RemoveTags",
                "dynamodb:TagResource",
                "dynamodb:UntagResource",
                "elasticbeanstalk:AddTags",
                "elasticbeanstalk:RemoveTags",
                "redshift:CreateTags",
                "redshift:DeleteTags",
                "elasticmapreduce:AddTags",
                "elasticmapreduce:RemoveTags",
                "ecr:TagResource",
                "ecr:UntagResource",
                "ecs:TagResource",
                "ecs:UntagResource",
                "elasticache:AddTagsToResource",
                "elasticache:RemoveTagsFromResource",
                "cloudfront:TagResource",
                "cloudfront:UntagResource",
                "cloudwatch:TagResource",
                "cloudwatch:UntagResource",
                "glue:TagResource",
                "glue:UntagResource",
                "iam:TagUser",
                "iam:TagRole",
                "sagemaker:AddTags",
                "sagemaker:DeleteTags",
                "firehose:TagDeliveryStream",
                "firehose:UntagDeliveryStream",
                "eks:TagResource",
                "eks:UntagResource",
                "kms:TagResource",
                "kms:UntagResource",
                "logs:TagLogGroup",
                "logs:UntagLogGroup",
                "cloudtrail:AddTags",
                "cloudtrail:RemoveTags",
                "codepipeline:TagResource",
                "codepipeline:UntagResource",
                "waf-regional:TagResource",
                "waf-regional:UntagResource",
                "ecs:UntagTaskDefinition",
                "transcribe:TagResource",
                "transcribe:UntagResource",
                "appsync:TagResource",
                "appsync:UntagResource",
                "appmesh:TagResource",
                "appmesh:UntagResource",
                "cloud9:TagResource",
                "cloud9:UntagResource",
                "mediastore:TagResource",
                "mediastore:UntagResource",
                "servicecatalog:TagResource",
                "servicecatalog:UntagResource",
                "servicediscovery:TagResource",
                "servicediscovery:UntagResource",
                "transfer:TagResource",
                "transfer:UntagResource",
                ],
            resources=["*"]
        )
        update_tags_lambda.role.attach_inline_policy(iam.Policy(self, "UpdateTagPolicy", statements=[update_tag_policy]))
        

        get_tagged_resourses_lambda = _lambda.Function(
            self, "GetTaggedResoursesLambda",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="get_tagged_resourses.lambda_handler",
            code=_lambda.Code.from_asset("lambda_functions/"),
            role=lambda_role
        )

        tagging_policy = iam.PolicyStatement(
            actions=["resourcegroupstaggingapi:GetResources"],
            resources=["*"] 
        )
        get_tagged_resourses_lambda.role.attach_inline_policy(iam.Policy(self, "TaggingPolicy", statements=[tagging_policy]))


        page_lambda = _lambda.Function(
            self, "PageLambda",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="page_html.lambda_handler",
            code=_lambda.Code.from_asset("lambda_functions/"),
        )

        login_lambda = _lambda.Function(
            self, "LoginLambda",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="login.lambda_handler",
            code=_lambda.Code.from_asset("lambda_functions/"),
        )


        api = apigateway.RestApi(
            self, "TagsApi",
            rest_api_name="TagsApi",
            description="API Gateway for tags",
            default_method_options=apigateway.MethodOptions(api_key_required=False)
        )

        get_resourcies_integration = apigateway.LambdaIntegration(get_tagged_resourses_lambda)

        get_resourcies = api.root.add_resource("getresourses")
        get_resourcies_by_name = get_resourcies.add_resource("by-name")
        get_resourcies_by_tag = get_resourcies.add_resource("by-tag")
        get_resourcies_by_resource = get_resourcies.add_resource("by-resource")
        get_resourcies_by_owner = get_resourcies.add_resource("by-owner")
        get_resourcies_by_region = get_resourcies.add_resource("by-region")
        get_resourcies_tags_keys = get_resourcies.add_resource("get-tags-keys")
        get_resourcies_resources_names= get_resourcies.add_resource("get-resourses-names")

        get_resourcies.add_method("GET", get_resourcies_integration)
        get_resourcies_by_name.add_method("POST", get_resourcies_integration)
        get_resourcies_by_tag.add_method("POST", get_resourcies_integration)
        get_resourcies_by_resource.add_method("POST", get_resourcies_integration)
        get_resourcies_by_owner.add_method("POST", get_resourcies_integration)
        get_resourcies_by_region.add_method("POST", get_resourcies_integration)
        get_resourcies_tags_keys.add_method("GET", get_resourcies_integration)
        get_resourcies_resources_names.add_method("GET", get_resourcies_integration)


        get_tags_resource = api.root.add_resource("gettags")
        get_tags_integration = apigateway.LambdaIntegration(get_tags_lambda)
        get_tags_resource.add_method("POST", get_tags_integration)

        update_tags_resource = api.root.add_resource("updatetags")
        update_tags_integration = apigateway.LambdaIntegration(update_tags_lambda)
        update_tags_resource.add_method("POST", update_tags_integration)

        page_resource = api.root.add_resource("index")
        page_resource_index_login = page_resource.add_resource("login")
        page_resource_index_home = page_resource.add_resource("home")
        page_resource_index_tags = page_resource.add_resource("tags")
        page_integration = apigateway.LambdaIntegration(page_lambda)
        page_resource.add_method("GET", page_integration)
        page_resource_index_login.add_method("GET", page_integration)
        page_resource_index_home.add_method("GET", page_integration)
        page_resource_index_tags.add_method("GET", page_integration)

        login_resource = api.root.add_resource("login")
        login_integration = apigateway.LambdaIntegration(login_lambda)
        login_resource.add_method("POST", login_integration)




