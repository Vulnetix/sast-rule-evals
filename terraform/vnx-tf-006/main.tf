# vnx-tf-006 eval target: EC2 instance still allowing IMDSv1
resource "aws_instance" "web" {
  ami           = "ami-0abcdef1234567890"
  instance_type = "t3.micro"

  metadata_options {
    http_endpoint = "enabled"
    http_tokens   = "optional" # TRIGGERS rule — IMDSv1 permitted, SSRF reaches credentials
  }
}
