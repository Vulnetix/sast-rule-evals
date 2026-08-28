# vnx-tf-007 eval target: EKS cluster with a public API endpoint
resource "aws_eks_cluster" "primary" {
  name     = "primary"
  role_arn = aws_iam_role.eks.arn

  vpc_config {
    endpoint_public_access  = true # TRIGGERS rule — API server reachable from the internet
    endpoint_private_access = false
    subnet_ids              = ["subnet-0123456789abcdef0"]
  }
}
