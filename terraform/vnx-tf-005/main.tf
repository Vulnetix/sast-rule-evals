# vnx-tf-005 eval target: EBS volume created without encryption
resource "aws_ebs_volume" "data" {
  availability_zone = "ap-southeast-2a"
  size              = 100
  encrypted         = false # TRIGGERS rule — data at rest is unencrypted
}
