// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-RUST-005: panic!/unwrap()/expect() in Result-returning function

use std::num::ParseIntError;

fn parse_port(s: &str) -> Result<u16, ParseIntError> {
    // TRIGGERS VNX-RUST-005: unwrap() inside a Result-returning function
    let n = s.parse::<i32>().unwrap();
    Ok(n as u16)
}

fn read_config(path: &str) -> Result<String, std::io::Error> {
    // TRIGGERS VNX-RUST-005: expect() inside a Result-returning function
    let content = std::fs::read_to_string(path).expect("Failed to read config file");
    Ok(content)
}

fn validate_input(input: &str) -> Result<(), String> {
    // TRIGGERS VNX-RUST-005: panic! inside a Result-returning function
    if input.is_empty() {
        panic!("Input must not be empty");
    }
    Ok(())
}
