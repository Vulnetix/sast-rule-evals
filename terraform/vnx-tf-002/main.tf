# Fake vulnerable Terraform for SAST evaluation - DO NOT USE IN PRODUCTION
# This file demonstrates VNX-TF-002: Security group with 0.0.0.0/0 ingress

resource "aws_security_group" "web_server" {
  name        = "web-server-sg"
  description = "Security group for web server"
  vpc_id      = var.vpc_id

  # VULNERABLE: Allows all traffic from internet on port 22 (SSH)
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # VULNERABLE: Allows all traffic from internet on all ports
  ingress {
    from_port   = 0
    to_port     = 65535
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # VULNERABLE: IPv6 unrestricted
  ingress {
    from_port        = 3389
    to_port          = 3389
    protocol         = "tcp"
    ipv6_cidr_blocks = ["::/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

variable "vpc_id" {}
