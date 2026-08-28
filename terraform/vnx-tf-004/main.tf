# vnx-tf-004 eval target: IAM policy granting a wildcard Action
resource "aws_iam_role_policy" "admin_everything" {
  name = "admin-everything"
  role = aws_iam_role.app.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect   = "Allow"
        Action   = "*" # TRIGGERS rule — every action on every service
        Resource = "*"
      }
    ]
  })
}
