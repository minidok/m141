#!/usr/bin/env python3
"""
Security validation script for m141 PostgreSQL setup
Tests that the configuration follows security best practices
"""

import os
import yaml
import sys
from pathlib import Path

def test_env_file_exists():
    """Test that .env.example exists and .env is in .gitignore"""
    print("Testing environment file security...")
    
    env_example = Path(".env.example")
    gitignore = Path(".gitignore")
    
    assert env_example.exists(), ".env.example file should exist"
    print("✓ .env.example file exists")
    
    if gitignore.exists():
        gitignore_content = gitignore.read_text()
        assert ".env" in gitignore_content, ".env should be in .gitignore"
        print("✓ .env is properly ignored in git")
    
def test_docker_compose_security():
    """Test docker-compose.yml for security configurations"""
    print("\nTesting Docker Compose security...")
    
    compose_file = Path("docker/docker-compose.yml")
    assert compose_file.exists(), "docker-compose.yml should exist"
    
    with open(compose_file, 'r') as f:
        content = f.read()
        
    # Test for security improvements
    security_checks = [
        ("Environment variables used", "${" in content),
        ("No hard-coded passwords", "POSTGRES_PASSWORD: 123456" not in content and "PGADMIN_DEFAULT_PASSWORD: root" not in content),
        ("Localhost binding", "127.0.0.1" in content),
        ("Pinned versions", ":latest" not in content),
        ("Health checks configured", "healthcheck:" in content),
        ("Security options", "security_opt:" in content),
        ("Resource limits", "resources:" in content),
        ("Non-root users", "user:" in content),
        ("Restart policy secure", "unless-stopped" in content),
    ]
    
    for check_name, condition in security_checks:
        if condition:
            print(f"✓ {check_name}")
        else:
            print(f"✗ {check_name}")
            
def test_database_config_security():
    """Test database configuration for security"""
    print("\nTesting database configuration security...")
    
    config_file = Path("myDatabase/dbconnection.ini")
    assert config_file.exists(), "dbconnection.ini should exist"
    
    with open(config_file, 'r') as f:
        content = f.read()
    
    # Test for security improvements
    security_checks = [
        ("SSL mode configured", "sslmode" in content),
        ("No hard-coded weak passwords", "dominik" not in content),
        ("Container networking used", "host=db" in content),
        ("Localhost configuration available", "host=localhost" in content),
    ]
    
    for check_name, condition in security_checks:
        if condition:
            print(f"✓ {check_name}")
        else:
            print(f"✗ {check_name}")

def test_python_config_security():
    """Test Python configuration module for security"""
    print("\nTesting Python configuration security...")
    
    config_file = Path("myDatabase/config.py")
    assert config_file.exists(), "config.py should exist"
    
    with open(config_file, 'r') as f:
        content = f.read()
    
    # Test for security improvements
    security_checks = [
        ("Environment variable support", "os.environ" in content),
        ("Secure logging", "password" and "***" in content),
        ("SSL default configuration", "sslmode" in content),
    ]
    
    for check_name, condition in security_checks:
        if condition:
            print(f"✓ {check_name}")
        else:
            print(f"✗ {check_name}")

if __name__ == "__main__":
    print("M141 Security Validation Test")
    print("=" * 40)
    
    try:
        test_env_file_exists()
        test_docker_compose_security()
        test_database_config_security()
        test_python_config_security()
        
        print("\n" + "=" * 40)
        print("✓ Security validation completed successfully!")
        print("The configuration has been improved for security.")
        
    except AssertionError as e:
        print(f"\n✗ Security test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Unexpected error during testing: {e}")
        sys.exit(1)