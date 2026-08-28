# vnx-tf-008 eval target: AWS provider with credentials hardcoded in source
provider "aws" {
  region     = "ap-southeast-2"
  access_key = "AKIAIOSFODNN7EXAMPLE"                     # TRIGGERS rule
  secret_key = "wJalrXUtnFEMIK7MDENGbPxRfiCYEXAMPLEKEYXX" # TRIGGERS rule
}
