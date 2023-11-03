provider "aws" {
  region = "us-east-1" 
}
 
resource "aws_instance" "my_ec2" {
  ami           = "ami-0fc5d935ebf8bc3bc"
  instance_type = "t2.micro"
  key_name      = "demo-aws"
  security_groups = [aws_security_group.my_ec2.id]
  subnet_id = "subnet-0c5aa8fed2f503cf2"
  tags = {
    Name = "My instance"
  }
}

output "My_ip"{
  value = aws_instance.my_ec2.public_ip
}

resource "aws_security_group" "my_ec2" {
  name        = "aws-group-6"
  description = "Security Group"
  vpc_id = "vpc-0dc979631fedb2186"
 
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  
  }
 
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  
  }
  
    ingress {
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  
  }

  ingress {
    from_port   = 9090
    to_port     = 9090
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  
  }
  
  egress {
    from_port = 0
    to_port = 0
    protocol = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
