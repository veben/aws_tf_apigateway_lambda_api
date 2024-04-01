output "ConsumerFunction" {
  value       = aws_lambda_function.lambda_function.arn
  description = "ConsumerFunction function name"
}

output "Api" {
  value       = aws_api_gateway_rest_api.api.id
  description = "API id"
}

output "ApiResource" {
  value       = aws_api_gateway_resource.resource.id
  description = "API resource id"
}