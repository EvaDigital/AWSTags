import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_tags.aws_tags_stack import AwsTagsStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_tags/aws_tags_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsTagsStack(app, "aws-tags")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
