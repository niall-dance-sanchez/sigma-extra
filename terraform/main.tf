provider "aws" {
    region = vars.AWS_REGION
    access_key = var.AWS_ACCESS_KEY
    secret_key = var.AWS_SECRET_KEY
}

data "aws_vpc" "cohort-vpc"{
    id = ""
}

data "aws_subnet" "public-cohort-subnet"{
    id = ""
}

resource "aws_security_group" "c19-niall-tf-sg" {
  vpc_id = data.aws_vpc.cohort-vpc.id

  ingress {
    cidr_blocks = ["0.0.0.0/0"]
    from_port = 22
    to_port = 22
    protocol = "tcp"
  }
}

resource "aws_instance" "" {
  ami = "ami-0cfb394ad   "
  instance_type = "t2.nano"

  tags = {
    Name = "c19-niall-tf-example"
  }
  vpc_security_group_ids = ""
  subnet_id = data.aws_subnet.public-cohort-subnet.id
}