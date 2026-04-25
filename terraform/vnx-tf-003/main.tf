# Fake vulnerable Terraform for SAST evaluation - DO NOT USE IN PRODUCTION
# This file demonstrates VNX-TF-003: RDS instance publicly accessible

resource "aws_db_instance" "app_database" {
  identifier        = "app-production-db"
  engine            = "mysql"
  engine_version    = "8.0"
  instance_class    = "db.t3.medium"
  allocated_storage = 20

  db_name  = "appdb"
  username = "admin"
  password = var.db_password

  # VULNERABLE: Database accessible from the internet
  publicly_accessible = true

  skip_final_snapshot = false
}

# VULNERABLE: RDS cluster also publicly accessible
resource "aws_rds_cluster" "aurora_cluster" {
  cluster_identifier = "aurora-cluster"
  engine             = "aurora-mysql"
  master_username    = "root"
  master_password    = var.db_password

  publicly_accessible = true
}

variable "db_password" {
  sensitive = true
}
