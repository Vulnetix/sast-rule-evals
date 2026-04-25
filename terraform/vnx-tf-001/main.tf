# Fake vulnerable Terraform for SAST evaluation - DO NOT USE IN PRODUCTION
# This file demonstrates VNX-TF-001: S3 bucket with public ACL

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

# VULNERABLE: public-read ACL exposes all bucket objects to the internet
resource "aws_s3_bucket" "public_assets" {
  bucket = "my-app-public-assets"
}

resource "aws_s3_bucket_acl" "public_assets_acl" {
  bucket = aws_s3_bucket.public_assets.id
  acl    = "public-read"
}

# VULNERABLE: public-read-write is even worse
resource "aws_s3_bucket" "shared_bucket" {
  bucket = "my-shared-data"
  acl    = "public-read-write"
}
